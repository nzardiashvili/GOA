while True:
    name = input("enter your name: ")
    email = input("enter your email: ")
    password = input("enter your password: ")
    if len( name) > 0 and '@' in email and len(password) >= 6:
        print("registriraishen succsesful!")
        break
    else:
        print("please provide valid detals.")