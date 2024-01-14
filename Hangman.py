import random
import time

guessedLetters = []

word = random.choice(["tiger", "banana", "japan", "python", "starwars", "computer",])

atempts = 10
  
def displayBoard(guessedLetters, word):
  
  Board = ""
  for letter in word:
    if letter in guessedLetters:
      Board += letter
    else:
      Board += "_"
  return Board


print(displayBoard(guessedLetters , word), "\n")


validLetters = "abcdefghijklmnopqrstuvwxyz"

print("Welcome to hangman!")

while True:
  guess = input("Guess a letter: ")
  guess = guess.lower()
  if len(guess) != 1 or guess not in validLetters:
    print("Invalid input!")

    continue

  if guess in guessedLetters:

    print("You already guessed that letter!")
    continue
    
  if guess in word:
    print("Correct!")
    guessedLetters.append(guess)
    print(displayBoard(guessedLetters , word))

  else:
    atempts -= 1
    print("Wrong!")
    print(f"You have {atempts} atempts left")
    print(displayBoard(guessedLetters , word))
    
    if atempts == 0:
      print("You lost!")
      time.sleep(1)
      break

  if all(letter in guessedLetters for letter in word):
    print("Contragulations! You won!")
    time.sleep(1)
    break












