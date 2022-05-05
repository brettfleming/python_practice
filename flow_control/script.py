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

credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")

if not (credits >= 120) and not (gpa >= 2.0):
  print("You do not meet either requirement to graduate!")


credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")


grade = 86

if grade >= 90:
  print('A')
elif grade >= 80:
  print('B')
elif grade >= 70:
  print('C')
elif grade >= 60:
  print('D')
else:
  print('F')


print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19
 
print("Your weight:", weight)