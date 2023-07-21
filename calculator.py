import math

memory = None

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Invalid input for square root"
    return math.sqrt(x)

def modulo(x, y):
    if y == 0:
        return "Cannot perform modulo with zero"
    return x % y

def store_result(result):
    global memory
    memory = result

def recall_memory():
    global memory
    return memory

def calculator():
    print("Welcome to the calculator!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Modulo")
    print("8. Store result to memory")
    print("9. Recall result from memory")
    print("10. Exit")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10): ")

        if choice == '10':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            print("Invalid choice. Please try again.")
            continue

        if choice in ('1', '2', '3', '4', '5', '7'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        elif choice == '6':
            num1 = float(input("Enter the number: "))

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = exponentiate(num1, num2)
        elif choice == '6':
            result = square_root(num1)
        elif choice == '7':
            result = modulo(num1, num2)
        elif choice == '8':
            store_result(result)
            print("Result stored to memory.")
            continue
        elif choice == '9':
            memory_result = recall_memory()
            if memory_result is not None:
                print("Recalled result from memory:", memory_result)
            else:
                print("Memory is empty.")
            continue

        print("Result:", result)


if __name__ == "__main__":
    calculator()