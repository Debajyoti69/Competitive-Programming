a=int(input('rows:'))
b=a
print("colums=rows=",b)

for i in range(1,a+1):
    for j in range(1,b+1):
        if j==i or j==a+1-i:
            print("*",end='')
        else:
            print(" ",end='')
    print()
    

'''
*   *
 * *
  *
 * *
*   *
'''




