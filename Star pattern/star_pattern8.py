a=int(input("rows :"))
print(f"cloumns={2*a-1}")
b=2*a-1

for i in range(1,a+1):
    k=1
    for j in range(1,b+1):
        if j>=a+1-i and j<=a-1+i:
            print(k,end="")
            if j<a:
                k+=1
            else:
                k-=1
        else:
            print(" ",end="")
    print()
    
'''
   1
  121
 12321
1234321
'''