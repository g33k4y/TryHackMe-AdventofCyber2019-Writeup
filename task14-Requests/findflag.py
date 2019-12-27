#!/usr/bin/env Python3
import requests

path = '/'
host = 'http://10.10.112.87:3000'
flag = ''

while (host is not ''):
	response = requests.get(host + path)
	json_response = response.json()
	if str(json_response['next']) != 'end':		#ends loop if response is 'end'
		path = '/' + json_response['next']
		flag += json_response['value']
	else:
		host = ''

print(f"Flag: {flag}")