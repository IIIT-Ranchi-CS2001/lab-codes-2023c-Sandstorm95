import pandas as pd
import numpy as np

# Load the CSV file
file_path = 'AQI_Data.csv' 
data = pd.read_csv(file_path)

# Display the first 8 rows
print("First 8 rows:")
print(data.head(8))

# Display the last 5 rows
print("\nLast 5 rows:")
print(data.tail(5))

# Show the dtype and number of non-null values in each column
print("\nData types and non-null values:")
data.info()

# Ensure the necessary columns exist in the dataset
columns = ['AQI', 'PM2.5', 'PM10']
if all(column in data.columns for column in columns):
    # Extract columns as NumPy arrays
    aqi = data['AQI'].to_numpy()
    pm25 = data['PM2.5'].to_numpy()
    pm10 = data['PM10'].to_numpy()

    # Calculate statistics using NumPy
    mean_aqi = np.mean(aqi)
    max_pm25 = np.max(pm25)
    min_pm10 = np.min(pm10)

    # Display results
    print("\nOverall Statistics:")
    print(f"Mean AQI: {mean_aqi}")
    print(f"Max PM2.5: {max_pm25}")
    print(f"Min PM10: {min_pm10}")
else:
    print("Required columns ('AQI', 'PM2.5', 'PM10') are missing from the dataset.")
