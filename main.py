user_in = input("How many dollars: ")
try:
  val = int(user_in)
  print("Yes, input is an Integer.")
  print("Input value is: ", val)
except ValueError:
  print("That's not an integer!")

user_name = input("What is your first name: ")
try:
  name = str(user_name)
  print("What a nice name.")
  print("It is nice to meet you", name)
except ValueError:
  print("That doesn't sound like a name.")

user_num = input("Enter your speed: ")
try:
  val = int(user_num)
  if(val > 0):
    print("User speed is positive.")
  else:
    print("You can't go negative speed!?")
except ValueError:
  print("No... input is not a number.")