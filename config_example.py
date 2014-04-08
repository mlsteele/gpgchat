# Client configuration

import gpgio

SERVER_HOSTNAME = "localhost"
SERVER_PORT = 8387

RECIPIENTS = ["Jess", "Anna", "Miles"]
# RECIPIENTS = [
#   "Miles Steele <miles@milessteele.com>",
#   "Jess Kenney <seveneightn9ne@gmail.com>",
#   "Anna Walsh (octopus) <awalsh28@mit.edu>",
# ]

SIGNER_FINGERPRINT = gpgio.find_local_key("Miles")['fingerprint']
# SIGNER_FINGERPRINT = "1F5DE74F4D4E8884775F2BF1514FC07220D4A61A"
