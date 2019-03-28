def save_user(**user):
    print(user["name"])
    print(user)


save_user(id=1, name="Sandeep", age=31)
# When we use ** we can pass multiple key value pairs or multiple keyword arguments to function Python will automaticaaly package them to dictionary
