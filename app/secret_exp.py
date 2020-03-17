import math
import random


class Crypto:

    def buildPrimeNumbers(self, max):
        list = []
        k = 0
        for i in range(2, max+1):
            for j in range(2, i):
                if i % j == 0:
                    k = k + 1
            if k == 0:
                list.append(i)
            else:
                k = 0
        return list

    def getRandomNumber(self, min, max, isBasic):
        value = random.randint(min, max)
        return value

    # e
    def findExp(self, fi, array):
        for n in array:
            if (fi / n).is_integer() is False:
                return n
        return None

    # N
    def generateRSAKey(self, a, b):
        return a * b

    # d
    def secretExp(self, fi, e):
        k = 1
        max = 10000
        while True:
            d = (fi * k + 1) / e
            if d.is_integer() is True:
                return d
            k = k + 1
            if k == max:
                return None

    # fi
    def eilerFunction(self, a, b):
        return (a-1) * (b-1)

    def encrypt(self, e, rsa, message):
        value = message ** e
        m_crypted = value % rsa
        return m_crypted

    def decrypt(self, d, rsa, message):
        value = message ** d
        de_crypted = value % rsa
        return de_crypted
