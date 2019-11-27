#Algorithm to encrypt account passwords
import random
import func

def encrypt(pwd):
    pwdls=list(pwd)
    pwd = ""
    al = ""
    l = ""
    for i in range(0,len(pwdls)):
        diff=int(random.randrange(0,10))
        pwd+=str(ord(pwdls[i])+diff)
        al+=str(diff)
        l+=str(len(str(ord(pwdls[i])+diff)))
    return pwd+"x"+al+"x"+l

def decrypt(pwd):
    code=pwd.split("x")
    a = 0 
    b = 0 
    c = list(code[2]) 
    d = list(code[1]) 
    pwd_chars=[]
    for i in c:
        letter=code[0][a:a+int(c[b])]
        pwd_chars.append(letter)
        a=a+int(c[b])
        b += 1
    pwd=""
    for i in range(0,len(pwd_chars)):
        pwd+=chr(int(pwd_chars[i])-int(d[i]))

    return pwd
