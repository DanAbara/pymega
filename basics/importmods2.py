import time as t
import os
import pandas as pd # load pandas package. Several modules are called packages

while True:
    if os.path.exists("files/temps_today.csv"):
        data = pd.read_csv("files/temps_today.csv")
        print(data.mean())
    else:
        print("File does note exist.")
    t.sleep(5)
