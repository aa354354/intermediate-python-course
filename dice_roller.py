import random
repeat="Y"
while repeat == "Y":
   print("Rolling the dice")
   print(random.randint(1,6))

repeat =input("Do you wanna roll again Y/N?")
if repeat=="Y":
    continue