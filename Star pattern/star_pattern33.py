a=int(input("rows :"))
print(f"cloumns={2*a-1}")
b=2*a-1

for i in range(1,a+1):
    k='A'
    for j in range(1,b+1):
        if j<=a+1-i or j>=a-1+i:
            print(k,end="")
            k=chr(ord(k)+1)
        else:
            print(" ",end="")
            k=chr(ord(k)+1)

    print()
    
'''
ABCDEFG
ABC EFG
AB   FG
A     G
'''