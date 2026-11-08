print("Calculator")

num1 = int(input("Input a number: "))
num2 = int(input("Input a second number: "))

result = 0

operation = input("+ - * / ")

if(operation == "+"):
    result = num1 + num2
elif(operation == "-"):
    result = num1 - num2
elif(operation == "*"):
    result = num1 * num2
elif(operation == "/"):
    result = num1 / num2
else:
    print("Wrong input")

print(result)