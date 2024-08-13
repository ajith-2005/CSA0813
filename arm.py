#armstrong number
n=153
sum=0
temp=n
while (n!=0):
    r=n%10
    sum=sum+r*r*r
    n=n//10
if (sum==temp):
    print("armstrong")
else:
    print("not armstrong")

#harshad number
n=18
sum=0
while(n>0):
    digit=n%10
    sum=sum+digit
    n=n//10
if (n%sum==0):
    print("Harshad Number")
else:
    print("Not Harshad Number")


#happy number
n=18

v=set()

while n!=1 and n not in v:
    v.add(n)
    
    sum_of_squares = 0
    temp=n
    while temp>0:
        digit=temp % 10
        sum_of_squares += digit*digit
        temp//=10
    
    n = sum_of_squares

if n==1:
    print("The number is a happy number.")
else:
    print("The number is not a happy number.")


