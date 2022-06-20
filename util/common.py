
import uuid
import time

def generate_uuid():
    return str(uuid.uuid4().hex)[0:6]

def get_pretty_date(datetime):
    return time.strftime("%x %X", datetime)