a=int(input("rows: "))
b=int((a+1)/2)
print("cloumns: ",b)
k=0
for i in range (1,a+1):
    if i<=b:
        k+=1
    else:
        k-=1
    for j in range (1,b+1):
        if j<=k:
            print("*",end="")
        else:
            print(" ",end='')

    print()
    
'''
*
**
***
****
***
**
*
'''