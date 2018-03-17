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

#String
#Can use single or double quotes ' or ""
#triple quoted for continue across lines or statements
my_dynamic_var = 'Naga'
print "my_dynamic_var:",my_dynamic_var

my_dynamic_var = "Mallesh"
print "my_dynamic_var:",my_dynamic_var

my_dynamic_var = """    Thanks
                    -------
                    Naga Mallesh"""
print "my_dynamic_var:",my_dynamic_var

#List - collection of different types: use rectangular braces []
# value can be blank
my_dynamic_var=[]
print "my_dynamic_var:",my_dynamic_var

my_dynamic_var=['phone number',123456789,"India"]
print "Length of list:",len(my_dynamic_var)
print my_dynamic_var[0],":",my_dynamic_var[1]
print my_dynamic_var[0:2] #return 2 elements from 0 [0 is first index]
my_dynamic_var[1]="Number out of coverage" # Update value in list
print my_dynamic_var[0],":",my_dynamic_var[1]

#Tuple - like list but fixed size : Use ( )
#Tuple immutable (can't change, remove, add) and static (use for constant operations and don't want to change data)
#Index starting at 0
my_tuple=() #Empty tuple
my_tuple=(1,) #Single value - make sure have comma
my_tuple=(1,2,1,2)
my_tuple=1,2,1,2
my_tuple=(1,2.0,"Mallesh",False,True)
print my_tuple[0:3] #return 3 elements from 0 [0 is first index]

#Dictionary : Use flower or curly braces { }
#Like Maps in Java, having Key value pairs
#Faster access via key
my_data={"name":"Naga Mallesh","Ph No":"123456789"}
print my_data["name"]
print my_data.keys() #returns keys
print my_data.has_key("name")
print 'name' in my_data # in checks key only
print 'Naga Mallesh' in my_data #in dont check values






