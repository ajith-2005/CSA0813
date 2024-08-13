def decimal_to_binary_octal(decimal_number):
    if decimal_number < 0:
        raise ValueError("Please enter a non-negative integer.")
    
    binary_number = bin(decimal_number)[2:]  
    octal_number = oct(decimal_number)[2:]      
    return binary_number, octal_number

if name=="main":
    try:
        decimal_number = int(input("Enter a decimal number: "))
        binary_number, octal_number = decimal_to_binary_octal(decimal_number)
        print("Binary equivalent: {binary_number}")
        print("Octal equivalent: {octal_number}")
    except ValueError as e:
        print(e)
