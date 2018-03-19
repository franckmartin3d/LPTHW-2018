#franck 16/03/2018

people = 30
cars = 40
trucks = 15

if cars > people:
    print("we should take cars.")

elif cars < people:
    print("we should not take the cars.")
else:
    print("we cant decide")

if trucks > cars:
    print("Thats too many truck")
elif trucks < cars:
    print("maybe we could take the trucks.")
else:
    print("we still cant decide")

if people > trucks:
    print("Alright, lets just take the truck")
else:
    print("Fine, lets stay home")