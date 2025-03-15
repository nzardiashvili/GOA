def addtodatabase(first_name, last_name, age):
    database = {}
    database["first_name"] = first_name
    database["Last_name"] = last_name
    database["age"] = age
    return database
person_info = addtodatabase("nino", "Zardiashvili", "14")