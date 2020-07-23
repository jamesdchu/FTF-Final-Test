def inDataBase(email, password, users):
    #users is database
    if (email in users) and (password == users['email']['password']):
        return True
    else:
        return False
