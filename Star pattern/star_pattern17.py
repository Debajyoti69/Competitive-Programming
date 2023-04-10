a=int(input("rows:"))
b=a
c=(b+1)/2
print("rows=column i.e.",b)
k=-1
for i in range(1,a+1):
    if i<=c:
        k+=1
    else:
        k-=1
    for j in range(1,b+1):
        if j<=c-k or j>=c+k:
            print('*',end='')            
        else:
            print(" ",end='')
    print()
        
'''
*********
**** ****
***   ***
**     **
*       *
**     **
***   ***
**** ****
*********
'''