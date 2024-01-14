import random

print("when you say throw you will roll the dice")

def dice_race():
  print("Robot: Choose a number to race for. It should be higher than 10 lower than 100")
  you = input(": ")
  try:
    you = int(you)
    you = min(max(you, 10), 100)
  except ValueError as e:
    print(you, f"is not a number\n{e}")
  robot_score = 0
  player_score = 0
  while True:
    throw = input("say throw: ")
    throw = throw.lower()
    if throw == "throw":
      player_score += random.randint(1, 6)
      print(player_score)
      
      robot_score += random.randint(1, 4)
      print(robot_score)
      
    else:
      print("Enter throw please!")
      
    if player_score >= you:
      print("Player wins")
      break
      
    elif robot_score >= you:
      print("Robot wins")
      break


dice_race()