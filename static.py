i = 1

def getint():
    f = open('num.txt', 'r')
    return int(f.read())

def ink(i):
    f = open('num.txt', 'w')
    f.write(str(i))

def savekey(key,addr,balance):
    f = open('KEY_SAVE{}.txt'.format(i), 'w')
    f.write("PRIVATE KEY:       {}\n"
            "ADDRESS:           {}\n"
            "BALANCE:           {}".format(key,addr,balance))

def errors(key,addr):
    f = open('errors.txt', 'a')
    f.write("PRIVATE KEY:       {}\n"
            "ADDRESS:           {}\n\n\n".format(key,addr))