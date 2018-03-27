#franck 20/03/2018
#Doing things to list

the_things = "Apple Oranges Crows Telephone Light Sugar"

print("wait there are 10 things in tha list . lets fix that.")

stuff = the_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana" , "Girls", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Lets do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #woah fancy
print(stuff.pop())
print(' '.join(stuff)) #what cool
print("# ".join(stuff[3:5]))

