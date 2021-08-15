from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


def rsa_key(num: int):
    key = RSA.generate(num, Random.new().read)
    return key.publickey().export_key(), key.export_key()


def dersa(encrypted_data: bytes, signature: bytes, public_key: bytes, private_key: bytes):
    data = PKCS1_OAEP.new(RSA.import_key(private_key)).decrypt(encrypted_data)
    try:
        pkcs1_15.new(RSA.import_key(public_key)).verify(
            SHA256.new(data), signature)
        return data, True
    except:
        return data, False


def enrsa(data: bytes, public_key: bytes, private_key: bytes):
    return PKCS1_OAEP.new(RSA.import_key(public_key)).encrypt(data), pkcs1_15.new(RSA.import_key(private_key)).sign(SHA256.new(data))
