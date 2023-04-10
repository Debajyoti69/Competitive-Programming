a=int(input("rows: "))

b=2*a-1
print("cloumns : ",b)
c=b+1
for i in range(1,a+1):
    c=c-1
    for j in range(1,b+1):
        if j>=i and j<=c:
            print("*",end="")
        else:
            print(" ",end="")
    print()


'''
*********
 *******
  *****
   ***
    *
'''