
running = True
rocks = 20

while running:
  while rocks > 0:
    player1 = 0
    while player1 != 1 and player1 != 2:
      player1 = input("Player 1 would you like to remove 1 or 2 stones?")
      if player1 == "Ur mom":
        print("Never Gonna Give You Up Never Gonna Let You Down")
        print()
        print("You should have manners. This is a life lesson")
      else:
        player1 = int(player1)
    
    rocks -= player1
    print(f"There are {rocks} rocks left")
    if rocks <= 0:
      print("Player 2 wins")
      break
  
      
    player2 = 0
    while player2 != 1 and player2 != 2:
      player2 = input("Player 2 would you like to remove 1 or 2 stones?")
      if player2 == "Ur mom":
        print("Never Gonna Give You Up Never Gonna Let You Down")
        print()
        print("You should have manners. This is a life lesson")
      else:
        player2 = int(player2)
      
    rocks -= player2
    print(f"There are {rocks} rocks left")
    if rocks <= 0:
      print("Player 1 wins")
      break

  option = input("Do you want to play again?(y/n) ")    
  option = option.lower()
  
  if option == "y":
    running = True
    rocks = 20
  else:
    option = input("Are you sure you want to leave?(y = leave n = don't leave) ")
    option = option.lower()
  


if option == "n":
  running = True
  rocks = 20
else:
  running = False
