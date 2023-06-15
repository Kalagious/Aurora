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

		case "Exploit":
			if parent.object in ["Vector"]:
				if item.name not in getNamesFromArray(parent.exploits):
					parent.exploits.append(item)
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



