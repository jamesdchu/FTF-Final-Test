def inDataBase(user, password):
    #users is database
    if (user in users) and (password == users['user']['password']):
        return True
    else:
        return False
