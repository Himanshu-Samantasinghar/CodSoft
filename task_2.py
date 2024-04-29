def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide two numbers"""
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def get_user_input():
    """Get user input for operation choice and numbers"""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return (choice, num1, num2)
    else:
        print("Invalid input")
        return None

def perform_operation(choice, num1, num2):
    """Perform the selected operation"""
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))

def main():
    """Main function to handle user interaction"""
    while True:
        operation = get_user_input()
        if operation:
            choice, num1, num2 = operation
            perform_operation(choice, num1, num2)
        
        again = input("Do you want to perform another calculation? (yes/no): ")
        if again.lower() != "yes":
            break

if __name__ == "__main__":
    main()
