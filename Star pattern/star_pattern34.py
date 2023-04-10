a=int(input("rows:"))
b=a
print("columns=rows=",b)
k,c=1,a-1
for i in range(1,a+1):
    p=k
    c=a-i
    for j in range(1,b+1):
        if j<=i:
            print(p,end='')
            p=p-c-1
            c+=1
        else:
            print(" ",end='')
    k=k+(1+a)-i
    print()


'''
1
62
1073
131184
15141295
'''

