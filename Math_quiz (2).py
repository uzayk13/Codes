import random
def ask_question():
  operation = random.choice(["+","-","*","/"])
  number1 = random.randint(1,1000)
  if operation == "/":
    number2 = random.randint(1,number1)
    
  else:
    number2 = random.randint(1,1000)
  question = str(number1) + operation + str(number2) + " = "
  players_answer = float(input(question))

  if operation == "+":
    if number1 + number2 == players_answer:
      return True
      
  elif operation == "-":
    if number1 - number2 == players_answer:
      return True

  elif operation == "*":
    if number1 * number2 == players_answer:
      return True
    

    elif operation == "/":
      if int(number1 / number2) == players_answer:
        return True
  
  return False


print("This is a simple test. There will be 10 random math questions witch it's numbers are between 1 and 1000.")
print()
counter = 0
for i in range(10):
  if ask_question():
    counter += 1
print(f"You got {counter} out of 10.") 