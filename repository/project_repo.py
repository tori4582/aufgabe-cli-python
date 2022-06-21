
import modal.Project as Project
from repository.mongodb import aufgabe_database

collection = aufgabe_database.get_collection('project')

def add(project: Project):
    return collection.insert_one(project.__dict__)

def remove(project_id: str):
    return collection.delete_one({'id' : project_id})

def get(project_id: str):
	return collection.find_one({'id' : project_id})

def update(project_id: str, update_data: dict):
    return collection.update_one({'id' : project_id}, update_data)

def getall():
    return collection.find({})