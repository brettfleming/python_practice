weight = 5
#Ground Shipping
if weight <= 2:
  cost = weight * 1.5 + 20
  print(cost)
elif weight <= 6:
  cost = weight * 3 + 20
  print(cost)
elif weight <= 10:
  cost = weight * 4 + 20
  print(cost)
else:
  cost = weight * 4.75 + 20 
  print(cost)