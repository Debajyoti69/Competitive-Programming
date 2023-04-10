a=int(input("rows :"))
print(f"cloumns={2*a-1}")
b=2*a-1

for i in range(1,a+1):
    k,k1,k2=1,1,'A'
    for j in range(1,b+1):
        if i%2!=0:
            if j>=a+1-i and j<=a-1+i and k:
                print(k1,end="")
                k,k1=0,k1+1
            else:
                print(" ",end="")
                k=1
        elif i%2==0:
            if j>=a+1-i and j<=a-1+i and k:
                print(k2,end="")
                k,k2=0,chr(ord(k2)+1)
            else:
                print(" ",end="")
                k=1
            
    print()
    
    
'''
   1
  A B
 1 2 3
A B C D
'''