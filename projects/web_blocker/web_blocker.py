"""
Block websites during your worktime with this simple script.
Needs to have a valid hosts path updated and opened as sudo.
"""

import time
from datetime import datetime as dt

# Windows hosts path
# C:\Windows\System32\drivers\etc\hosts
# Update the path when setting up
hosts_temp = "hosts"
hosts_path = "/etc/hosts"

# Update the website list
website_list = [
        "www.facebook.com",
        "facebook.com",
        ]
redirect = "127.0.0.1"

# Update the script start and stop at the end of expression
start = dt(dt.now().year, dt.now().month, dt.now().day, 8)
stop = dt(dt.now().year, dt.now().month, dt.now().day, 21)

while True:
    if start < dt.now() < stop:
        print("Working hours...")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            # Set the cursor to the beginning of file with seek method
            # Iterate through and delete rest of file with truncate
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
            print("Fun hours...")
    time.sleep(5)
