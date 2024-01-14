import time

running = 1
while running == 1:

  print("Type in /cmds to see the commands")
  convert = input("/")
  convert = convert.lower()
  if convert == "cmds":
    print("CF = Celsius to Fahrenheit \nFC = Fahreheit to Celsius")
    print("End = End the program")
  elif convert == "cf":
    cf = input("What is the temperature in Celsius? ")
    f = float(cf) * 1.8 + 32
    print("The temperature in Fahrenheit is", f)
  
  elif convert == "fc":
    fc = input("What is the temperature in Fahrenheit? ")
    c = (float(fc) - 32) * 5/9
    print("The temperature in Celsius is", c)

  elif convert == "end":
    print("Ending program")
    time.sleep(2)
    print("Goodbye")
    time.sleep(0.5)
    running = 0
  
  else:
    print("Invalid Command")
    