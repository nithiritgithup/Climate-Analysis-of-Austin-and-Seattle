import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
austin_data = pd.read_csv('austin_weather.csv')
seattle_data = pd.read_csv('seattle_weather.csv')

# Convert date columns to datetime
austin_data['Date'] = pd.to_datetime(austin_data['Date'])
seattle_data['Date'] = pd.to_datetime(seattle_data['Date'])

# Set date as index
austin_data.set_index('Date', inplace=True)
seattle_data.set_index('Date', inplace=True)

# Plotting time series data
plt.figure(figsize=(14, 7))

# Temperature trends
plt.subplot(2, 2, 1)
plt.plot(austin_data.index, austin_data['Temperature'], label='Austin')
plt.plot(seattle_data.index, seattle_data['Temperature'], label='Seattle', color='orange')
plt.title('Temperature Trends')
plt.xlabel('Date')
plt.ylabel('Temperature (°F)')
plt.legend()

# Humidity trends
plt.subplot(2, 2, 2)
plt.plot(austin_data.index, austin_data['Humidity'], label='Austin')
plt.plot(seattle_data.index, seattle_data['Humidity'], label='Seattle', color='orange')
plt.title('Humidity Trends')
plt.xlabel('Date')
plt.ylabel('Humidity (%)')
plt.legend()

# Bar charts: Monthly averages
austin_monthly_avg = austin_data.resample('ME').mean()
seattle_monthly_avg = seattle_data.resample('ME').mean()

plt.subplot(2, 2, 3)
austin_monthly_avg['Temperature'].plot(kind='bar', label='Austin', alpha=0.7)
seattle_monthly_avg['Temperature'].plot(kind='bar', label='Seattle', alpha=0.7)
plt.title('Monthly Average Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°F)')
plt.legend()

# Histograms: Temperature distribution
plt.subplot(2, 2, 4)
plt.hist(austin_data['Temperature'], bins=30, alpha=0.5, label='Austin')
plt.hist(seattle_data['Temperature'], bins=30, alpha=0.5, label='Seattle')
plt.title('Temperature Distribution')
plt.xlabel('Temperature (°F)')
plt.ylabel('Frequency')
plt.legend()

plt.tight_layout()
plt.show()

# Scatter plot: Temperature vs. Humidity
plt.figure(figsize=(10, 5))
plt.scatter(austin_data['Temperature'], austin_data['Humidity'], label='Austin', alpha=0.5)
plt.scatter(seattle_data['Temperature'], seattle_data['Humidity'], label='Seattle', alpha=0.5, color='orange')
plt.title('Temperature vs. Humidity')
plt.xlabel('Temperature (°F)')
plt.ylabel('Humidity (%)')
plt.legend()
plt.show()

# Create a combined DataFrame for boxplot
combined_data = pd.DataFrame({
    'Temperature': pd.concat([austin_data['Temperature'], seattle_data['Temperature']]),
    'City': ['Austin'] * len(austin_data) + ['Seattle'] * len(seattle_data)
})

# Statistical Plot: Box plots for temperature
plt.figure(figsize=(10, 5))
sns.boxplot(x='City', y='Temperature', data=combined_data)
plt.title('Box Plot of Temperature')
plt.ylabel('Temperature (°F)')
plt.show()
