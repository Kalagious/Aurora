import json
import sys
import os
from jsonConvert import *

sys.path.append('..')
import Aurora




os.environ['AURORA'] = '/home/kali/Aurora'
Aurora.loadConfig(False)
# Aurora.target = randomTarget()
# Aurora.target.name = "test"

# Aurora.saveTarget()

Aurora.loadTarget('testsdf')
items = Aurora.getByClass("Box")
for item in items:
	print(item.json())