a=int(input("rows:"))
b=2*a
print("columns:",b)
k=a+1
for i in range(1,a+1):
    k-=1
    for j in range(1,b+1):
        if j>=k and j<=k+4:
            print("*",end='')
        else:
            print(" ",end='')
    print()

'''
   *****
  *****
 *****
*****
'''