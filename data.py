myFile = open('data.txt', 'r')
lines = myFile.readlines()


def get(operation):
    if operation == 'fbToken':
        return lines[0][:-1]
    elif operation == 'fbUser':
        return lines[1][:-1]
    elif operation == 'fbPass':
        return lines[2][:-1]
    elif operation == 'fbID':
        return lines[3][:-1]
    elif operation == 'telegramToken':
        return lines[4][:-1]
    elif operation == 'telegramChatID':
        return lines[5][:-1]
    else:
        return -1
    file.close()