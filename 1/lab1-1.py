from operator import mod
import base64
import pathlib
from turtle import position
import pathlib


def Encrypt(KEYa,KEYb, encrypt):#функция шифровки
    
    encrypted = ""
    
    for letter in encrypt:
        M = int(ord(letter))# порядок символа нахожу при помощи команды ord
        #Возвращает для указанного Юникод-символа целое, представляющее его позицию кода.
        encryptedLetter = (KEYa*M+KEYb) % 256 #шифрование кода символа
        encrypted = encrypted + chr(encryptedLetter)#преобразование нового кода в символ командрой chr
        
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
    
    return decrypted


print(8*"*","Вариант 8, ключ 19 , 56 . словарь 256",8*"*","\n")
path = input("enter the name of the file - ")

ext=(pathlib.Path(path).suffix)
ext='result' + ext
with open(path,'rb') as f:
        res = base64.b64encode(f.read())

    
res = res.decode('utf-8')

encrypted = Encrypt(19,56, res) #шифровка
    
my_fileEC = open("ENCRYPTED.txt", "w+", encoding='utf-8') #результат шифровки в отдельный файл
my_fileEC.write(encrypted)
my_fileEC.close()


Result = Decrypt(19, 56, encrypted) #дешифровка для проверки


img = base64.b64decode(Result)
file = open(ext,'wb')
file.write(img)
file.close()
    
print("programm completed, result saved in files 'ENCRYPTED.txt' and " + ext)
exit = input()