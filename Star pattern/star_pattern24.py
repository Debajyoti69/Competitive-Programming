a=int(input("rows:"))
b=a
c=(a+1)/2
for i in range(1,a+1):
    for j in range(1,b+1):
        if (i==1 or i==a or j==1 or j==a) or (i>=c-1 and i<=c+1 and j>=c-1 and j<=c+1) and (i==c-1 or i==c+1 or j==c-1 or j==c+1):
            print("*",end='')
        else:
            print(" ",end="")
    print()


'''
*******
*     *
* *** *
* * * *
* *** *
*     *
*******
'''