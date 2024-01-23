import logging
print(logging.__file__)
logging.basicConfig(filename='C:\\Users\\NithinRajkumar\\Desktop\\skill_captain_python_advanced\\Day7\\test.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='w')

input_log = str(input("Please enter the desired logging level"))
input_msg = str(input("Please enter the message you wish to display"))

valid_levels = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}

if input_log not in valid_levels:
  print("Invalid logging level name. Please try again.")
  exit()

level = valid_levels[input_log]
logging.log(level, input_msg)
