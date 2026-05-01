

import math



while True:
    print("Choose any one operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. close")

    choice = input("Enter choice (1-7): ")

    if choice == "7":
        print("closing calculator...")
        break

    try:
        if choice in ["1", "2", "3", "4", "5"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", a + b)

            elif choice == "2":
                print("Result:", a - b)

            elif choice == "3":
                print("Result:", a * b)

            elif choice == "4":
                if b == 0:
                    print("Error: Division by zero not allowed")
                else:
                    print("Result:", a / b)

            elif choice == "5":
                print("Result:", a ** b)

        elif choice == "6":
            num = float(input("Enter number: "))
            if num < 0:
                print("Error: Cannot take square root of negative number")
            else:
                print("Result:", math.sqrt(num))


        else:
            print("Invalid choice, try again")

    except Exception as e:
        print("Error:", e)
