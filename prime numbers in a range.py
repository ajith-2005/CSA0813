n1=int(input("enter the value of n1"))
n2=int(input("enter the value of n2"))
for i in range(n1,n2+1):
        if i>0:
                count=0
                for j in range(1,i+1):
                        if i%j==0:
                                count=count+1
        if count==2:
                print(i)
    
