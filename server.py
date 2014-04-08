import re
import zmq

class Server(object):
  def __init__(self):
    self.context = zmq.Context()
    self.sock = self.context.socket(zmq.REP)
    self.sock.bind('tcp://*:8387')

    self.messages = []

  def listen(self):
    while True:
      msg = self.sock.recv()
      mtype = re.match("(.*)\n", msg).groups(1)[0]
      if mtype == "send":
        self._receive_message(msg[len("send\n"):])
        self.sock.send("OK")
      elif mtype == "fetchmessage":
        index = re.match(".*\n(.*)", msg).groups(1)[0]
        index = int(index)
        self.sock.send(self._fetch_message(index))
      else:
        print "Unrecognized message type: {}".format(mtype)

  def _receive_message(self, msg):
    print "Message received."
    print msg
    self.messages.append(msg)

  def _fetch_message(self, index):
    print "Client asked for message {}".format(index)
    if index < len(self.messages):
      print "  responding with message."
      return self.messages[index]
    else:
      print "  responding NOMESSAGE."
      return "NOMESSAGE"


s = Server()
s.listen()
