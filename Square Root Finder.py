import time

print("Welcome to the Odd or Even number finder!\n")
print(">Type 's' to start")


running = 1
while running == 1:
  
  start = input(">")
  if start == "s":
    number = int(input("Type a number: "))
    squareRoot = number ** 0.5
    print("Calculating...")
    time.sleep(0.5)
    print(f"The square root of {number} is {squareRoot}")
  else:
    print("Invalid input")
    continue