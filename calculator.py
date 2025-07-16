# A simple calculator app
print('''***********\n1. Additon\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponential\n*********** ''')
print ("Enter two numbers to add:")
# prompt the user for a number and store it
firstnumber=(input("First Number:"))
# propmt the user for the second number and store it
secondnumber=(input("Second Number:"))
sum = float(firstnumber) +float(secondnumber)
print(f"{firstnumber} + {secondnumber} = {sum}")

print("***********\nSubtraction")
print ("Enter two numbers to subtract:")
# prompt the user for a number and store it
firstnumber=(input("First Number:"))
# propmt the user for the second number and store it
secondnumber=(input("Second Number:"))
sub = float(firstnumber) - float(secondnumber)
print(f"{firstnumber} - {secondnumber} = {sub}")
  
print("***********\nMultiplication")
print ("Enter two numbers to multipy:")
# prompt the user for a number and store it
firstnumber=(input("First Number:"))
# propmt the user for the second number and store it
secondnumber=(input("Second Number:"))
mul = float(firstnumber) * float(secondnumber)
print(f"{firstnumber} * {secondnumber} = {mul}")

print("***********\nDivision")
print ("Enter two numbers to divide:")
# prompt the user for a number and store it
firstnumber=(input("First Number:"))
# propmt the user for the second number and store it
secondnumber=(input("Second Number:"))
div = float(firstnumber) / float(secondnumber)
print(f"{firstnumber} / {secondnumber} = {div}")

print("***********\nExponential")
print ("Enter two numbers to exponent:")
# prompt the user for a number and store it
firstnumber=(input("First Number:"))
# propmt the user for the second number and store it
secondnumber=(input("Second Number:"))
exp = float(firstnumber) ** float(secondnumber)
print(f"{firstnumber} ** {secondnumber} = {exp}")


 

