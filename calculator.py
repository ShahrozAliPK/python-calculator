# Forever Loop, until user exits
while(True):

  # UI Menu
  print("-----------------------")
  print("Instructions:")
  print("1.Keep typing the numbers and press enter.")
  print("2.For final answer type '='")
  print("3.Carefully type the numbers.")
  print("-----------------------")
  print("What do you want to do?")
  print("-----------------------")
  print(" | + | - | * | / |")
  print("-----------------------")

  # Ask for operation
  operation = input()

  # If "+"
  if operation == "+":

    # Display text to start
    print("Enter numbers to add")

    # List to store numbers
    numbers = []

    # Keep prompting until user types "="
    while(True):

      # Prompt for number
      ask = input()

      # Check if to stop
      if ask == "=":

        # Answer
        ans = 0

        # Loop till all the numbers and do operation
        for i in range(len(numbers)):
            ans = ans + numbers[i]

        # Print final answer, exit the loop
        print(f"Answer: {ans}")
        break

      # Check for valid number
      if ask.isdigit() == False:

        while(True):
          ask = input("Invalid input\n")

          if ask.isdigit() == True:
            break

      # Insert number into the list
      numbers.append(int(ask))
    
  # If "-"
  if operation == "-":
    
    # Display text to start
    print("Enter numbers to subtract")

    # List to store numbers
    numbers = []

    # Keep prompting until user types "="
    while(True):

      # Prompt for number
      ask = input()

      # Check if to stop
      if ask == "=":

        # Assign first number 
        ans = numbers[0]
        
        # Loop till all the numbers (starting from second one) and do operation
        for i in range(1, len(numbers)):
            ans = ans - numbers[i]

        # Print final answer, exit the loop
        print(f"Answer: {ans}")
        break
      
      # Check for valid number
      if ask.isdigit() == False:

        while(True):
          ask = input("Invalid input\n")

          if ask.isdigit() == True:
            break

      # Add number to the list
      numbers.append(int(ask))

  # If "*"
  if operation == "*":
    
    # Display text to start
    print("Enter numbers to multiply")

    # List to store numbers
    numbers = []

    # Keep prompting until user types "="
    while(True):

      # Prompt for number
      ask = input()

      # Check if to stop
      if ask == "=":
        ans = 1

        # Loop till all the numbers
        for i in range(len(numbers)):
            ans = ans * numbers[i]

        # Print final answer
        print(f"Answer: {ans}")
        break

      # Check for valid number
      if ask.isdigit() == False:

        while(True):
          ask = input("Invalid input\n")

          if ask.isdigit() == True:
            break
    
      # Add number to the list
      numbers.append(int(ask))
    

  # If "/"
  if operation == "/":
    
    # Display text to start
    print("Enter numbers to divide")

    # List to store numbers
    numbers = []

    # Keep prompting until user types "="
    while(True):

      # Prompt for number
      ask = input()

      # Check if to stop
      if ask == "=":

        # Assign first number
        ans = numbers[0]

        # Loop till all the numbers (starting from second one)
        for i in range(1, len(numbers)):
            ans = ans / numbers[i]

        # Print final answer
        print(f"Answer: {ans}")
        break

      # Check for valid number
      if ask.isdigit() == False:

        while(True):
          ask = input("Invalid input\n")

          if ask.isdigit() == True:
            break

      # Add number to the list 
      numbers.append(int(ask))

  # After final answer, print '\n'
  if operation == "+" or operation == "-" or operation == "*" or operation == "/":
    print()

  else:
    print("Invalid operation...")

  # Ask for reuse or not?
  print("Do you want to use again? (yes/no)?")
  option = input()

  # If "no", exit the loop
  if (option == "no"):
    break

# Exit the calculator
print("Thankyou!")
print("Program Developed By Syed Shehroz Ali")

