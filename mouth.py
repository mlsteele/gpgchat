import zmq
import gpgio

class TalkClient(object):
  def __init__(self):
    self.context = zmq.Context()
    self.sock = self.context.socket(zmq.REQ)
    self.sock.connect('tcp://localhost:8387')

  def send_message(self, msg):
    packet = "send\n{}".format(msg)
    print "Sending message... ",
    self.sock.send(packet)
    response = self.sock.recv()
    if response != "OK":
      raise RuntimeError("Message send failed.")
    print "message received"


c = TalkClient()

while True:
  msg = gpgio.prompt_encrypt()
  c.send_message(msg)
