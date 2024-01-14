import time
import random


Money = random.randint(30, 50)

def McDonalds(store, walletMoney):
  print("\n--------------------------------------------------")
  
  print("Welcome to McDonalds")
  
  print("--------------------------------------------------")

  print("You can look at the menu by typing 'Y'")
  
  print("--------------------------------------------------")
  
  print("You can order by typing the first letter of your food")
  
  print("--------------------------------------------------")
  
  print(f"You have ${walletMoney}")
  
  print("--------------------------------------------------")
  
  print("You will see your money everytime you purchase something")
  
  print("--------------------------------------------------")
  
  menuReq = str(input(">View the menu? (Y/N): "))
  if menuReq == "y" or menuReq == "Y":
    print("MENU \nBurger - $5 \nFries - $3 \nSoda - $1 \nChicken Nuggets - $9")
  foodReq = input("What would you like to order? (B/F/S/C): ")
  #----------------------------------------------------------------------
  #----------------------------------------------------------------------
  if foodReq == "b" or foodReq == "B" and walletMoney >= 5:
    print("You ordered a burger")
    print("--------------------------------------------------")
    time.sleep(0.5)
    print("Your food will arrive soon.")
    print("--------------------------------------------------")
    time.sleep(random.randint(1,5))
    print("Your food is here, enjoy!")
    print("--------------------------------------------------")
    print("You will give us $5")
    print("--------------------------------------------------")
    walletMoney -= 5
    print(f"You have ${walletMoney} left")
  #----------------------------------------------------------------------
  #----------------------------------------------------------------------
  elif foodReq == "F" or foodReq == "f" and walletMoney >= 3:
    print("You ordered fries")
    print("--------------------------------------------------")
    time.sleep(0.5)
    print("Your food will arrive soon.")
    print("--------------------------------------------------")
    time.sleep(random.randint(1,5))
    print("Your food is here, enjoy!")
    print("--------------------------------------------------")
    print("You will give us $3")
    print("--------------------------------------------------")
    walletMoney -= 3
    print(f"You have ${walletMoney} left")
  #----------------------------------------------------------------------
  #----------------------------------------------------------------------
  elif foodReq == "C" or foodReq == "c" and walletMoney >= 9:
    print("You ordered chicken nuggets")
    print("--------------------------------------------------")
    time.sleep(0.5)
    print("Your food will arrive soon.")
    print("--------------------------------------------------")
    time.sleep(random.randint(1,5))
    print("Your food is here, enjoy!")
    print("--------------------------------------------------")
    print("You will give us $9")
    print("--------------------------------------------------")
    walletMoney -= 9
    print(f"You have ${walletMoney} left")
  #----------------------------------------------------------------------
  #----------------------------------------------------------------------
  elif foodReq == "S" or foodReq == "s" and walletMoney >= 1:
    print("You ordered soda")
    print("--------------------------------------------------")
    time.sleep(0.5)
    print("Your soda will arrive soon.")
    print("--------------------------------------------------")
    time.sleep(random.randint(1,2))
    print("Your soda is here, enjoy!")
    print("--------------------------------------------------")
    print("You will give us $1")
    print("--------------------------------------------------")
    walletMoney -= 1
    print(f"You have ${walletMoney} left")
  #----------------------------------------------------------------------
  #----------------------------------------------------------------------
  print("--------------------------------------------")

  return walletMoney

  ### MC DONALDS CODE ENDS HERE ###


