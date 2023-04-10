a=int(input("rows:"))
b=2*a-1
print("columns:",b)

for i in range(1,a+1):
    k=a+1
    for j in range(1,b+1):
        if j<=a:
            k-=1
        else:
            k+=1
        if j>=a-i+1 and j<=a+i-1:   
            print(k,end='')            
        else:
            print(" ",end='')
    print()


# ============
# also 2nd method
# ============


for i in range(1,a+1):
    k=i
    for j in range(1,b+1):
        if j>=a+1-i and j<=a-1+i:
            print(k,end='')
            if j<a:
                k-=1
            else:
                k+=1
        else:
            print(" ",end='')
    print()



'''
   1
  212
 32123
4321234
'''