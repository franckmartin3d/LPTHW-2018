#franck 20/03/2018
#Branche and functions

from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("man, learn to type a number.")

    if how_much < 50:
        print("Nice, youre not greedy, you win!")
        exit(0)
    else:
        dead("your a greedy bastard")

def bear_room():
    print("there is a bear here")
    print("the bear has a bunch of honey.")
    print("the fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = false

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you, and then slap your face off")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go trought it now")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("the bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulthu_room():
    print("Here you see the great evil cthulu.")
    print("He, it , whatever stares at you and you go insane.")
    print("Do you flee for you life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head in choice":
        dead("well that was tasty!!!!")
    else:
        cthulthu_room()

def dead(why):
    print(why, "good job!")
    exit(0)

def start():
    print("You are in a dark room")
    print("There is a door to your right and left.")
    print("what door do you open?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulthu_room()
    else:
        dead("you stumble around the room and starve")

start()


