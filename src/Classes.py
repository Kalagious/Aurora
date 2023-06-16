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
		self.dns = []
		self.owned = False
		self.notes = []
		self.object = "Target"


	def json(self):
		tmp = {
			"name" : self.name,
			"domains" : array2json(self.domains),
			"boxes" : array2json(self.boxes),
			"dns" : self.dns,
			"owned" : self.owned,
			"notes" : array2json(self.notes),
			"class" : "Target"
		}
		return cleanjson(json.dumps(tmp))




class Box:
	def __init__(self):
		self.name = ""
		self.hostnames = []
		self.ips = []
		self.enumeration = []
		self.services = []
		self.users = []
		self.vectors = []
		self.owned = False
		self.notes = []
		self.object = "Box"

	def addUser(self, user):
		self.users.append(user)
		user.pBoxes.append(self.name)
		return user

	def newUser(self):
		newUser = User()
		self.users.append(newUser)
		newUser.pBoxes.append(self.name)
		return newUser

	def json(self):
		tmp = {
			"name" : self.name,
			"hostnames" : self.hostnames,
			"ips" : self.ips,
			"enumeration" : array2json(self.enumeration),
			"services" : array2json(self.services),
			"users" : array2json(self.users),
			"vectors" : array2json(self.vectors),
			"owned" : self.owned,
			"notes" : array2json(self.notes),
			"class" : "Box"
		}
		return cleanjson(json.dumps(tmp))



class Domain:
	def __init__(self):
		self.name = ""
		self.pBoxes = []
		self.users = []
		self.enumeration = []
		self.vectors = []
		self.owned = False
		self.notes = []
		self.object = "Domain"


	def json(self):
		tmp = {
			"name" : self.name,
			"pBoxes" : self.pBoxes,
			"users" : array2json(self.users),
			"enumeration" : array2json(self.enumeration),
			"vectors" : array2json(self.vectors),
			"owned" : self.owned,
			"notes" : array2json(self.notes),
			"class" : "Domain"
		}
		return cleanjson(json.dumps(tmp))



class Service:
	def __init__(self):
		self.name = []
		self.ports = []
		self.enumeration = []
		self.credentials = []
		self.pUser = []
		self.vectors = []
		self.pBox = ""
		self.owned = False
		self.notes = []
		self.object = "Service"


	def json(self):
		tmp = {
			"name" : self.name,
			"ports" : self.ports,
			"enumeration" : array2json(self.enumeration),
			"credentials" : array2json(self.credentials),
			"pUser" : self.pUser,
			"vectors" : array2json(self.vectors),
			"pBox" : self.pBox,
			"owned" : self.owned,
			"notes" : array2json(self.notes),
			"class" : "Service"
		}
		return cleanjson(json.dumps(tmp))






class User:
	def __init__(self):
		self.name = ""
		self.credentials = []
		self.enumeration = []
		self.pServices = []
		self.pBoxes = []
		self.pDomain = ""
		self.vectors = []
		self.access = []
		self.owned = False
		self.notes = []
		self.object = "User"

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
			"enumeration" : array2json(self.enumeration),
			"pServices" : self.pServices,
			"pBoxes" : self.pBoxes,
			"pDomain" : self.pDomain,
			"vectors" : array2json(self.vectors),
			"access" : self.access,
			"owned" : self.owned,
			"notes" : array2json(self.notes),
			"class" : "User"
		}
		return cleanjson(json.dumps(tmp))


class Credential:
	def __init__(self):
		self.name = ""
		self.username = ""
		self.pServices = []
		self.pUsers = []
		self.password = ""
		self.hash = ""
		self.salt = ""
		self.notes = []
		self.object = "Credential"


	def json(self):
		tmp = {
			"name" : self.name,
			"username" : self.username,
			"pServices" : self.pServices,
			"pUsers" : self.pUsers,
			"password" : self.password,
			"hash" : self.hash,
			"salt" : self.salt,
			"notes" : array2json(self.notes),
			"class" : "Credential"
		}
		return cleanjson(json.dumps(tmp))



class Vector:
	def __init__(self):
		self.name = ""
		self.attacks = []
		self.priority = 1000;
		self.pServices = []
		self.notes = []
		self.object = "Vector"

	def json(self):
		tmp = {
			"name" : self.name,
			"attacks" : array2json(self.attacks),
			"priority" : self.priority,
			"pServices" : self.pServices,
			"notes" : array2json(self.notes),
			"class" : "Vector"
		}
		return cleanjson(json.dumps(tmp))



class Enumeration:
	def __init__(self):
		self.name = ""
		self.type = []
		self.tools = []
		self.pServices = []
		self.data = ""
		self.notes = []
		self.object = "Enumeration"


	def json(self):
		tmp = {
			"name" : self.name,
			"type" : self.type,
			"tool" : self.tools,
			"pServices" : self.pServices,
			"data" : self.data,
			"notes" : array2json(self.notes),
			"class" : "Enumeration"
		}
		return cleanjson(json.dumps(tmp))




class Attack:
	def __init__(self):
		self.name = []
		self.pVector = ""
		self.pServices = []
		self.type = []
		self.tool = []
		self.cmd = ""
		self.notes = []
		self.object = "Attack"


	def json(self):
		tmp = {
			"name" : self.name,
			"pVector" : self.pVector,
			"pServices" : self.pServices,
			"type" : self.type,
			"tool" : self.tool,
			"cmd" : self.cmd,
			"notes" : array2json(self.notes),
			"class" : "Attack"
		}
		return cleanjson(json.dumps(tmp))

class Pointer:
	def __init__(self, inPointer, inObject):
		self.pointer = inPointer
		self.object = inObject
	def json(self):
		tmp = {
			"pointer" : self.pointer,
			"class" : self.object,
		}
		return cleanjson(json.dumps(tmp))

class DNS:
	def __init__(self):
		self.name = []
		self.entries = []
		self.ip = ""
		self.object = "DNS"


	def json(self):
		tmp = {
			"name" : self.name,
			"entries" : self.entries,
			"ip" : self.ip,
			"class" : "DNS"
		}
		return cleanjson(json.dumps(tmp))



class Note:
	def __init__(self):
		self.name = ""
		self.type = ""
		self.data = []
		self.object = "Note"


	def json(self):
		tmp = {
			"name" : self.name,
			"type" : self.type,
			"data" : self.data,
			"class" : "Note"
		}
		return cleanjson(json.dumps(tmp))


class Config:
	def __init__(self):
		self.auroraPath = ""
		self.targetsPath = ""

config = Config()