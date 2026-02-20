num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
opration=input("Enter the operation you want to perform: ")
if opration=="+":
    result=num1+num2
    print(f"The result of {num1} + {num2} is: {result}")
elif opration=="-":
    result=num1-num2
    print(f"The result of {num1} - {num2} is: {result}")
elif opration=="*":
    result=num1*num2
    print(f"The result of {num1} * {num2} is: {result}")
elif opration=="/":
    if num2==0:
        print("Error: Division by zero is not allowed.")
    else:
        result=num1/num2
        print(f"The result of {num1} / {num2} is: {result}")
else:
    print("Invalid operation. Please enter +, -, *, or /.")
    
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
elif result == 0:
    print("The result is zero.")