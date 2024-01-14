print("Welcome to the Odd or Even number finder!\n")
print(">Type 's' to start")
running = 1
while running == 1:
  start = input("> ")
  if start == "s":
    number = int(input("\n>Type a number: "))
    for i in range(number):
      find = number % 2
  
      if find == 0:
        print(f"{number} is an even number\n")
        break
      else:
        print(f"{number} is an odd number\n")
        break