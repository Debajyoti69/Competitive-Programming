a=int(input("rows:"))
b=a
print("rows=column i.e.",b)

for i in range(1,a+1):
    for j in range(1,b+1):
        if j<=i:
            if j%2!=0:
                print("1",end="")
            else:
                print("0",end='')
        else:
            print(" ",end="")
    print()


'''
1
10
101
1010
10101
101010
'''

