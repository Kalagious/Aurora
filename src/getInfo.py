from jsonConvert import *



target = randomTarget()
user = getUserFromName(target, "Abbi")
if user:
	print(user.json())