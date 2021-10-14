import logging
import sys
# import string_utils from 'shared' module
from shared import string_utils
# import 'example.py' script
import example

# configure logging level
logging.basicConfig(level=logging.INFO)

# method that processes a string and returns a new one
def process_my_string(input: str) -> str:
  result = string_utils.clean_string(input)
  example.example_function()
  return result

# application execution starts here
if __name__ == "__main__":
  logging.debug("Arguments received:")
  logging.debug(sys.argv)

  if sys.argv.__len__() <= 1:
    raise Exception("Argument missing")

  string_to_process = sys.argv[1]
  logging.info("Result: " + process_my_string(string_to_process))