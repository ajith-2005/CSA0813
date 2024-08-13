#square
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()



#rectangle
n=6
m=9
for i in range(1,n):
    for j in range(1,m):
        print("*",end=" ")
    print()


#lower triangle
n=6
for i in range(1,n+1,+1):
    print("*"*i)



#upper triangle
def upper_triangle(n):
    for i in range(n):
        for j in range(n):
            if j>=i:
                print("*", end=" ")
                
            print()

n=5
upper_triangle(n)

#hallow square
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
            print()


#diamond
n=6
for i in range(n):
    print(" " * (n-i-1)+""(2*i+1))
for i in range(n-2,-1,-1):
    print(" " * (n-i-1)+""(2*i+1))
