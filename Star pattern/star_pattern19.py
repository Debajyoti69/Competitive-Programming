a=int(input("rows:"))
b=a*2-1
c=-1
print('cloumns=',b)
for i in range(1,a+1):
    k="A"
    c+=1
    for j in range(1,b+1):
        if j>=a-c and j<=a+c:
            print(k,end='')
            if j<a:
                k=chr(ord(k)+1)
            else:
                k=chr(ord(k)-1)
        else:
            print(" ",end='')
    print()


'''
   A
  ABA
 ABCBA
ABCDCBA
'''


