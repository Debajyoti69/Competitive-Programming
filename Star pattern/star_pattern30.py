n=int(input("enter the value of n: "))
r=3*n
c=2*n-1
print("rows=",r,"\ncolumns=",c)

for i in range(1,r+1):
    for j in range(1,c+1):
        if i<=n:
            if j>=c+1-i:
                print("*",end='')
            else:
                print(" ",end='')
        elif i<=2*n:
            if j==n:
                print("|",end='')
            elif j<=i-n-1:
                print("*",end='')
            elif j>=i:
                print("*",end='')
            else:
                print(" ",end='')
        elif i<=3*n:
            if j<=(3*n)-i+1:
                print("*",end="")
            else:
                print(" ",end='')
    print()


'''
    *
   **
  ***
  |**
* | *
**|
***
**
*
'''

