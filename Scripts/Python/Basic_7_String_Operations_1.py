# Making variable ready for operations
my_string_1 = "Naga"
my_string_2 = "Mallesh"
my_string_3 = "Naga Mallesh"

# In - True if an item of s is equal to x, else False
print "In:", my_string_1 in my_string_3

# + concatenation
print "+:", my_string_1 + my_string_2

#s*t equivalent to adding s to itself n times
print "*:", my_string_1 * 2

#slice from 0 to 6
print "6 characters from first:", my_string_3[0:6]

#slice from 0 to 6, with step 3
print "6 characters from first, step by 3:", my_string_3[0:6:3]

# Min, Max
print "Min of;", min(my_string_1,my_string_2)
print "Max of:", max(my_string_1,my_string_2)

# Min, Max
try:
    print "Numberic Values :",int(my_string_1[0])
except ValueError:
    print "Conversion Error"