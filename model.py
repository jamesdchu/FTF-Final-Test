def inDataBase(email, password, users):
    #users is database
    inDataBase = False
    for user in users: 
        if (email==user["email"] and password==user["password"]):
            inDataBase = True
    return inDataBase
