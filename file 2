import datetime

users = []

def addUser(name, age):
    users.append({"name": name, "age": age, "joined": datetime.datetime.now()})
    return users

def getOldestUser():
    oldest = None
    for u in users:
        if oldest is None or u["age"] > oldest["age"]:
            oldest = u
    return oldest
