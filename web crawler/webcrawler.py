#!/usr/bin/env python

import sys

import requests
print(sys.version)


def request(url):
	try:
		return requests.get("http://"+url)
	except requests.exceptions.ConnectionError:
		pass

target_url="google.com"

with open("/home/kilgrave/Documents/python3/Web Crawler/subdomain.txt","r") as worldlist_file : 
	for line in worldlist_file:
		word =line.strip()
		test_url=target_url + "/" +word
		response=request(test_url)
		if response:
			print("[+] Discoverd URL -->"+test_url)