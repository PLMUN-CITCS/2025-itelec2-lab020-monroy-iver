# Iver John Monroy
# ITELEC2
# Laboratory # 20 - Group Activity # 01 - Problem 02: Even or Odd Checker with Input and Logic Functions



def main():
    try:
        number = int(input("Enter an integer: "))
        if number % 2 == 0:
            result = f"{number} is an Even number."
        else:
            result = f"{number} is an Odd number."
        print(result)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()