from itertools import *

encypted = 'РППОЕААДТВЛ_ЕБЬЛНЫЕ_ПА_ВР'
arr = []
for letter in encypted:
    arr.append(str(letter))

def createblock(arr,i):
    block = arr[0*5+i]+arr[1*5+i]+arr[2*5+i]+arr[3*5+i]+arr[4*5+i]
    return block
encryptrd =''

for i in permutations('01234'): #получим кортеж комбинаций позиций для строк
        
        one=createblock(arr,int(i[0]))#создаем блоки
        two=createblock(arr,int(i[1]))
        the=createblock(arr,int(i[2]))
        fr=createblock(arr,int(i[3]))
        fw=createblock(arr,int(i[4]))
        
        encryptrd=encryptrd+one[0]+two[0]+the[0]+fr[0]+fw[0]#преобразуем в строки
        encryptrd=encryptrd+one[1]+two[1]+the[1]+fr[1]+fw[1]
        encryptrd=encryptrd+one[2]+two[2]+the[2]+fr[2]+fw[2]
        encryptrd=encryptrd+one[3]+two[3]+the[3]+fr[3]+fw[3]
        encryptrd=encryptrd+one[4]+two[4]+the[4]+fr[4]+fw[4]
        encryptrd=encryptrd+'\n'
        
    
my_fileEC = open("ENCRYPTED.txt", "w+", encoding='utf-8') #результат шифровки в отдельный файл
my_fileEC.write(encryptrd)
my_fileEC.close()