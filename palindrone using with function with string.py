def palindrome():
    s=str(input("enter the string"))
    temp=s
    reverse=s[::-1]
    if(reverse==temp):
        print("palindrome")
    else:
        print("not palindrome")
palindrome()
