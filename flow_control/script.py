example_statement = "No"

statement_one = "Yes"

statement_two = "Yes"

statement_three = "No"

statement_four = "No"


#(5 * 2) - 1 == 8 + 1
statement_one = True
#13 - 6 != (3 * 2) + 1
statement_two = False
#3 * (2 - 1) == 4 - 1
statement_three = True

#not a boolean value
#must be capitalized and not in qoutes
my_baby_bool = 'true'

print(type(my_baby_bool)) #returns str 
#this is a boolean
my_baby_bool_two = True

print(type(my_baby_bool_two)) #returns bool 


# Enter a user name here, make sure to make it a string
user_name = 'angela_catlady_87'

if user_name == "Dave":
  print("Get off my computer Dave!")

if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")