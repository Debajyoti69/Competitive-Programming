a=int(input("rows: "))
b=int((a+1)/2)
k=b+1
for i in range(1,a+1):
    c=1
    if i<=b:
        k-=1       
    else:
        k+=1
    for j in range(1,b+1):
        if j>=k:
            print(c,end="")
            c+=1
        else:
            print(" ",end='')
    print()
    
    
'''
    1
   12
  123
 1234
12345
 1234
  123
   12
    1
'''