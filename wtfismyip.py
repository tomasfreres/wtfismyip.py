#!/usr/bin/python


import json
import urllib
from urllib.request import urlopen, Request


def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode() == 200):
        data = operUrl.read()
    else:
        print("Error receiving data", operUrl.getcode())
    return data


ipv4 = getResponse('https://json.ipv4.wtfismyip.com')
ipv6 = getResponse('https://json.ipv6.wtfismyip.com')

ipv4json = json.loads(ipv4)
ipv6json = json.loads(ipv6)

print('Your fucking IPv4-Address is: ' + ipv4json['YourFuckingIPAddress'])
print('Your fucking IPv6-Address is: ' + ipv6json['YourFuckingIPAddress'])
print('Your fucking ISP is: ' + ipv6json['YourFuckingISP'])
print('Your fucking Countrycode is: ' + ipv6json['YourFuckingCountryCode'])
