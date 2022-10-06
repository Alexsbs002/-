from operator import mod
import base64
import pathlib
from turtle import position
import pathlib

def encrypt(arr):
    
    arr = bytearray(arr)
    
    if len(arr)%6!=0:
        arr.append(255)
        for _ in range(len(arr),(len(arr)//6+1)*6):
            arr.append(0)
    
    for i in range(0, len(arr)//6):
        arr[i*6],arr[i*6+1],arr[i*6+2],arr[i*6+3],arr[i*6+4],arr[i*6+5] = arr[i*6+2],arr[i*6+4],arr[i*6],arr[i*6+5],arr[i*6+1],arr[i*6+3]
    
    return bytes(arr)

    
def decrypt(arr):
    
    arr = bytearray(arr)
    
    for i in range(0, len(arr)//6):
        arr[i*6],arr[i*6+1],arr[i*6+2],arr[i*6+3],arr[i*6+4],arr[i*6+5] = arr[i*6+2],arr[i*6+4],arr[i*6],arr[i*6+5],arr[i*6+1],arr[i*6+3]
    
    while arr[-1] == 0:
        del arr[-1]
    
    del arr[-1]
    
    return bytes(arr)



print(8*"*","Вариант 8",8*"*","\n")
path = input("enter the name of the file - ")
ext=(pathlib.Path(path).suffix)
ext='result' + ext


with open(path,'rb') as input:
    res = input.read()

encrypted = encrypt(res) #шифровка

with open('encrypted.txt','wb') as output:
    output.write(encrypted)


Result = decrypt(encrypted) #дешифровка для проверки

with open(ext,'wb') as output:
    output.write(Result)
    
print("programm completed, result saved in files 'ENCRYPTED.txt' and " + ext)
