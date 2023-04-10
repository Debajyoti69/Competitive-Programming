a=int(input("rows: "))
b=a*2-1
print("columns: ",b)
for i in range (1,a+1):
    k=i
    for j in range (1,b+1):
        if j>=a+1-i and j<=a-1+i:
            print(k,end='')
            if j<a:
                k+=1
            elif j>=a:
                k-=1
        else:
            print(" ",end='')
    print()
    

'''
   1   
  232  
 34543 
4567654
'''