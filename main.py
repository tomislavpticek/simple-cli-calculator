import art
from replit import clear

def clear_and_logo():
  clear()
  print (art.logo)


def calculate (first_number, second_number, operation):
  if(operation == '+'):
    return first_number + second_number
  elif(operation == '-'):
    return first_number - second_number
  elif(operation == '/'):
    return first_number / second_number
  elif(operation == '*'):
    return first_number * second_number

allowed_operations = ['+', '-', '/', '*']

first_number = 0
second_number= 0
result = 0
operation = ""
carryover = False

clear_and_logo()

while True:
  if (not carryover):
    first_number = float(input("Enter first number: "))
  
  print ("Pick one of the following operations: ", end="")
  for var in allowed_operations:
    if allowed_operations.index(var) != (len(allowed_operations)-1):
      print (f"[{var}] ", end="")
    else:
      print (f"[{var}]")
  
  while True:
      operation = input("Operation: ") 
      if operation not in allowed_operations:
        print("Invalid operation for this calculator, try again.")
      else:
        break
    
  second_number = float(input("Enter second number: "))
  
  result = calculate(first_number=first_number, second_number=second_number, operation=operation)
  
  print(f"{first_number} {operation} {second_number} = {result}")
  
  choice = ""
  
  while True:
    choice = input("Enter 'y' to use the result in the next calculation, 'n' to start a completely new calculation or enter 'exit' to exit the program: ")
    if (choice.lower() == "y" or choice.lower() == "n" or choice.lower() == "exit"):
      break
    else:
      print("Invalid input, try again.")
  
  clear_and_logo()

  if (choice == "exit"):
    break
  elif (choice == "y"):
    first_number = result
    carryover = True
  else:
    first_number = 0
    carryover = False
  
  second_number = 0
  operation = 0
  
