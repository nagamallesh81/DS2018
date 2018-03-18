# Making variable ready for operations
my_number_1 = 10
my_number_2 = 20
my_number_3 = 30

# Less Than
print "<:", my_number_1 < my_number_2

# Less Than or equal
print "<=:", my_number_1 <= my_number_1

# Greater Than
print ">:", my_number_1 > my_number_2

# Greater Than or equal
print ">=:", my_number_1 >= my_number_2

# Equal To
print "==", my_number_1 == my_number_2

# Not Equal To
print "!=", my_number_1 != my_number_2
print "<>", my_number_1 <> my_number_2

# is - can be used for objects
print "Number is Integer:", my_number_1 is my_number_2

# is not- can be used for objects
print "Number is not Integer:", my_number_1 is not my_number_2

# more than one operator is executed in Left to Right order
# Below example first condition is false, hence not evaluated second one
print my_number_3 < my_number_1 <= my_number_2

# Below example first condition is true, second one is false
print my_number_1 < my_number_3 <= my_number_2

# Below example first condition is true, second one is also true
print my_number_1 < my_number_2 <= my_number_3
