a=int(input("rows: "))
b=a
print("cloumn=rows i.e.",b)
for i in range(1,a+1):
    k=i
    for j in range(1,b+1):
        if j==k:
            print("\\",end='')
        elif j==a+1-k:
            print('/',end='')
        else:
            print("*",end='')
    print()
    
'''
\*****/
*\***/*
**\*/**
***\***
**/*\**
*/***\*
/*****\
'''