# Calculator----

# Build a basic calculator that performs addition, subtraction, multiplication, and division.
# Add error handling for invalid inputs.

print("Welcome To The Two Operation Calculator: ")

try:
    # Input numbers
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
except ValueError:
    print("Error: Please enter valid numbers!")
    exit()

# Display menu
print("\nChoose an Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

try:
    # Input choice
    choice = int(input("Enter Your Choice (1-4): "))
    match choice:
        case 1:
            result = a + b
        case 2:
            result = a - b
        case 3:
            result = a * b
        case 4:
            if b == 0:
                raise ZeroDivisionError("Error: Division by zero is not allowed!")
            result = a / b
        case _:
            print("Error: Invalid choice. Please select a number between 1 and 4.")
            exit()
    
    print(f"Result: {result}")

except ValueError:
    print("Error: Invalid input. Please enter a number for your choice.")
except ZeroDivisionError as e:
    print(e)
