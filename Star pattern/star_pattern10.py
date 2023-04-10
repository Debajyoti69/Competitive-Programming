a=int(input("rows :"))
print(f'rows and cloums are same i.e. {a}')
b=a
# print(f"cloumns={2*a-1}")
# b=2*a-1
k=0
c=int((a+1)/2)
# print(c)
for i in range(1,a+1):
    if a%2==0:
        if i<=c:
            k+=1
        if i>c:
            k-=1
    else:
        if i<=c:
            k+=1
        else:
            k-=1
    for j in range(1,a+1):
        if j>=c+1-k and j<=c-1+k:
            print("*",end='')            
        else:
            print(" ",end='')
    print()
    
'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''