from pprint import pprint

def multiline_input():
  s = ""
  try:
    while True:
      s += "\n" + raw_input()
  except EOFError:
    return s + "\n"

pprint(multiline_input())
