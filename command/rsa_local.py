import rsa


def rsa_key(num: int):
    pubkey, privkey = rsa.newkeys(num)
    return pubkey, privkey


def enrsa(Str: str, pubkey, privkey):
    udata2 = rsa.encrypt(Str.encode("utf-8"), pubkey)
    udata3 = rsa.sign(Str.encode("utf-8"), privkey, 'SHA-256')
    return udata2, udata3


def dersa(Str: bytes, Digital_visa: bytes, pubkey, privkey):
    udata = rsa.decrypt(Str, privkey).decode("utf-8")
    try:
        udata2 = rsa.verify(udata.encode("utf-8"), Digital_visa, pubkey)
    except:
        udata2 = "error"
    return udata, udata2
