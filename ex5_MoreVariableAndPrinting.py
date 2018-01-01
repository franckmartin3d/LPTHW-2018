#franck 31/12/2017
# Exercise 5 More Variables and printing

my_name = 'Franck martin'
my_age = 33
my_height = 190 #cm
my_weight = 190 #lbs
my_eyes = "brown"
my_teeth = 'white'
my_hair = "brown"

print "lets talk about %s." % my_name
print "he's %d cm tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually hes fat"
print "Hes got %s eyes and %s Hair." % (my_eyes, my_hair)
print "his teeth are usually %s" % my_teeth

#this line is tricky, try to get it exactly right
print " If i add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight)
