#!/usr/bin/env python

import gnupg

gpg = gnupg.GPG()

class DecryptionError(RuntimeError):
  pass
class EncryptionError(RuntimeError):
  pass

def multiline_input(prompt=None):
  if prompt:
    print(prompt)
  s = ""
  try:
    while True:
      s += "\n" + raw_input()
  except EOFError:
    return s + "\n"

def find_local_key(query):
  """
  Search for a local key
  query - a name to search for e.g. "Miles"
  returns a dict of key info from gpg.list_keys
  """
  matches = []
  for key in gpg.list_keys():
    search_items = key['uids'] + [key['keyid']]
    if any(query in item for item in search_items):
      matches.append(key)

  if len(matches) == 0:
    raise RuntimeError("no matches")
  elif len(matches) == 1:
    return matches[0]
  else:
    raise RuntimeError("ambiguous query, many matches")


DEFAULT_RECIPIENTS = ["Jess", "Anna", "Miles"]
DEFAULT_SIGNER_FINGERPRINT = find_local_key("Miles")['fingerprint']

def prompt_encrypt():
  msg_prompt = "Enter your message ending in ^D on a newline:"
  msg_cleartext = multiline_input(msg_prompt)
  crypt = gpg.encrypt(msg_cleartext, DEFAULT_RECIPIENTS, sign=DEFAULT_SIGNER_FINGERPRINT)
  if crypt:
    return str(crypt)
  else:
    raise EncryptionError("Problem Encrypting")

def decrypt(msg):
  crypt = gpg.decrypt(msg)
  if crypt:
    meta_lines = crypt.stderr.split('\n')
    meta_lines = [line for line in meta_lines if "[GNUPG:]" not in line]
    meta = '\n'.join(meta_lines)
    return "{}\n\n{}".format(str(crypt), meta)
  else:
    raise DecryptionError("Problem Decrypting")
