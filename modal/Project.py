
import time
import util.common as common

class Project:
	def __init__(self, name, description = ''):
		self.id = common.generate_uuid()
		self.name = name
		self.created_at = common.get_pretty_date(time.gmtime())
		self.description = description
