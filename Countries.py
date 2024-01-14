countries_dict = {"France": "Paris", 
                  "Portugal": "Lisbon", 
                  "Spain": "Madrid", 
                  "Italy": "Rome", 
                  "Germany": "Berlin",
                  "Greece": "Athens", 
                  "UK": "London", 
                  "Mexico": "Mexico city", 
                  "Brazil": "Brasilia", 
                  "Turkiye": "Ankara", 
                  "Netherlands": "Amsterdam"}
print("Type in cmds to see the commands")

def print_fancy_dict(dictionary):
    for key, value in dictionary.items():
      if type(dictionary[key]) == dict:
        print(f"{key}:")
        for key1, value1 in dictionary[key].items():
          print(f"{key1}: {value1}")
        print("-"*40)
      else:
        print(f"{key}: {value}")
        print("-"*40)
running = True
while running:
  commands = input("/")
  
  if commands == "cmds":
    print("/country")
    print("/all")
    print("/add")
    print("/delete")
    print("/exit")
    continue
  
  elif commands == "country":
    country = input("Which country do you want to look? ")
    
    if country not in countries_dict.keys():
      print("Your country is not stored and will not be saved. But you can add it by typing add.")
      continue
    else:
     print(f"Capital of {country} is {countries_dict[country]}")
     continue

  elif commands == "all":
    print_fancy_dict(countries_dict)
    continue

  elif commands == "delete":
    delete = input("which country do u want to delete: ")
    del countries_dict[delete]
    continue

  elif commands == "add":
    adding_key = input("Which country do you want to add? ")
    adding_value = input(f"What is the capital of {adding_key}? ")

    countries_dict[adding_key] = adding_value
    continue

  elif commands == "exit":
    running = False
print("This is how it looks")
print()
print_fancy_dict(countries_dict)