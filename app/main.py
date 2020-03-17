import secret_exp

class CardInfo():

    card_number = ''
    card_cvv = ''
    card_due_date = ''


class User():

    def sendCardInfo(model):
        pass

    def encryptCardInfo(rsa, exp):
        pass


class Internet():

    def transfer():
        pass


class Hacker():

    def hack():
        pass

crypto = secret_exp.Crypto()
array = crypto.buildPrimeNumbers(60)
number = crypto.getRandomNumber(0, len(array)-1, False)
A = array[number]
print("A: " + str(A))
number = crypto.getRandomNumber(0, len(array)-1, False)
B = array[number]
print("B: " + str(B))

N = crypto.generateRSAKey(A, B)
print("N: " + str(N))
fi = crypto.eilerFunction(A, B)
print("fi: " + str(fi))
e = crypto.findExp(fi, array)
print("e: " + str(e))
d = crypto.secretExp(fi, e)
print("d: " + str(d))

message = 62
print('message: ' + str(message))

secretmessage = crypto.encrypt(e, N, message)
print('secretmessage: ' + str(secretmessage))

decryptedmessage = crypto.decrypt(d, N, secretmessage)
print('decryptedmessage: ' + str(decryptedmessage))
