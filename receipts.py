#the point of this prject is to display the customers receipt to the console

#this is the first item that the customer can buy and its discription
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
#price of the loveseat
lovely_loveseat_price = 254.00
#second item that customer can buy
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
#sette price 
stylish_settee_price = 180.50

#the last item that customer can buy
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
#the lamps price
luxurious_lamp_price = 52.15
#sales tax perectage
sales_tax = .088
#the starting total which should always be zero
customer_one_total = 0

customer_one_itemization = ""

customer_one_total += lovely_loveseat_price

customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price

customer_one_itemization += luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax


print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)