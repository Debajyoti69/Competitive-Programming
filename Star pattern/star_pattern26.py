a=int(input("rows:"))
b=a
print("rows=columns i.e.",b)

for i in range(1,a+1):
    k1,k2=i-1,'A'
    for j in range(1,b+1):
        if j<=i:
            print(chr(ord(k2)+k1),end='')
            k1-=1
        else:
            print(" ",end='')      
    print() 


'''
A
BA
CBA
DCBA
'''


