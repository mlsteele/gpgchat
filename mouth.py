import zmq
import gpgio
import config

class TalkClient(object):
  def __init__(self):
    self.context = zmq.Context()
    self.sock = self.context.socket(zmq.REQ)
    dest = "tcp://{}:{}".format(config.SERVER_HOSTNAME, config.SERVER_PORT)
    self.sock.connect(dest)


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
  msg_prompt = "Enter your message ending in ^D on a newline:"
  msg = gpgio.prompt_encrypt(
    prompt=msg_prompt,
    recipients=config.RECIPIENTS,
    sign=config.SIGNER_FINGERPRINT)
  print ""
  c.send_message(msg)
  print ""
