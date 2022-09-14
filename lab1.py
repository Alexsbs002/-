# Ek(M)=aM+b mod m, шифр
# Dk(C)=a-1(C-b) mod m. дешифр

# вар 8, Мирко Александр МБС-002. 1-8. m=256, k=(19,56).

from operator import mod
from turtle import position

print("you enter 19 , 56 - keys. ", " cat - mesage to encrypt\n")

def Encrypt(KEYa,KEYb, encrypt):
    encrypt = encrypt.lower()
    encrypted = ""
    for letter in encrypt:
        M = int(ord(letter))
        encryptedLetter = (KEYa*M+KEYb) % 256
        encrypted = encrypted + chr(encryptedLetter)
    print("your cipher is ", encrypted,"\n")
    return encrypted


encrypted = Encrypt(19,56, "abc") 

def getModularMultiplicativeInverse(a, n):
    for x in range(2, n):
        if (a * x) % n == 1:
            return int(x)


def Decrypt(KEYa,KEYb, decrypt):
    decrypted = ""
    for letter in decrypt:
        C = int(ord(letter))
        
        #decryptedLetter = ((KEYa^-1)*(C-KEYb)) % 256
        n = int(256)
        decryptedLetter = (getModularMultiplicativeInverse(KEYa, n) * (C - KEYb)) % 256
        
        decrypted = decrypted + chr(decryptedLetter)
    print("your cipher is ", decrypted,"\n")
    return decrypted


Decrypt(19, 56, encrypted)