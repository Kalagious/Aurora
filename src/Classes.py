import json


# Takes an array of python objects and converts them to a json string array
def array2json(array):
	tmp = []
	for item in array:
		tmp.append(cleanjson(item.json()))
	
	return tmp


def cleanjson(data):
	return data.replace('\\"', '"').replace("\\\\n",'\n').replace("\"{", '{').replace("}\"", '}')



class Target:
	def __init__(self):
		self.name = ""
		self.domains = []
		self.boxes = []
		self.owned = False
		self.notes = []

	def json(self):
		tmp = {
			"name" : self.name,
			"domains" : array2json(self.domains),
			"boxes" : array2json(self.boxes),
			"owned" : self.owned,
			"notes" : self.notes,
			"class" : "Target"
		}
		return cleanjson(json.dumps(tmp))




class Box:
	def __init__(self):
		self.name = ""
		self.hostnames = []
		self.ips = []
		self.services = []
		self.localUsers = []
		self.generalVectors = []
		self.owned = False
		self.notes = []

	def addUser(self, user):
		self.localUsers.append(user)
		user.pBoxes.append(self.name)
		return user

	def newUser(self):
		newUser = User()
		self.localUsers.append(newUser)
		newUser.pBoxes.append(self.name)
		return newUser

	def json(self):
		tmp = {
			"name" : self.name,
			"hostnames" : self.hostnames,
			"ips" : self.ips,
			"services" : array2json(self.services),
			"localUsers" : array2json(self.localUsers),
			"generalVectors" : array2json(self.generalVectors),
			"notes" : self.notes,
			"class" : "Box"
		}
		return cleanjson(json.dumps(tmp))



class Domain:
	def __init__(self):
		self.name = ""
		self.pBoxes = []
		self.domainUsers = []
		self.owned = False
		self.notes = []

	def json(self):
		tmp = {
			"name" : self.name,
			"pBoxes" : self.pBoxes,
			"domainUsers" : self.domainUsers,
			"owned" : self.owned,
			"notes" : self.notes,
			"class" : "Domain"
		}
		return cleanjson(json.dumps(tmp))



class Service:
	def __init__(self):
		self.name = []
		self.ports = []
		self.credentials = []
		self.pUsers = []
		self.pOwner = ""
		self.vectors = []
		self.pBox = ""
		self.owned = False
		self.notes = []

	def json(self):
		tmp = {
			"name" : self.name,
			"ports" : self.ports,
			"credentials" : array2json(self.credentials),
			"pUsers" : self.pUsers,
			"pOwner" : self.pOwner,
			"pBox" : self.pBox,
			"owned" : self.owned,
			"notes" : self.notes,
			"class" : "Service"
		}
		return cleanjson(json.dumps(tmp))



class Credential:
	def __init__(self):
		self.name = ""
		self.pServices = []
		self.pUsers = []
		self.password = ""
		self.hash = ""
		self.salt = ""
		self.notes = []

	def json(self):
		tmp = {
			"name" : self.name,
			"pServices" : self.pServices,
			"pUsers" : self.pUsers,
			"password" : self.password,
			"hash" : self.hash,
			"salt" : self.salt,
			"notes" : self.notes,
			"class" : "Credential"
		}
		return cleanjson(json.dumps(tmp))


class User:
	def __init__(self):
		self.name = ""
		self.credentials = []
		self.pServices = []
		self.pBoxes = []
		self.pDomain = ""
		self.vectors = []
		self.access = []
		self.owned = False
		self.notes = []

	def addCredential(self, cred):
		self.credentials.append(cred)
		cred.pUsers.append(self.name)
		return cred

	def newCredential(self):
		newCred = Credential()
		self.credentials.append(newCred)
		newCred.pUsers.append(self.name)
		return newCred

	def json(self):
		tmp = {
			"name" : self.name,
			"credentials" : array2json(self.credentials),
			"pServices" : array2json(self.pServices),
			"pBoxes" : self.pBoxes,
			"pDomain" : self.pDomain,
			"vectors" : array2json(self.vectors),
			"access" : self.access,
			"owned" : self.owned,
			"notes" : self.notes,
			"class" : "User"
		}
		return cleanjson(json.dumps(tmp))


class Vector:
	def __init__(self):
		self.name = ""
		self.enumeration = []
		self.exploits = []
		self.priority = 1000;
		self.notes = []

	def json(self):
		tmp = {
			"name" : self.name,
			"enumeration" : array2json(self.enumeration),
			"exploits" : array2json(self.exploits),
			"priority" : self.priority,
			"notes" : self.notes,
			"class" : "Vector"
		}
		return cleanjson(json.dumps(tmp))



class Enumeration:
	def __init__(self):
		self.name = ""
		self.type = []
		self.tools = []
		self.data = ""
		self.pVector = ""
		self.notes = []


	def json(self):
		tmp = {
			"name" : self.name,
			"type" : self.type,
			"tool" : self.tools,
			"data" : self.data,
			"pVector" : self.pVector,
			"notes" : self.notes,
			"class" : "Enumeration"
		}
		return cleanjson(json.dumps(tmp))




class Exploit:
	name = []
	pVector = ""
	type = []
	tool = []
	cmd = ""
	notes = []


	def json(self):
		tmp = {
			"name" : self.name,
			"pVector" : self.pVector,
			"type" : self.type,
			"tool" : self.tool,
			"cmd" : self.cmd,
			"notes" : self.notes,
			"class" : "Exploit"
		}
		return cleanjson(json.dumps(tmp))

