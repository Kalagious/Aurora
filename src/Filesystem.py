import json
import os
import Aurora


def loadArray(array):
	items = []

	if len(array) == 0:
		return items

	itemType = array[0]["class"]

	match itemType:
		case "Box":
			for item in array:
				tmp = Aurora.Box()
				tmp.name = item["name"]
				tmp.hostnames = item["hostnames"]
				tmp.ips = item["ips"]
				tmp.enumeration = loadArray(item["enumeration"])
				tmp.services = loadArray(item["services"])
				tmp.users = loadArray(item["users"])
				tmp.vectors = loadArray(item["vectors"])
				tmp.owned = item["owned"]
				tmp.notes = loadArray(item["notes"])
				tmp.object = "Box"
				items.append(tmp)

		case "Enumeration":
			for item in array:
				tmp = Aurora.Enumeration()
				tmp.name = item["name"]
				tmp.type = item["type"]
				tmp.tools = item["tools"]
				tmp.pServices = item["pServices"]
				tmp.data = item["data"]
				tmp.notes = loadArray(item["notes"])
				tmp.object = "Enumeration"
				items.append(tmp)


		case "Service":
			for item in array:
				tmp = Aurora.Service()
				tmp.name = item["name"]
				tmp.ports = item["ports"]
				tmp.enumeration = loadArray(item["enumeration"])
				tmp.credentials = loadArray(item["credentials"])
				tmp.pUser = item["pUser"]
				tmp.vectors = loadArray(item["vectors"])
				tmp.pBox = item["pBox"]
				tmp.owned = item["owned"]
				tmp.notes = loadArray(item["notes"])
				tmp.object = "Service"
				items.append(tmp)

		case "User":
			for item in array:
				tmp = Aurora.User()
				tmp.name = item["name"]
				tmp.credentials = loadArray(item["credentials"])
				tmp.enumeration = loadArray(item["enumeration"])
				tmp.pServices = item["pServices"]
				tmp.pBoxes = item["pBoxes"]
				tmp.pDomain = item["pDomain"]
				tmp.vectors = loadArray(item["vectors"])
				tmp.access = item["access"]
				tmp.owned = item["owned"]
				tmp.notes = loadArray(item["notes"])
				tmp.object = "User"
				items.append(tmp)

		case "Vector":
			for item in array:
				tmp = Aurora.Vector()
				tmp.name = item["name"]
				tmp.attacks = loadArray(item["attacks"])
				tmp.priority = item["priority"]
				tmp.pServices = item["pServices"]
				tmp.notes = loadArray(item["notes"])
				tmp.object = "Vector"
				items.append(tmp)


		case "Credential":
			for item in array:
				tmp = Aurora.Credential()
				tmp.name = item["name"]
				tmp.username = item["username"]
				tmp.pServices = item["pServices"]
				tmp.pUsers = item["pUsers"]
				tmp.password = item["password"]
				tmp.hash = item["hash"]
				tmp.salt = item["salt"]
				tmp.notes = loadArray(item["notes"])
				tmp.object = "Credential"
				items.append(tmp)


		case "Attack":
			for item in array:
				tmp = Aurora.Attack()
				tmp.name = item["name"]
				tmp.pVector = item["pVector"]
				tmp.pServices = item["pServices"]
				tmp.type = item["type"]
				tmp.tool = item["tool"]
				tmp.cmd = item["cmd"]
				tmp.notes = loadArray(item["notes"])
				tmp.object = "Attack"
				items.append(tmp)


		case "Note":
			for item in array:
				tmp = Aurora.Note()
				tmp.name = item["name"]
				tmp.type = item["type"]
				tmp.data = item["data"]
				tmp.object = "Note"
				items.append(tmp)


		case "Domain":
			for item in array:
				tmp = Aurora.Domain()
				tmp.name = item["name"]
				tmp.pBoxes = item["pBoxes"]
				tmp.users = loadArray(item["users"])
				tmp.enumeration = loadArray(item["enumeration"])
				tmp.vectors = loadArray(item["vectors"])
				tmp.owned = item["owned"]
				tmp.notes = loadArray(item["notes"])
				tmp.object = item["object"]
				tmp.object = "Domain"
				items.append(tmp)


		case "DNS":
			for item in array:
				tmp = Aurora.Domain()
				tmp.name = item["name"]
				tmp.entries = item["entries"]
				tmp.ip = item["ip"]
				tmp.object = "DNS"
				items.append(tmp)

	return items;

def loadConfig(logging=True):
	if not os.getenv("AURORA"):
		print(" [!] Aurora environment variable not set!")
		return None
	configRaw = open(os.path.join(os.getenv("AURORA"),"config.json"),'r').read()
	configjson = json.loads(configRaw)
	Aurora.config.auroraPath = configjson['auroraPath']
	Aurora.config.targetsPath = configjson['targetsPath']
	if logging:
		print(" [*] Aurora config loaded!")



def saveConfig(logging=True):
	if not Aurora.config.auroraPath:
		Aurora.config.auroraPath = os.getenv("AURORA")
	configRaw = json.dumps(config.__dict__)
	open(os.path.join(config.auroraPath,"config.json"), 'w').write(configRaw)
	if logging:
		print(" [*] Aurora config saved!")



def loadTarget(targetPath):
	if "/" not in targetPath or "\\" not in targetPath:
		if targetPath not in Aurora.getTargets():
			return False
		targetPath = os.path.join(Aurora.config.targetsPath, targetPath, targetPath+".json")

	
	Aurora.target = Aurora.Target()
	targetRaw = open(targetPath, 'r').read()
	targetJson = json.loads(targetRaw)
	Aurora.target.name = targetJson["name"]
	Aurora.target.domains = loadArray(targetJson["domains"])
	Aurora.target.boxes = loadArray(targetJson["boxes"])
	Aurora.target.dns = loadArray(targetJson["dns"])
	Aurora.target.owned = targetJson["owned"]
	Aurora.target.notes = loadArray(targetJson["notes"])
	Aurora.target.object = "Target"


def saveTarget():
	if not Aurora.target or not Aurora.target.name:
		print(" [!] There is no active target to save!")
		return
	targetFile = open(os.path.join(Aurora.config.targetsPath, Aurora.target.name, Aurora.target.name+".json"), 'w')
	targetFile.write(Aurora.target.json())
	print(" [*] {} has been saved.".format(Aurora.target.name))
