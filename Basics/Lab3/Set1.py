
import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('AQI_Data.csv')

# Part a: Count rows for each city
city_counts = data['City'].value_counts().to_dict()  # Replace 'City' with your city column name
print("City counts:", city_counts)

# Part b: Compute pollutant sums and save the updated dataset
pollutant_columns = ['PM2.5', 'PM10', 'NO2', 'CO', 'O3', 'SO2'] 
 # Replace with your pollutant column names
print("Pollutant columns data (first few rows):")
print(data[pollutant_columns].head())  # Display first few rows of pollutant data for verification

# Ensure pollutant columns are numeric
data[pollutant_columns] = data[pollutant_columns].apply(pd.to_numeric, errors='coerce')

# Calculate the sum
data['PollutantSum'] = data[pollutant_columns].sum(axis=1)

print("Pollutant sums :")
print(data[['PollutantSum']].head())  # Display first few rows of the calculated sum

# Save the updated dataset
data.to_csv('pollutant.txt', index=False)
print("Updated dataset saved to 'pollutant.txt'.")


