# import time
# start_time = time.time()
#
# HEADER = '\033[95m'
# OKBLUE = '\033[94m'
# OKCYAN = '\033[96m'
# OKGREEN = '\033[92m'
# WARNING = '\033[93m'
# FAIL = '\033[91m'
# ENDC = '\033[0m'
# BOLD = '\033[1m'
# UNDERLINE = '\033[4m'
# print(HEADER + "header", OKBLUE + "okblue", OKCYAN + "okcyan", OKGREEN + "okgreen", WARNING + "warning", FAIL + "fail", ENDC + "endc", BOLD + "bold", UNDERLINE + "underline")
import red as red
from termcolor import colored

text = colored("Hello, World!", red, attrs=["reverse", "blink"])
print(text)

