a=int(input("rows:"))
b=a*2-1
c,d=-1,-1
print('cloumns=',b)
for i in range(1,a+1):
    k1,k2="A",1
    c+=1
    for j in range(1,b+1):
        if j>=a-c and j<=a+c:
            if j<=a:               
                print(k1,end='')
                k1=chr(ord(k1)+1)
            if j>=a:
               print(k2,end='')
               k2+=1
        else:
            print(" ",end='')
    print()
    

'''
   A1
  AB12
 ABC123
ABCD1234
'''