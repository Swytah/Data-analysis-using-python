print("Hello World")

# Get age from user
age = int(input("Enter your age: "))
print("Your age:", age)

# Eligibility check
if age < 18:
    print("Not Eligible")
elif age == 18:
    print("Age is 18. You are Eligible.")
    first_name = input("Enter your First name: ")
    last_name = input("Enter your Last name: ")
    print("Full Name:", first_name + " " + last_name)
else:
    print("Eligible")
    first_name = input("Enter your First name: ")
    last_name = input("Enter your Last name: ")
    print("Full Name:", first_name + " " + last_name)
n = int(input("Enter how many numbers you want in your calculator: "))

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Percentage")
    print("6. Exit")

    u = int(input("Enter your choice: "))

    if u == 1:  # Addition
        t = 0
        for i in range(n):
            a = int(input(f"Enter number {i+1}: "))
            t += a
        print("Addition of", n, "digits is:", t)

    elif u == 2:  # Subtraction
        t = int(input("Enter first number: "))  # Initialize with first input
        for i in range(n - 1):  # Start loop from second number
            a = int(input(f"Enter next number: "))
            t -= a
        print("Subtraction of", n, "digits is:", t)

    elif u == 3:  # Multiplication
        t = 1  # Start with 1, not 0
        for i in range(n):
            a = int(input(f"Enter number {i+1}: "))
            t *= a
        print("Multiplication of", n, "digits is:", t)

    elif u == 4:  # Division
        t = float(input("Enter first number: "))  # First number initializes t
        for i in range(n - 1):
            a = float(input("Enter next number: "))
            if a == 0:
                print("Error: Cannot divide by zero. Skipping this number.")
                continue
            t /= a
        print("Division of", n, "digits is:", t)

    elif u == 5:  # Percentage
        y = float(input("Enter the total value for percentage calculation: "))
        t = 0
        for i in range(n):
            a = float(input(f"Enter number {i+1}: "))
            t += a
        k = (t / y) * 100  # Corrected percentage formula
        print("Percentage of", n, "digits is:", k, "%")

    elif u == 6:  # Exit
        print("Thanks!!")
        break

    else:
        print("Invalid choice! Please enter a valid option (1-6).")
print("Promotional Diary")
n = int(input("Enter number of employees: "))

for i in range(n):
    category = input(f"Enter the category of employee {i+1}: ")
    name = input(f"Enter the name of employee {i+1}: ")
    salary = float(input(f"Enter the salary of employee {i+1}: "))

    print("\nCategory:", category)
    print("Full Name:", name)
    print("Salary:", salary)

    if salary >= 50000.00 and category == '1':
        new_salary = salary + 10000.00
    elif salary <= 45000.00 and category == '2':
        new_salary = salary + 5000.00
    else:
        new_salary = salary + 3000.00

    print("New Salary:", new_salary)
    print("-" * 30)

print("Thanks!")
a = ()  # Tuple for ages
na = ()  # Tuple for names

while True:
    print("\n1. Add age")
    print("2. Add name")
    print("3. Change age or name")
    print("4. Print names and ages")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of ages to add: "))
        for i in range(n):
            age = int(input("Enter age: "))
            a += (age,)  # Using tuple concatenation
        print("Ages:", a)

    elif choice == 2:
        n = int(input("Enter number of names to add: "))
        for i in range(n):
            name = input("Enter name: ")
            na += (name,)  # Using tuple concatenation
        print("Names:", na)

    elif choice == 3:
        while True:
            print("\n1. Change age")
            print("2. Change name")
            print("3. Go back")

            ch = int(input("Enter your choice: "))

            if ch == 1:
                if len(a) == 0:
                    print("No ages entered yet!")
                    break
                else:
                    print("Ages:", a)
                    ind = int(input("Enter index to change (starting from 0): "))
                    if 0 <= ind < len(a):
                        value = int(input("Enter new age: "))
                        a = a[:ind] + (value,) + a[ind+1:]  # Creating a new tuple
                        print("Updated Ages:", a)
                    else:
                        print("Invalid index!")

            elif ch == 2:
                if len(na) == 0:
                    print("No names entered yet!")
                    break
                else:
                    print("Names:", na)
                    ind = int(input("Enter index to change (starting from 0): "))
                    if 0 <= ind < len(na):
                        value = input("Enter new name: ")
                        na = na[:ind] + (value,) + na[ind+1:]  # Creating a new tuple
                        print("Updated Names:", na)
                    else:
                        print("Invalid index!")

            elif ch == 3:
                break
            else:
                print("Incorrect choice!")

    elif choice == 4:
        print("Names:", na, "Ages:", a)

    elif choice == 5:
        print("Thanks!")
        break

    else:
        print("Invalid choice! Try again.")
a = []  # List for ages
na = []  # List for names

while True:
    print("\n1. Add age")
    print("2. Add name")
    print("3. Change age or name")
    print("4. Print names and ages")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of ages to add: "))
        for i in range(n):
            age = int(input("Enter age: "))
            a.append(age)  # Adding to list
        print("Ages:", a)

    elif choice == 2:
        n = int(input("Enter number of names to add: "))
        for i in range(n):
            name = input("Enter name: ")
            na.append(name)  # Adding to list
        print("Names:", na)

    elif choice == 3:
        while True:
            print("\n1. Change age")
            print("2. Change name")
            print("3. Go back")

            ch = int(input("Enter your choice: "))

            if ch == 1:
                if not a:  # Check if list is empty
                    print("No ages entered yet!")
                    break
                else:
                    print("Ages:", a)
                    ind = int(input("Enter index to change (starting from 0): "))
                    if 0 <= ind < len(a):
                        value = int(input("Enter new age: "))
                        a[ind] = value  # Directly modifying list
                        print("Updated Ages:", a)
                    else:
                        print("Invalid index!")

            elif ch == 2:
                if not na:  # Check if list is empty
                    print("No names entered yet!")
                    break
                else:
                    print("Names:", na)
                    ind = int(input("Enter index to change (starting from 0): "))
                    if 0 <= ind < len(na):
                        value = input("Enter new name: ")
                        na[ind] = value  # Directly modifying list
                        print("Updated Names:", na)
                    else:
                        print("Invalid index!")

            elif ch == 3:
                break
            else:
                print("Incorrect choice!")

    elif choice == 4:
        print("Names:", na, "Ages:", a)

    elif choice == 5:
        print("Thanks!")
        break

    else:
        print("Invalid choice! Try again.")
