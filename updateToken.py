import getToken

def update():
    file = open(“token.txt”, ”w”)

    file.write(getToken.get())
    file.close()