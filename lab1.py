# Ek(M)=aM+b mod m, шифр
# Dk(C)=a-1(C-b) mod m. дешифр
#decryptedLetter = ((KEYa^-1)*(C-KEYb)) % 256
# вар 8, Мирко Александр МБС-002. 1-8. m=256, k=(19,56).

from operator import mod
from turtle import position



def Encrypt(KEYa,KEYb, encrypt):#функция шифровки
    
    encrypted = ""
    for letter in encrypt:
        M = int(ord(letter))# порядок символа нахожу при помощи команды ord
        #Возвращает для указанного Юникод-символа целое, представляющее его позицию кода.
        encryptedLetter = (KEYa*M+KEYb) % 256 #шифрование кода символа
        encrypted = encrypted + chr(encryptedLetter)#преобразование нового кода в символ командрой chr
    print("ENCRYPT: ", encrypted,"\n")
    return encrypted


def getModularMultiplicativeInverse(a, n):#где a - число взаимно простое с n,
    for x in range(2, n):
        if (a * x) % n == 1:
            return int(x)


def Decrypt(KEYa,KEYb, decrypt):#функция дешифрования
    decrypted = ""
    for letter in decrypt:
        C = int(ord(letter))
        
        n = int(256)
        decryptedLetter = (getModularMultiplicativeInverse(KEYa, n) * (C - KEYb)) % 256 # дешифрование кода символа по алгоритму 
        
        decrypted = decrypted + chr(decryptedLetter)
    print("DECRYPT: ", decrypted,"\n")
    return decrypted


print(8*"*","Вариант 8, ключ 19 , 56 . словарь 256",8*"*","\n")
encrypt = "Message i need to hide and to understand" #СЮДА МОЖНО ВВЕСТИ ТЕКСТ ДЛЯ ШИФРОВКИ\ДЕШИФРОВКИ
print("Text to encrypt is: ' ", encrypt,"'","\n")
encrypted = Encrypt(19,56, encrypt) 
Decrypt(19, 56, encrypted)

exit = input()