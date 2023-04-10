a=int(input("rows :"))
print(f"cloumns={2*a-1}")
b=2*a-1

for i in range(1,a+1):
    k1,k2=1,"A"
    for j in range(1,b+1):
        if j>=a+1-i and j<=a-1+i:
            if j<=a:
                print(k1,end="")
                k1+=1
            elif j>a:
                print(k2,end="")
                k2=chr(ord(k2)+1)
        else:
            print(" ",end="")
    print()
    

'''
   1
  12A
 123AB
1234ABC
'''