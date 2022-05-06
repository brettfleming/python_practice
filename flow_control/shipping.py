weight = 8.4
premium_ground = 125
#Ground Shipping
if weight <= 2:
  cost = weight * 1.5 + 20
  print('cost of regular ground shipping:')
  print(cost)
elif weight <= 6:
  cost = weight * 3 + 20
  print('cost of regular ground shipping:')
  print(cost)
elif weight <= 10:
  cost = weight * 4 + 20
  print('cost of regular ground shipping:')
  print(cost)
else:
  cost = weight * 4.75 + 20 
  print('cost of regular ground shipping:')
  print(cost)

  
print('cost of premium ground shipping:')
print(premium_ground)