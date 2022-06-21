
import time
import util.common as common

class Project:
	def __init__(self, name: str, description: str):
		self.id = common.generate_uuid()
		self.name = name
		self.created_at = common.get_pretty_date(time.gmtime())
		self.description = description
		self.tasks = []
		self.tags = []

	@classmethod
	def from_dict(cls, d: dict):
		cls.id = d['id']
		cls.name = d['name']
		cls.created_at = d['created_at']
		cls.description = d['description']
		cls.tasks = d['tasks']
		cls.tags = d['tags']
		return cls
