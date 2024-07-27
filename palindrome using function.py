def palindrome():
    n=int(input("enter the num"))
    temp=n
    sum=0
    while n!=0:
        r=n%10
        sum=sum*10+r
        n=n//10
    if(sum==temp):
        print(temp,"palindrome")
    else:
        print(temp,"not palindrome")
palindrome()
