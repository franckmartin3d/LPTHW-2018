#franck 20/03/2018
# while loop

i = 0
numbers = []

while i < 6:
    print(f"at the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("numbers now: ", numbers)
    print(f"at the bottom i is {i}")

print("The numbers:")

for num in numbers:
    print(num)


