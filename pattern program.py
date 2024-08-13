#square pattern
n=5
for i in range(0,n):
    for j in range(0,n):
        print("*",end="")
    print()


#rectangle
n=4
m=7
for i in range(n):
    for j in range(m):
        print("*", end="")
    print()

#daimond
n=6
for i in range(n):
    print(" " * (n-i-1)+""(2*i+1))
for i in range(n-2,-1,-1):
    print(" " * (n-i-1)+""(2*i+1))
    
#upper triangle
n=5
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

#lower triangle
n=5
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

#hallow triangle
    n = 5

# Create a hollow square pattern
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
