import json
import sys
import random
import os
sys.path.append('..')
import Aurora

usernames = open("usernames.txt", 'r').read().split('\n')
computernames = open("computernames.txt", 'r').read().split('\n')


def randomfromlist(list):
	return list[random.randrange(len(list))]



def randomUser():
	user = Aurora.User()
	user.name = randomfromlist(usernames)
	user.addCredential(randomCredential())
	return user


def randomCredential():
	cred = Aurora.Credential()
	cred.name = "test cred"
	cred.password = "goodpassword123"
	return cred

def randomNote():
	note = Aurora.Note()
	note.name = "TestNote"
	note.data = "TestData"
	return note

def randomService():
	service = Aurora.Service()
	service.name = "Test Service"
	service.notes.append(randomNote())
	service.credentials.append(randomCredential())
	return service


def randomBox():
	box = Aurora.Box()
	box.name = randomfromlist(computernames)
	box.ips = ["192.168.1."+str(random.randrange(255))]
	for i in range(1, 2):
		box.services.append(randomService())
	for i in range(1, 2):
		box.addUser(randomUser())
	return box


def randomTarget():
	tmpTarget = Aurora.Target()
	for i in range(1, 5):
		tmpTarget.boxes.append(randomBox())

	return tmpTarget


# target = randomTarget()
# Aurora.assign(randomBox(), target)
# target.boxes.append(randomBox())
# print(target.json())

