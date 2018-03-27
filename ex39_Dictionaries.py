#Franck 21/03/2018
#Dictionaries

# Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigant': 'MI',
}

#create a basic set of states and some cities in them

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('_' * 10)
print("NY State Has: ", cities['NY'])
print("OR State Has: ", cities['OR'])

# print some states
print("_" * 20)
print("michigan abbreviation is: ", states['Michigant'])
print("Florida abbreviation is: ", states['Florida'])

# do it vy using states then cities dictionary
print("_" * 20)
print("Michigan has: ", cities[states['Michigant']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print("_" * 20)
for states, abbrev in list(states.items()):
    print(f"{states} is abbreviates {abbrev}")

# print every city in state
print("_" * 20)
for abbrev, city in list(cities.items()):
    print(f"{abbrev}has the city {city}")

#now do both at same time
print("_" * 20)
for state, abbrev in list(states.items()):
    print(f"{states} state is abbreviated {abbrev}")
    print(f"and as city {cities[abbrev]}")

print("_" * 20)
#safely get a abbreviation by state that might not be there
states = states.get('Texas')
if not states:
    print("sorry, no texas.")

# get a city with a default value
city = cities.get('TX', "does not exist")
print(f"the city for the state 'TX' is : {city}")

