
import json
import os.path
from util.logger import Logger

FILE_NAME = "globalvars.json"

def vars_write(field: str, value: any):
	globalvars = _load_json()
	globalvars[field] = value
	_write_json(globalvars)

def vars_read(field: str):
	globalvars = _load_json()

	if field not in globalvars.keys():
		Logger.error("Invalid or unexisted varname")
		return None

	return globalvars[field]

def _load_json():

    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'a') as jsonfile:
            jsonfile.write("{}")
        return {}

    with open(FILE_NAME, 'r') as jsonfile:
        return json.load(jsonfile)

def _write_json(json_obj):
    with open(FILE_NAME, 'w') as jsonfile:
        jsonfile.write(json.dumps(json_obj))