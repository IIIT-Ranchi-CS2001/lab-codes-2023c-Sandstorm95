import numpy as np


covid_data = np.array([
    [1500, 2000, 1800, 1200, 900],  # Day 1
    [1600, 2100, 1900, 1300, 950],  # Day 2
    [1700, 2200, 2000, 1400, 1000], # Day 3
    [1650, 2150, 1950, 1350, 980],  # Day 4
    [1750, 2250, 2050, 1450, 1020], # Day 5
    [1800, 2300, 2100, 1500, 1050], # Day 6
    [1900, 2400, 2200, 1600, 1100]  # Day 7
])


sumTotal = np.sum(covid_data)

percentages = []
for i in range(covid_data.shape[0]):
    sum_day = np.sum(covid_data[i])
    percent_day = (sum_day / sumTotal) * 100
    percentages.append(percent_day)


print(percentages)
