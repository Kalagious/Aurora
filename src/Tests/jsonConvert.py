import json
import sys
import random
sys.path.append('..')
from Aurora import *

usernames = open("usernames.txt", 'r').read().split('\n')
computernames = open("computernames.txt", 'r').read().split('\n')


def randomfromlist(list):
	return list[random.randrange(len(list))]



def randomUser():
	user = User()
	user.name = randomfromlist(usernames)
	user.addCredential(randomCredential())
	return user


def randomCredential():
	cred = Credential()
	cred.name = "test cred"
	cred.password = "goodpassword123"
	return cred



def randomBox():
	box = Box()
	box.name = randomfromlist(computernames)
	box.ips = ["192.168.1."+str(random.randrange(255))]
	box.notes = ["box note 1", "box note 2"]
	for i in range(1, 2):
		box.addUser(randomUser())
	return box


def randomTarget():
	target = Target()
	for i in range(1, 5):
		target.boxes.append(randomBox())

	return target


target = randomTarget()
assign(randomBox(), target)
target.boxes.append(randomBox())
print(target.json())
