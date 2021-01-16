import time
from datetime import datetime as dt # datetime is a class inside the datetime module

# to modify hosts file, one needs to run the script as admin
# hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts" - the double \ is to avoid special character readings like \n
hosts_temp ="hosts" # temporary hosts file in current working directory for testing script. Change to hosts_path when script is finished.
hosts_path = "/etc/hosts"
redirect="127.0.0.1"
sites_to_block = ["www.facebook.com","facebook.com","gmail.com","mail.google.com","www.gmail.com"]

while True:
    # to only execute this if the time now is > 8.00hrs but < 16:00hrs. That is, from 8am to 4pm.
    if dt(dt.now().year,dt.now().month,dt.now().day, 8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 16): # year,month,day,timehour.
        print("working hours")
        with open(hosts_path, 'r+') as file: #r+ allows read/append
            content=file.read()
            for site in sites_to_block: # check each of the websites to block
                if site in content: # check if the site is in the opened hosts file
                    pass # if yes, then pass to the next line.
                else:
                    file.write(redirect +" "+site+"\n") # if the site is not in hosts, then write it to hosts, with space in between and new line
    else:
        print("Fun hours")
        with open(hosts_path, 'r+') as file:
            content=file.readlines() # readlines generates a list as strings of each line in the file
            file.seek(0) # takes the pointer/cursor from the end of the file (after reading file content) to the start of the file
            for line in content: # for each line in the file
                if not any(site in line for site in sites_to_block): # check all the lines of the hosts file where the sites_to_block are not present
                    file.write(line) # then write those line
            file.truncate() # delete everything else after the cursor from writing.
    time.sleep(5) # to save memory and run every 5 seconds.
