# more standard libraries at https://docs.python.org/2.7/library/

import sys
import datetime

# Python sets the variable type based on the value that is assigned to it. Unlike more riggers languages
# Python will change the variable type if the variable value is set to another value.

# Python has 5 standard data types
# Numbers, String, List, Tuple, Dictionary

#Numbers
#int	 	 	a = 10	 	 	Signed Integer
#long	 	 	a = 345L	 	 	(L) Long integers, they can also be represented in octal and hexadecimal
#float	 	 	a = 45.67	 	 	(.) Floating point real values
#complex	 	 	a = 3.14J	 	 	(J) Contains integer in the range 0 to 255.
my_int = 2 #int signed integer
my_long = 20L #long integers - can use Octal and hexa
my_float = 3.14 #floating real values with decimal
my_complex = 1.2J #J contains integer range from 0 to 255

my_dynamic_var = 2

# Compile time errors are less, it will not check for types, names of functions until it run.
print "my_dynamic_var:",my_dynamic_var

my_var = 'Mallesh'
print "my_dynamic_var:",my_dynamic_var
