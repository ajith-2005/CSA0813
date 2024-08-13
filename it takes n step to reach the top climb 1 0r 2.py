def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
s=4
print("Number of ways=",end="")
print(fib(s+1))
