a=int(input('rows: '))
b=2*a-1
print("cloumns=",b)
k=0
for i in range(1,a+1):
    if i%2==0:
        k=k+i
        c=k
    for j in range(1,b+1):
        if j<=2*i-1:
            if j%2==0:
                print("*",end='')
            else:
                if i%2==0:
                    print(c,end='')
                    c-=1
                else:
                    k+=1
                    print(k,end='')                  
        else:
            print(" ",end='')
    print()



