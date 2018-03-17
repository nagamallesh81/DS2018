# Making number variable ready for operations
my_number_1 = 10
my_number_2 = 20
my_number_3 = 30.5
my_number_4 = 40L
# Operations on other types like Text,Tuple,Dictionary will be provided in next examples

# Addition
print my_number_1 + my_number_2

# Substraction
print my_number_1 - my_number_2
print my_number_3 - my_number_4
print my_number_4 - my_number_2

# Multiply / product of
print my_number_2 * my_number_1

# Reminder
print my_number_1 % my_number_2
print my_number_2 % my_number_1

# Divide or quotient of
print my_number_3 / my_number_2

# Divide or quotient of
print "divmod", divmod (my_number_3, my_number_2) #Returns dividend, modulus


# Divide with floor
print my_number_3 // my_number_2

# X Power of y
print my_number_2 * 4
print pow(my_number_2,4) # same as above

# use bases to order operations
# number 1 and 3 will be added ,later sum of it will be divided by number 2
print (my_number_1 + my_number_3) / my_number_2

my_number_2 = -my_number_2  # change value to negative [negative of negative is positive]
print my_number_2

print abs(my_number_3)
print int(my_number_3)
print float(my_number_3)
print long(my_number_3)
print complex(my_number_3,12)
