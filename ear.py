"""
ear
Client for receiving messages
"""

import os
import subprocess
import time
import zmq
import gpgio
import config

DEBUG = False

class ListenClient(object):
  def __init__(self):
    self.context = zmq.Context()
    self.sock = self.context.socket(zmq.REQ)
    dest = "tcp://{}:{}".format(config.SERVER_HOSTNAME, config.SERVER_PORT)
    self.sock.connect(dest)

  def fetch_message(self, index):
    packet = "fetchmessage\n{}".format(index)
    if DEBUG: print "Fetching message {}... ".format(index),
    self.sock.send(packet)
    response = self.sock.recv()
    if response == "NOMESSAGE":
      if DEBUG: print "no message yet"
      return None
    else:
      if DEBUG: print "message received"
      return response

  def fetch_messages_since(self, last_index):
    new_messages = []
    msg = self.fetch_message(last_index + 1)
    while msg != None:
      last_index += 1
      new_messages.append((last_index, msg))
      msg = self.fetch_message(last_index + 1)
    return new_messages


c = ListenClient()
last_message_index = -1

while True:
  time.sleep(1)
  new_messages = c.fetch_messages_since(last_message_index)
  for (index, message) in new_messages:
    print "\n\n\n------ BEGIN MESSAGE {} ------".format(index)
    try:
      print gpgio.decrypt(message)
      with open(os.devnull, 'w') as devnull:
        subprocess.Popen(["mpg123", "blip.mp3"], stdout=devnull, stderr=devnull)
    except gpgio.DecryptionError:
      print "ERROR: Failed to decrypt message."
    print "------ END MESSAGE   {} ------".format(index)
    last_message_index = index
