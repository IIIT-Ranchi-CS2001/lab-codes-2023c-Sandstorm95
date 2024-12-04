import numpy as np

covid_data = np.array([ [1500, 2000, 1800, 1200, 900], # Day 1 
[1600, 2100, 1900, 1300, 950], 	# Day 2 
[1700, 2200, 2000, 1400, 1000], 	# Day 3 
[1650, 2150, 1950, 1350, 980], 	# Day 4 
[1750, 2250, 2050, 1450, 1020], 	# Day 5 
[1800, 2300, 2100, 1500, 1050], 	# Day 6 
[1900, 2400, 2200, 1600, 1100], 	# Day 7 
])

cnt = 0
for i in covid_data:
  for j in covid_data:
    cnt = cnt + 1
print(cnt) 

maxi =  np.max(covid_data)
print(maxi)

