import math

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def natural_log(x):
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

def main():
    while True:
        print("\nScientific Calculator")
        print("1. Square root - √x")
        print("2. Factorial - x!")
        print("3. Natural logarithm (base e) - ln(x)")
        print("4. Power function - x^b")
        print("5. Exit")
        choice = input("Choose an operation (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the program. Goodbye!")
            break

        x = float(input("Enter the value of x: "))
        if choice == '4':
            b = float(input("Enter the value of b: "))

        try:
            if choice == '1':
                print("Result: ", square_root(x))
            elif choice == '2':
                print("Result: ", factorial(int(x)))  # Factorial requires an integer
            elif choice == '3':
                print("Result: ", natural_log(x))
            elif choice == '4':
                print("Result: ", power(x, b))
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError as e:
            print("Error:", e)
        except OverflowError as e:
            print("Error: Number too large.", e)

if __name__ == "__main__":
    main()
