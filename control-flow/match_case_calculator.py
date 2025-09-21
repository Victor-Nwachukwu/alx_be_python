num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":   
        result = int(num1) + int(num2)
        print(f"The result is {result}")

    case "-":
        result = int(num1) - int(num2)  
        print(f"The result is {result}")

    case "*":
        result = int(num1) * int(num2)  
        print(f"The result is {result}")

    case "/":
        if int(num2) != 0:
            result = int(num1) / int(num2)  
            print(f"The result is {result}")
        else:
            print("Cannot divide by zero.")