#Binary number
#To wirte a binary number in code
#Put a 0b before the binary digits
binary_number = 0b1101
print(binary_number)
#To write an octal number use 0o
octal_number = 0o12
print(octal_number)
#To write an hexadecimal use 0x
hexadecimal_number = 0x12
print(hexadecimal_number)

#Convert user input from binary
#To decimal
bin_num = input('Entert binary number')
bin_to_dec = int(bin_num,2)
print(f'The value {bin_num} is {bin_to_dec}')

#Ask the user for two binary number
#Print their total
bin_num1 = input('Enter binary number1')
bin_num2 = input('Enter binary number2')
bin_to_dec1 = int(bin_num1,2)
bin_to_dec2 = int(bin_num2,2)
total = bin_to_dec1 + bin_to_dec2
print('Total is',total)

#Ask the user for two octal number
#print their total
octal_num1 = input('Enter octal number1')
octal_num1 = int(octal_num1,8)
octal_num2 = input('Enter octal number2')
octal_num2 - int(octal_num2,8)
total = octal_num1 + octal_num2
print('Total is',total)

print(bin(11))      
print(oct(11))
print(hex(11))