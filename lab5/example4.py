password = "qwerty1234"
index = 0 
chance = 3 

while True : 
  user_password = input("enter a pasword: ")
  if password == user_password : 
    print("welcome")
    break
  elif user_password == "help" : 
    print(password[index])
    index += 1 
    if index == len(password) : 
      print("I already wrote the answer ")
  else : 
    print("wrong")
    chance -= 1
    if chance == 0 :
      break


