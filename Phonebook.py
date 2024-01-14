def add(phonebook):
  friend = input("Who do you want to add: ")
  email = input("Whats his/her email(This is not stored): ")
  phone_number = input("Whats his/her phone number: ")
  phonebook[friend] = {"email": email, "phone_number": phone_number}


def delete(phonebook):
  idk = input("Who do you want to delete: ")
  if idk not in phonebook.keys():
    print(
      "You can't delete a person that does not exist in this phonebook, but you can add him/her"
    )
  else:
    del phonebook[idk]


def modify(phonebook):
  person = input("who do you want to modify: ")
  if person not in phonebook:
    print("This person does not exist in this phonebook. You can add him/her.")
    return None

  modify = input("what catagory do you want to modify(email, phone_number): ")
  modify = modify.lower()

  if modify == "email":
    email = input("Whats his/her email(This is not stored): ")
    phonebook[person]["email"] = email

  elif modify == "phone_number":
    phone_number = input("Whats his/her phone_number(This is not stored): ")
    phonebook[person]["phone_number"] = phone_number


def fetch(phonebook):
  printer = input("What will be the files name: ")
  with open(printer + ".txt", 'w') as f:
    for key, value in phonebook.items():
      f.write(key + "\n")
      for key2, value2 in value.items():
        f.write(key2 + ": " + value2 + "\n")
      f.write(40 * "-" + "\n")

print("You can see the commads by typing 'cmds'.")

phonebook = {}

while True:
  cmds = input("/")
  cmds = cmds.lower()
  if cmds == "cmds":
    print(
      "add: Add a person\ndelete: Delete a person\nmodify: Modify a person\nfetch: Create a file and print the phonebook in it\nstop: stops the program\n"
    )
  elif cmds == "add":
    add(phonebook)
  elif cmds == "delete":
    delete(phonebook)
  elif cmds == "modify":
    modify(phonebook)
  elif cmds == "fetch":
    fetch(phonebook)
  elif cmds == "stop":
    break
  else:
    print("Invalid command!")

