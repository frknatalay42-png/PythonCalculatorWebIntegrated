def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero!"
    return a / b

def power(a, b):
    return a ** b

def average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(int(number))))

def calculator():
    print("Welcome to the Python Calculator!")
    print("Options:")
    print("1: Add (+)")
    print("2: Subtract (-)")
    print("3: Multiply (×)")
    print("4: Divide (÷)")
    print("5: Power (^)")
    print("6: Average of numbers")
    print("7: Sum of digits (bonus)")
    print("0: Exit")

    while True:
        choice = input("\nChoose an option (0-7): ")

        if choice == "0":
            print("Goodbye!")
            break
        elif choice in ["1", "2", "3", "4", "5"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(a, b))
            elif choice == "2":
                print("Result:", subtract(a, b))
            elif choice == "3":
                print("Result:", multiply(a, b))
            elif choice == "4":
                print("Result:", divide(a, b))
            elif choice == "5":
                print("Result:", power(a, b))

        elif choice == "6":
            nums = input("Enter numbers separated by space: ").split()
            nums = [float(n) for n in nums]
            print("Average:", average(*nums))

        elif choice == "7":
            num = input("Enter a number: ")
            print("Sum of digits:", sum_of_digits(num))
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    calculator()
