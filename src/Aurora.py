import json
from Classes import *
target = Target()

from Filesystem import *
import os


def addMatchingArrays(array1, array2, names):
	if len(array1):
		if array1[0].object in names or "All" in names:
			array2.extend(array1)


def getTargets():
	targets = {}
	for root, directories, contents in os.walk(config.targetsPath, topdown=False):
		for item in contents:
			if ".json" in item:
				targets[item.replace(".json","")] = (os.path.join(root, item)) 
	return targets


def getByClass(names):
	items = []	
	addMatchingArrays(target.boxes, items, names)

	users = []
	services = []
	attacks = []
	credentials = []
	vectors = []
	enumeration = []	
	notes = []
	notes.extend(target.notes)

	for box in target.boxes:
		users.extend(box.users)
		notes.extend(box.notes)
		services.extend(box.services)
		vectors.extend(box.vectors)
		enumeration.extend(box.enumeration)
		notes.extend(box.notes)


	for domain in target.domains:
		users.extend(domain.users)
		notes.extend(domain.notes)
		vectors.extend(domain.vectors)
		enumeration.extend(domain.enumeration)
		notes.extend(domain.notes)


	for service in services:
		vectors.extend(service.vectors)
		credentials.extend(service.credentials)
		enumeration.extend(service.enumeration)
		notes.extend(service.notes)


	for user in users:
		vectors.extend(user.vectors)
		credentials.extend(user.credentials)
		enumeration.extend(user.enumeration)
		notes.extend(user.notes)


	for vector in vectors:
		attacks.extend(vector.attacks)
		notes.extend(vector.notes)


	addMatchingArrays(users, items, names)
	addMatchingArrays(services, items, names)
	addMatchingArrays(target.domains, items, names)
	addMatchingArrays(attacks, items, names)
	addMatchingArrays(credentials, items, names)
	addMatchingArrays(vectors, items, names)
	addMatchingArrays(enumeration, items, names)
	addMatchingArrays(notes, items, names)

	return items


def getByNames(names):
	allItems = getByClass("All")
	items = []
	for item in allItems:
		#print(item.json())
		if item.name in names:
			items.append(item)
				
	return items



def getUsersFromTarget(itarget):
	users = []

	for box in itarget.boxes:
		users.extend(box.users)

	for domain in itarget.domains:
		users.extend(domain.users)

	return users


def getNamesFromArray(array):
	names = []
	for item in array:
		names.append(item.name)
		return names

def getUserFromName(target, username):
	for user in getUsersFromTarget(target):
		if (user.name == username):
			return user

	return None



def assign(item, parent, logging = True):
	output = ""
	match item.object:
		case "Box":
			if parent.object  == "Domain":
				if item.name not in parent.pBoxes:
					parent.pBoxes.append(item.name)
					output = "Success"
			elif parent.object == "Target":
				if item.name not in getNamesFromArray(parent.boxes):
					parent.boxes.append(item)
					output = "Success"
			else:
				output = "Type Error"


		case "Domain":
			if parent.object == "Target":
				if item.name not in getNamesFromArray(parent.domains):
					parent.domains.append(item)
					output = "Success"
			else:
				output = "Type Error"


		case "Service":
			if parent.object  == "Box":
				if item.name not in getNamesFromArray(parent.services):
					parent.boxes.append(item)
					output = "Success"
			elif parent.object in ["User"]:
				if item.name not in parent.pServices:
					parent.pServices.append(item)
					output = "Success"
			else:
				output = "Type Error"


		case "User":
			if parent.object in ["Box","Domain"]:
				if item.name not in getNamesFromArray(parent.users):
					parent.users.append(item)
					output = "Success"
			else:
				output = "Type Error"


		case "Credential":
			if parent.object in ["Service","User"]:
				if item.name not in getNamesFromArray(parent.credentials):
					parent.credentials.append(item)
					output = "Success"
			else:
				output = "Type Error"


		case "Enumeration":
			if parent.object in ["Service","Box", "Domain", "User"]:
				if item.name not in getNamesFromArray(parent.enumeration):
					parent.enumeration.append(item)
					output = "Success"
			else:
				output = "Type Error"

		case "attack":
			if parent.object in ["Vector"]:
				if item.name not in getNamesFromArray(parent.attacks):
					parent.attacks.append(item)
					output = "Success"
			else:
				output = "Type Error"


		case "Vector":
			if parent.object in ["Service","Box", "Domain"]:
				if item.name not in getNamesFromArray(parent.vectors):
					parent.vectors.append(item)
					output = "Success"
			else:
				output = "Type Error"



		case "Note":
			if item.name not in getNamesFromArray(parent.notes):
					parent.notes.append(item)
					output = "Success"

		case _:
			output = "Assignment Error"


	match output:
		case "Success":
			output = " [*] {} was assigned to {}!\n".format(item.name, parent.name)
		case "Type Error":
			output = " [!] {} can not be assigned to a {}!\n".format(item.object, parent.object)
		case "Assignment Error":
			output = " [!] {} can not be assigned.\n".format(item.object)
		case "":
			output = " [!] {} has already been assigned to {}.\n".format(item.name, parent.name)

	if (logging):
		print(output)
	return output



