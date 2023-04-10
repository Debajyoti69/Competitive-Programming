a=int(input("rows: "))
b=a
print("columns=rows",b)
k='A'
c=k
for i in range(1,a+1):
    if i>=2:
        k=chr(ord(k)+i)
        c=k
    for j in range(1,b+1):
        if j>=a+1-i:
            print(c,end='')
            c=chr(ord(c)-1)      
        else:
            print(" ",end='')
    print()



'''
   A
  CB
 FED
JIHG
'''