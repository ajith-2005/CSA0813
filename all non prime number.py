a=12
b=30
for x in range (a,b+1):
    if x>1:
        for i in range (2,x):
            if (x%i)==0:
                break
            else:
                print(x)
    
