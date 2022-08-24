from cryptography.fernet import Fernet
from decouple import config


key = config('ENC_KEY')

def encrypt(self, data, **kwargs):
    f = Fernet(key)
    return f.encrypt(data)


def decrypt(self, data, **kwargs):
    f = Fernet(key)
    return f.decrypt(data)