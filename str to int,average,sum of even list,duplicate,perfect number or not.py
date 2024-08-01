integer="60"
string=integer
print(string)


a=[1,2,6,9,3,5,7]
total=(a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6])
average=total/7
print(average)


s=[1,2,4,8,5,9,6]
sum=0
for n in s:
    if n%2==0:
        sum=sum+n
        print(sum)


list1=[1,2,2,4,7,8,9,9,6,3]
duplicate=list(set(list1))
print(duplicate)


import math
n=int(input("Enter a number"))
p=math.sqrt(n)
if p.is_integer():
    print("The number is a perfect square")
else:
    print("The number is not a perfect square")