def Burger_King(store, walletMoney):
  

  print("\n--------------------------------------------------")

  print("Welcome to Burger King")

  print("--------------------------------------------------")

  print("You can look at the menu by typing 'Y'")

  print("--------------------------------------------------")

  print("You can order by typing the first letter of your food")

  print("--------------------------------------------------")

  print(f"You have ${walletMoney}")

  print("--------------------------------------------------")

  print("You will see your money everytime you purchase something")

  print("--------------------------------------------------")

  menuReq = str(input(">View the menu? (Y/N): "))
  if menuReq == "y" or menuReq == "Y":
    print("MENU \nWhopper - $9 \nFries - $3 \nSoda - $2 \nChicken Nuggets - $4")
  foodReq = input("What would you like to order? (W/F/S/O): ")
  #----------------------------------------------------------------------
  #----------------------------------------------------------------------
  if foodReq == "o" or foodReq == "O" and walletMoney >= 5:
    print("You ordered onion rings")
    print("--------------------------------------------------")
    time.sleep(0.5)
    print("Your food will arrive soon.")
    print("--------------------------------------------------")
    time.sleep(random.randint(1,5))
    print("Your food is here, enjoy!")
    print("--------------------------------------------------")
    print("You will give us $4")
    print("--------------------------------------------------")
    walletMoney -= 4
    print(f"You have ${walletMoney} left")
  #----------------------------------------------------------------------
  #----------------------------------------------------------------------
  elif foodReq == "F" or foodReq == "f" and walletMoney >= 3:
    print("You ordered fries")
    print("--------------------------------------------------")
    time.sleep(0.5)
    print("Your food will arrive soon.")
    print("--------------------------------------------------")
    time.sleep(random.randint(1,5))
    print("Your food is here, enjoy!")
    print("--------------------------------------------------")
    print("You will give us $3")
    print("--------------------------------------------------")
    walletMoney -= 3
    print(f"You have ${walletMoney} left")
  #----------------------------------------------------------------------
  #----------------------------------------------------------------------
  elif foodReq == "W" or foodReq == "w" and walletMoney >= 9:
    print("You ordered a Whopper")
    print("--------------------------------------------------")
    time.sleep(0.5)
    print("Your food will arrive soon.")
    print("--------------------------------------------------")
    time.sleep(random.randint(1,5))
    print("Your food is here, enjoy!")
    print("--------------------------------------------------")
    print("You will give us $9")
    print("--------------------------------------------------")
    walletMoney -= 9
    print(f"You have ${walletMoney} left")
  #----------------------------------------------------------------------
  #----------------------------------------------------------------------
  elif foodReq == "S" or foodReq == "s" and walletMoney >= 1:
    print("You ordered soda")
    print("--------------------------------------------------")
    time.sleep(0.5)
    print("Your soda will arrive soon.")
    print("--------------------------------------------------")
    time.sleep(random.randint(1,2))
    print("Your soda is here, enjoy!")
    print("--------------------------------------------------")
    print("You will give us $2")
    print("--------------------------------------------------")
    walletMoney -= 2
    print(f"You have ${walletMoney} left")
  #----------------------------------------------------------------------
  #----------------------------------------------------------------------
  print("--------------------------------------------")

  return walletMoney

  ### Burger King CODE ENDS HERE ###

