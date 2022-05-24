heights = [61, 70, 67, 64, 65]

#broken_heights = [65 71 59 62]
broken_heights = [65, 71, 59, 62] #adding the commas is what fixes the errors

#in python lists can have multipule data types in them at once
ints_and_strings = [1, 2, 3, "four", "five", "six"]

sam_height_and_testscore = ["Sam", 67, 85.5, True]

#lists can be empty to start 
my_empty_list = []


example_list = [1, 2, 3, 4]

#Using Append
example_list.append(5)
# print(example_list)

#Using Remove
example_list.remove(5)
# print(example_list)


orders = ["daisies", "periwinkle"]
#print(orders)

orders.append('tulips')
#print(orders)

orders.append('roses')
#print(orders)



orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]
new_orders = ['lilac', 'iris']

orders_combined = orders + new_orders

#broken_prices = [5, 3, 4, 5, 4] + 4
broken_prices = [5, 3, 4, 5, 4] + [4] #adding in []'s is all you need to do to fix the new list


employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

employee_four = employees[3]

print(employees[5])


shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]


last_element = shopping_list[-1] #-1 selects the last element in a list no matter how long the list is
index5_element = shopping_list[5]
print(last_element, index5_element)