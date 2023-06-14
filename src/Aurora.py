import json
from Classes import *
from Commands import*


def getUsersFromTarget(target):
	users = []

	for box in target.boxes:
		users.extend(box.localUsers)

	for domain in target.domains:
		users.extend(domain.domainUsers)

	return users




def getUserFromName(target, username):
	for user in getUsersFromTarget(target):
		if (user.name == username):
			return user

	return None
