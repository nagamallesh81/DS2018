# Making variable ready for operations
my_string_1 = "naga"
my_string_2 = "mallesh"
my_string_3 = "naga mallesh"
my_string_4 = "my age is 35 only"
my_string_5 = "35"

# Check is it digits
print "get digits:", my_string_4.isdigit()
print "get digits:", my_string_5.isdigit()

print "capitalize ",my_string_1," :",my_string_1.capitalize()

print "Center :",my_string_2.center(40)," :",my_string_2.center(40,'*')

print "count :",my_string_3.count('a')," :",my_string_3.count('a',5,10)

print "ends with ",my_string_1.endswith("ga")," :",my_string_1.endswith("sh")

print "find ",my_string_4.find("age")