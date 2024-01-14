running = 1
while running == 1:
  a = 1
  
  
  my_number = int(input("Type in a number: "))
  def prime_number_checker(my_number):
    if my_number < 2:
      print("Your number is not a prime number.")
    for i in range(2, my_number):
      if my_number%i == 0:
        print("This number is not a prime number.")
        break
  
      else:
        a = 2
        return a
        
  
  
  a = prime_number_checker(my_number)
  
  if a == 2:
    print("This is a prime number.")

  again = input("Do you want to try another prime number? (y/n) ")
  if again == "y":
    continue

  elif again == "n":
    running = 2