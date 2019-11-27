#data read write
import func
import algogp
import algoac

data_path = "bin/d.txt"

def countAccounts():
    try:
        with open(data_path, "r", encoding='utf-8') as datafile:
            contents = datafile.read()
            if contents == "":
                datafile.close()
                return 0
            else:
                contents = func.JSONtoDict(algogp.decrypt(contents))
                count=len(contents)
                datafile.close()
                return count
    except IOError as e:
        return -1


def readData():
    try:
        with open(data_path, "r", encoding='utf-8') as datafile:
            contents = datafile.read()
            if contents != "":
                contents = func.JSONtoDict(algogp.decrypt(contents))
            datafile.close()
            return contents

    except IOError as e:
        return "error"

def writeData(contents):
    try:
        with open(data_path, "w+", encoding='utf-8') as file:
            file.write(algogp.encrypt(str(contents)))
            file.close()
            return True

    except IOError as e:
       return False

def addEntry(name,uname,pwd):
    accounts = readData()
    pwd = algoac.encrypt(pwd)
    entry = {"n":name,"u":uname,"p":pwd}
    if accounts == "error":
        return False
    else:
        if accounts == "":
            writeData(func.DICTtoJSON({countAccounts() + 1: entry}))
        else:
            accounts.update({str(countAccounts() + 1): entry})
            writeData(func.DICTtoJSON(accounts))
        return True


def deleteAccount(id):
    accounts = readData()
    if accounts == "error":
        return False
    else:
        if accounts == "":
            return False
        else:
            accounts.pop(id,None)
            writeData(func.DICTtoJSON(accounts))
        return True
