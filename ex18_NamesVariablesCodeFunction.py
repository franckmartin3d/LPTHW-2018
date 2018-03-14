# Franck Martin
#1/03/2018

#function do 3 things
# 1 they name piece of code the way variables names strings and numbers.
# 2 they take arghuments the way your scripts take argv
# 3 Using 1 and 2 they let you make your own "mini scripts" or tiny commands."

#This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1} , arg2: {arg2}"):
#ok , that *args is actually pointless, we can just do this

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1} , arg2: {arg2}")

print_two("Zed", "shaw")
print_two_again("Zed2","shaw2")
