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

x = 20
y = 20
if x == y:
  print("These numbers are the same")

credits = 120

if credits >= 120:
  print('You have enough credits to graduate!')


#(2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_one = False
#(4 * 2 <= 8) and (7 - 1 == 6)
statement_two = True

credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")


#(2 - 1 > 3) or (-5 * 2 == -10)
statement_one = True
#(9 + 5 <= 15) or (7 != 4 + 3)
statement_two = True

credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")


#not (4 + 5 <= 9)
statement_one = False
#not (8 * 2) != 20 - 4
statement_two = True