#(C) artemis#1551
#MIT License
from urllib import request
import json
import os
import time
from time import sleep
 
print("IP-Lookup - V.1")
print("Github : github.com/artemis1551")

from urllib import request
import json
import os

while True:
    lol = input("IP > ")
    print('Tracking for ',lol, ', Please wait...')
    sleep(5)
    url = "http://ip-api.com/json/"
    r = request.urlopen(url + lol)
    data = r.read()
    m = json.loads(data)

    print(f"""
    Status : {m['status']}
    IP : {m['query']}
    ISP : {m['isp']}
    Organization : {m['org']}
    Country : {m['country']}
    Region : {m['region']}
    City : {m['city']}
    Time Zone : {m['timezone']}
    """)
    
    break