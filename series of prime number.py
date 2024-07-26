n1=3
n2=10
for i in range(n1,n2+1):
    if i>1:
        count=0
        for j in range(1,i+1):
            if i%j==0:
                print("prime numbers b/w",n1,"and",n2,"=",i)
