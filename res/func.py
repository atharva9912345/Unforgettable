#functions
import os
import datetime
import json
import tkinter

def checkFileExists(path):
    if os.path.isfile(path):
        return True
    else:
        return False

def WriteFileInPath(content, path):
    try:
        with open(path, "a+") as f:
            func.write(content + "\n") 
            func.close()
            return True
    except IOError as e:
        Log(e, "WriteFileInPath")
        return False

def DeleteFilelnPath(path):
    if checkFileExists(path):
        os.remove(path)
        return True
    else:
        Log(path + " does not exist", "DeleteFileInPath")
        return False

def JSONtoDict(content):
    return json.loads(content)

def DICTtoJSON(content):
    return json.dumps(content)

def createDataFile():
    try:
        with open("bin/d.txt", "a+") as file:
            file.close()
            return True
    except IOError as e:
        Log(e, "createDataFile")
        return False
