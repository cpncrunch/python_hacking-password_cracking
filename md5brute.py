#!/usr/bin/python
#-*- coding:utf-8 -*-
#Author: Isaac Privett
#Date: 05-02-2022
#Description: Python program that will brute force salted encrypted passwords

import crypt
from termcolor import colored

def crackPass(cryptword):
	salt = cryptword[0:2]
	dictionary = open('passwords.txt', 'r', encoding='ISO-8859-1')
	for word in dictionary.readlines():
		word = word.strip('\n')
		cryptPass = crypt.crypt(word, salt)
		if (cryptword == cryptPass):
			print(colored("[+] Password found: " + word, 'green'))
			return
		else:
			print(colored("[-] Password not found!", 'red'))
			return

def main():
	passfile = open('credentials.txt', 'r', encoding='ISO-8859-1')
	for line in passfile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptword = line.split(':')[1].strip('\n')
			print(colored("[*] Cracking password for: " + user, 'blue'))
			crackPass(cryptword)
	
main()
