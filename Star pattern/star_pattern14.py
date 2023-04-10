a=int(input("rows:"))
print("columns = rows i.e.",a)
b=a
# k=a-1
for i in range(0,a):
    k=a-1-i
    for j in range(0,b):
        if j<=a-i-1:
            print(k,end='')
            k-=1
        else:
            print(" ",end='')
    print()
        
  
'''
6543210
543210
43210
3210
210
10
0
'''  