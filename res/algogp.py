#Algorithm to encrypt global password
import random
import func
import json

def genSalt():
    diff = int(random.randrange(0, 10))
    opps = ["+", "-"]
    secure_random = random.SystemRandom()
    opp = secure_random.choice(opps)
    final = str(diff) + opp
    saltfile = open("res/salt.txt", "w+")
    saltfile.write(final)
    saltfile.close()
   
def readSalt():
    global difference
    global operator
    try:
        with open("res/salt.txt", "r", encoding='utf-8') as saltfile:
            contents = saltfile.read()
            operator = contents.strip()[-1]
            difference = int(contents[:-1])
            saltfile.close()
            return True
    except IOError as e:
        return False

def encrypt(content):
    ls = list(content)
    content = ""
    readSalt()
    if (operator == "+"):
        for i in range(0, len(ls)):
            content += chr(ord(ls[i]) + difference)
    elif (operator == "-"):
        for i in range(0, len(ls)):
            content += chr(ord(ls[i]) - difference)
    return content

def decrypt(content):
    ls = list(content)
    content = ""
    readSalt()
    if operator == "+":
        for i in range(0, len(ls)):
            content += chr(ord(ls[i]) - difference)
    elif operator == "-":
        for i in range(0, len(ls)):
            content += chr(ord(ls[i]) + difference)
    return content

def storeGlobal(pwd):
    saltfile = open("bin/gp.txt", "w+", encoding='utf-8')
    dict1 = {"p": pwd}
    contents = json.dumps(dict1)
    saltfile.write(encrypt(str(contents)))
    saltfile.close()

def checkPassword(pwd):
    try:
        with open("bin/gp.txt", "r", encoding='utf-8') as gpfile:
            contents = decrypt(gpfile.read())
            data = func.JSONtoDict(contents)
            if encrypt(pwd) == data["p"]:
                return True
            else:
                return False
    except IOError as e:
        return False
