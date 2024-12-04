def my_zip(customer_names, customer_ids, shopping_points, strct=True):
    if strct:
       
        if len(customer_names) == len(customer_ids) == len(shopping_points):
            return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
        else:
            return []
    else:
        
        min_length = min(len(customer_names), len(customer_ids), len(shopping_points))
        return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(min_length)]


customer_names = ['John', 'Don', 'Motu','Patlu']
customer_ids = [101, 102, 103,]
shopping_points = [150, 200, 250]

print(my_zip(customer_names, customer_ids, shopping_points, strct=True))  
print(my_zip(customer_names, customer_ids, shopping_points, strct=False))

  
  