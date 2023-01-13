from pythonRSA import *


crypto = RSAHelper()
array = crypto.buildPrimeNumbers(1000)
number = crypto.getRandomNumber(100, len(array)-1, False)
A = array[number]
B = A
while A == B:
    number = crypto.getRandomNumber(100, len(array)-1, False)
    B = array[number]

if B == A:
    print("ErrorCode: 12 A shoud't be B")
    quit()

N = crypto.generateRSAKey(A, B)
fi = crypto.eilerFunction(A, B)
e = crypto.findExp(fi, array)
d = crypto.secretExp(fi, e)

loger = 'A: \t{0} \nB: \t{1} \nN: \t{2} \nfi: \t{3} \ne: \t{4} \nd: \t{5}'.format(A, B, N, fi, e, d)
print('\n---------------\n' + loger + '\n---------------\n')

def encryptMessage(message, e, N):

    list_encrypted_numbers = []
    for ch in message:
        number = ord(ch)
        encrypted_number = crypto.encrypt(e, N, number)
        list_encrypted_numbers.append(encrypted_number)
    return list_encrypted_numbers


def decryptMessage(list_encrypted_numbers, d, N):
    list_characters = []
    for number in list_encrypted_numbers:
        encrypted_number = crypto.decrypt(d, N, number)
        char = chr(encrypted_number)

        list_characters.append(char)
    return list_characters


message = "Hello encrypt!"
list_encrypted = encryptMessage(message, e, N)
print(list_encrypted)

list_characters = decryptMessage(list_encrypted, d, N)
print(list_characters)
