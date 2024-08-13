#print rectangular
def print_rectangle(rows, cols):
    for i in range(rows):
        for j in range(cols):
            print("*", end=" ")
        print()
print_rectangle(5, 10)

#calculate tax
n=float(input("Enter a number:"))
if n<=150000:
    print("Tax=0")
elif n>=150001 and n<=300001:
    print(n*0.10)
elif n>=300001 and n<=500000:
    print(n*0.20)
else:
    print(n*0.30)


#word Ascending order and descending order

names = input("Enter names:").split(',')
order = input("ascending (A) or descending (D) order? ").strip().upper()
if order=='A':
    names.sort()
elif order=='D':
    names.sort(reverse=True)
else:
    print("Invalid option. Please enter 'A' for ascending or 'D' for descending.")

print("Sorted names:", names)


#Mulplication matrix
matrix1 = [
    [1, 2],
    [4, 5]
]
matrix2 = [
    [9, 8],
    [6, 5]
]
result = [
    [0, 0],
    [0, 0]
]

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][j] * matrix2[i][j]
for row in result:
    print(row)


