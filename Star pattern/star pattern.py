a=int(input("rows :"))
b=int(input("cloumn :"))

for i in range(1,a+1):
    for j in range(1,b+1):
        if i==j:
            print("*"*i,end="")
    print()


'''
*
**
***
****
*****
'''