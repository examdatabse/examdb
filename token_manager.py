import hashlib
import time


class TokenManager:
    def __init__(self):
        pass

    @staticmethod
    def generate_token():
        seed = time.time()
        token = hashlib.sha256(str(seed).encode('utf-8')).hexdigest()
        return seed, token


