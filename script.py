my_name = "Brett"
my_last_name ='flemingo'
age = 24
hometown = 'Red Wing'
print("Hello and welcome " + my_name + "!")
print('Hello my name is' + my_name + my_last_name)
print('I am ' + age + 'years old')
print('I am from' + hometown)


#This is my first python comment lets Go!!!
#to comment in python you use the # symbol instead of the // like in javascript


# in python you use print instead of console.log() from javascript
print("Hello World!")
# strings can be made with either "" or ''
print('Brett')

#variables dont need to be declared with the word const or let like in javascript
# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
meal =  "sandwhich"

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner
meal = 'pasta'
# Printing out dinner
print("Dinner:")
print(meal)

# the line below with throw a syntaxerror 
#print('This message has mismatched quote marks!")

#its a simple fix just match the qoutes so making both qoutes double qoutes will fix the error and vise versa
print("This message has mismatched quote marks!")

#the line below with throw a nameError because it is loooking for a varible named Abracadabra but it doesnt exist
#print(Abracadabra)

# there are two ways to fix this add qoutes around the word or make a varible above to match the name
print("Abracadabra")

#Numbers in python can be either integers or floats

# An int or integer is a whole number that can be postive or negative (-20, 5, 1098, and 0)
release_year = 2013
runtime = 2
# A float is a number with decimals on the end (so 1.2, -20.5, 100.32354)
rating_out_of_10 = 7.8

# calculations in python are just like regular math they also fallow order of operations 
print(25 * 68 + 13 / 28)