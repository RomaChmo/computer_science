number1 = input('Enter a number')
number1 = float(number1)
number2 = input('Enter a second number')
number2 = float(number2)
number3 = input('Enter a third number')
number3 = float(number3)

l=number1
if l < number2:
    l = number2
if l < number3:
    l = number3
print('The largest number is',l)
  