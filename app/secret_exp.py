import math
# import random


class Crypto:

    def getRandomNumber(self, min, max, isBasic):
        return 0

    # N
    def generateRSAKey(self, a, b):
        a = self.getRandomNumber(1, 1000, True)
        return a * b

    # d
    def secretExp(fi, e):
        k = 1
        max = 10000
        while True:
            d = (fi * k + 1) / e
            if d.is_integer():
                return d
            k = k + 1
            if k == max:
                return None

    # fi
    def eilerFunction(a, b):
        return (a-1) * (b-1)

    def encrypt(e, rsa, message):
        value = message ** e
        m_crypted = math.modf(value)[0]
        # m_reserve = math.modf(value)[1]
        return m_crypted

    def decrypt(d, rsa, message):
        value = message ** d
        de_crypted = math.modf(value)[0]
        # m_reserve = math.modf(value)[1]
        return de_crypted