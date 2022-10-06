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

with open('test.txt','rb') as input:
    a = input.read()
a = encrypt(a)
with open('encrypted.txt','wb') as output:
    output.write(a)
a = decrypt(a)
with open('decrypted.txt','wb') as output:
    output.write(a)


