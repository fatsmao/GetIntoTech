import getpass

'''
while True:
    pin = input("Please enter your pin...")
    if pin == 1997:
        print("You have entered the correct pin")
        break
    else:
        print("You have entered the incorrect pin, please try again")
'''

#For loop is used when you know how many times you want to repeat a piece of code

pin = 1997
for i in range (3, 0, -1):
  #supplied_pin = int(input("Please enter your pin (you have three attempts): "))
  supplied_pin = int(getpass.getpass(prompt="Please enter your pin (you have three attempts): "))
  if supplied_pin == pin:
      print("Pin was correct!")
      break
  else:
      print("Incorrect pin, please try again!")
if i == 1:
    print("You have been denied access")
