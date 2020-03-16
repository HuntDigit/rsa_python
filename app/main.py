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
print(A)
number = crypto.getRandomNumber(0, len(array)-1, False)
B = array[number]
print(B)

N = crypto.generateRSAKey(A, B)
print(N)
fi = crypto.eilerFunction(A, B)
print(fi)
e = crypto.findExp(fi, array)
print(e)
d = crypto.secretExp(fi, e)
print(d)

message = 62
print('message')
print(message)

secretmessage = crypto.encrypt(e, N, message)
print('secret mesage')
print(secretmessage)
decryptedmessage = crypto.decrypt(d, N, secretmessage)
print('decrypted mesage')
print(decryptedmessage)
