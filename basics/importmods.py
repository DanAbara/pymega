import time as t # import a builtin module 'time' which is found in 'sys' builtin module
# other builtin modules are found by sys.builtin_module_names
# 'os' is also a builtin module found in the python3.5 installation directory

import os # import the os module
from os import path

while True:
    if path.exists("files/veggies.txt"):
        with open("files/veggies.txt") as file:
            print(file.read())
    else:
        print("File does not exist")
    t.sleep(10) # print content (file.read()) every 10 seconds

# open() loads data as a string so we cannot manipulate int types directly from files
