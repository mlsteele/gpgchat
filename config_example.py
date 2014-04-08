"""
Client and server configuration.
"""

import gpgio

SERVER_HOSTNAME = "localhost"
SERVER_PORT = 8387

RECIPIENTS = [
  "miles@milessteele.com",
  "seveneightn9ne@gmail.com",
  "awalsh28@mit.edu",
]
# RECIPIENTS = ["Jess", "Anna", "Miles"]

SIGNER_FINGERPRINT = gpgio.find_local_key("Miles")['fingerprint']
# SIGNER_FINGERPRINT = "1F5DE74F4D4E8884775F2BF1514FC07220D4A61A"
