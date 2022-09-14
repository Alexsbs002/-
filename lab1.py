# Ek(M)=aM+b mod m, шифр
# Dk(C)=a-1(C-b) mod m. дешифр

# вар 8, Мирко Александр МБС-002. 1-8. m=256, k=(19,56).

from operator import mod
from turtle import position



def Encrypt(KEYa,KEYb, encrypt):
    
    encrypted = ""
    for letter in encrypt:
        M = int(ord(letter))
        encryptedLetter = (KEYa*M+KEYb) % 256
        encrypted = encrypted + chr(encryptedLetter)
    print(" ENCRYPT: ", encrypted,"\n")
    return encrypted


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
    print("DECRYPT: ", decrypted,"\n")
    return decrypted


print(8*"*","Вариант 8, ключ 19 , 56 . словарь 256",8*"*","\n")
encrypt = "hfeuhufehu feuhfueh ufueh ufhe uu fheu huhfue huf DF E FG E F FFFFFFFFFFFFF DFFFF HFHFHHFHF EHHEH CHECKED " #СЮДА МОЖНО ВВЕСТИ ТЕКСТ ДЛЯ ШИФРОВКИ\ДЕШИФРОВКИ
print("Text to encrypt is: ' ", encrypt,"'","\n")
encrypted = Encrypt(19,56, encrypt) 
Decrypt(19, 56, encrypted)