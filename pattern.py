#square
n=4
for i in range(1,n+1):
       print("*"*n)


#rectangle
n=7
for i in range(1,n-1,+1):
      print(" * "*n)


#diamond
def diamond_pattern(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
diamond_pattern(5)




#hallo square
n=6
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()




#lower triangle
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")


#upper triangle
rows = 6
for i in range(0, rows):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
