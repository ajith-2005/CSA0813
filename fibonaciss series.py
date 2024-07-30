n=int(input("enter the no.of time"))
f1=0
f2=1
f3=0
for i in range(0,n+1):
    f1=f2
    f2=f3
    f3=f1+f2
    print(f3)
    
