import random,math

def zhi2(Min,Max):
    if Min > Max or Min < 2:
        print("发生错误！")
        return
    while True:
        a = random.randint(Min,Max)
        for i in range(2,int(math.sqrt(a))+1):
            if a % i == 0:
                return 1
        return a

def zhi(Min,Max):
    while True:
        a = zhi2(Min,Max)
        if a != 1:
            return a

def huzhi(Min,Max):
    for i in range(2,int(math.sqrt(Min))+1):
        if Min%i == 0 and Max%i == 0:
            return 1
    return Min

def rsa_key(Min,Max):
    p = zhi(Min,Max)
    q = zhi(Min,Max)
    n = p*q
    while True:
        e = random.randint(2,(p-1)*(q-1)-1)
        if (p-1)*(q-1) % e == 0:
            continue
        e = huzhi(e,(p-1)*(q-1))
        if e != 1:
            break
    for d in range(1,10**100):
        if e*d % ((p-1)*(q-1)) == 1:
            break
    if e == d:
        return rsa_key(Min,Max)
    return {"public":(e,n),"private":(d,n)}

def enrsa(Str,e,n1,d,n2):
    udata2 = []
    udata3 = str(hash(Str))
    udata4 = []
    for i in Str:
        udata2.append(hex(ord(i)**e%n1))
    for i in udata3:
        udata4.append(hex(ord(i)**d%n2))
    udata5 = ""
    udata6 = ""
    for i in range(len(udata2)):
        udata5+=udata2[i]
        if i != len(udata2)-1:
            udata5+=" "
    for i in range(len(udata4)):
        udata6+=udata4[i]
        if i != len(udata4)-1:
            udata6+=" "
    return udata5+","+udata6

def dersa(Str,e,n1,d,n2):
    Str2 = Str.split(",")
    Str2[0] = Str2[0].split(" ")
    Str2[1] = Str2[1].split(" ")
    udata2 = ""
    udata3 = ""
    for i in Str2[0]:
        udata2+=chr(int(i,16)**d%n2)
    for i in Str2[1]:
        udata3+=str(int(i,16)**e%n1)
    return udata2,udata3