def KFC(store, walletMoney):
  print("\n--------------------------------------------------")

  print("Welcome to KFC")

  print("--------------------------------------------------")

  print("You can look at the menu by typing 'Y'")

  print("--------------------------------------------------")

  print("You can order by typing the first letter of your food")

  print("--------------------------------------------------")

  print(f"You have ${walletMoney}")

  print("--------------------------------------------------")

  print("You will see your money everytime you purchase something")

  print("--------------------------------------------------")

  menuReq = str(input(">View the menu? (Y/N): "))
  if menuReq == "y" or menuReq == "Y":
    print("MENU \nChiken Bucket - $9 \nFries - $2 \nSoda - $1 \nChicken Burger - $5")
  foodReq = input("What would you like to order? (C/F/S/CB): ")
  #----------------------------------------------------------------------
  #----------------------------------------------------------------------
  if foodReq == "C" or foodReq == "c" and walletMoney >= 5:
    print("You ordered a Chicken bucket")
    print("--------------------------------------------------")
    time.sleep(0.5)
    print("Your food will arrive soon.")
    print("--------------------------------------------------")
    time.sleep(random.randint(1,5))
    print("Your food is here, enjoy!")
    print("--------------------------------------------------")
    print("You will give us $9")
    print("--------------------------------------------------")
    walletMoney -= 9
    print(f"You have ${walletMoney} left")
  #----------------------------------------------------------------------
  #----------------------------------------------------------------------
  elif foodReq == "F" or foodReq == "f" and walletMoney >= 3:
    print("You ordered fries")
    print("--------------------------------------------------")
    time.sleep(0.5)
    print("Your food will arrive soon.")
    print("--------------------------------------------------")
    time.sleep(random.randint(1,5))
    print("Your food is here, enjoy!")
    print("--------------------------------------------------")
    print("You will give us $2")
    print("--------------------------------------------------")
    walletMoney -= 2
    print(f"You have ${walletMoney} left")
  #----------------------------------------------------------------------
  #----------------------------------------------------------------------
  elif foodReq == "CB" or foodReq == "cb" or foodReq == "Cb" and walletMoney >= 9:
    print("You ordered a chicken burger")
    print("--------------------------------------------------")
    time.sleep(0.5)
    print("Your food will arrive soon.")
    print("--------------------------------------------------")
    time.sleep(random.randint(1,5))
    print("Your food is here, enjoy!")
    print("--------------------------------------------------")
    print("You will give us $9")
    print("--------------------------------------------------")
    walletMoney -= 5
    print(f"You have ${walletMoney} left")
  #----------------------------------------------------------------------
  #----------------------------------------------------------------------
  elif foodReq == "S" or foodReq == "s" and walletMoney >= 1:
    print("You ordered soda")
    print("--------------------------------------------------")
    time.sleep(0.5)
    print("Your soda will arrive soon.")
    print("--------------------------------------------------")
    time.sleep(random.randint(1,2))
    print("Your soda is here, enjoy!")
    print("--------------------------------------------------")
    print("You will give us $1")
    print("--------------------------------------------------")
    walletMoney -= 1
    print(f"You have ${walletMoney} left")
  #----------------------------------------------------------------------
  #----------------------------------------------------------------------
  print("--------------------------------------------")

  return walletMoney

  ### KFC CODE ENDS HERE ###


workExp = 0

def Work(store, walletMoney):
  global workExp
  if workExp <= 4:
    print("You went to work!")
    print("Your work rank is rookie")
    time.sleep(0.5)
    print("You will earn some money!")
    time.sleep(4.5)
    earnedMoney = random.randint(1,25)
    print("You earned $", earnedMoney)
    workExp += 1
    walletMoney += earnedMoney
    print(f"You have ${walletMoney}")

  elif workExp <= 9:
    print("You went to work!")
    print("Your work rank is experienced worker!")
    time.sleep(0.5)
    print("You will earn some money!")
    time.sleep(4.5)
    earnedMoney = random.randint(25,50)
    print("You earned $", earnedMoney)
    workExp += 1
    walletMoney += earnedMoney
    print(f"You have ${walletMoney}")

  elif workExp <= 14:
    print("You went to work!")
    print("Your work rank is CEO asistant")
    time.sleep(0.5)
    print("You will earn some money!")
    time.sleep(4.5)
    earnedMoney = random.randint(50,75)
    print("You earned $", earnedMoney)
    workExp += 1
    walletMoney += earnedMoney
    print(f"You have ${walletMoney}")

  elif workExp <= 19:
    print("You went to work!")
    print("Your work rank is CEO")
    time.sleep(0.5)
    print("You will earn some money!")
    time.sleep(4.5)
    earnedMoney = random.randint(75, 100)
    print("You earned $", earnedMoney)
    workExp += 1
    walletMoney += earnedMoney
    print(f"You have ${walletMoney}")

  return walletMoney

### WORK CODE ENDS HERE ###





running = 1
walletMoney = Money
while running == 1:
  store = input("\nWhat store would you like to go to? (M/B/K/Work): ")
  if store == "M" or store == "m":
    walletMoney = McDonalds(store, walletMoney)
    
  elif store == "B" or store == "b":
    walletMoney = Burger_King(store, walletMoney)

  elif store == "K" or store == "k":
    walletMoney = KFC(store, walletMoney)

  elif store == "Work" or store == "work" or store == "WORK":
    walletMoney = Work(store, walletMoney)
