import pandas as pd
import matplotlib.pyplot as plt

file_path = "C:/Users/aures/OneDrive/Documents/College Docs/Neural Networks & Deep Learning/Programming_Assignments/Neural_Networks/Assignment-4/data.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Show basic statistical description about the data
print("Statistical Description of the Data:")
print(df.describe())

# Check for null values and replace them with the mean of their respective column
df.fillna(df.mean(), inplace=True)

# Convert the datatype of Calories column to int after replacing null values
df['Calories'] = df['Calories'].astype(int)

# Aggregate selected columns
aggregated_data = df[['Duration', 'Calories']].agg(['min', 'max', 'count', 'mean'])

# Filter the DataFrame for specific conditions
filter1 = df[(df['Calories'] >= 500) & (df['Calories'] <= 1000)]
filter2 = df[(df['Calories'] > 500) & (df['Pulse'] < 100)]

# Create a modified DataFrame without the "Maxpulse" column
df_modified = df.drop(columns=['Maxpulse'])

# Delete the "Maxpulse" column from the main DataFrame
df.drop(columns=['Maxpulse'], inplace=True)

# Creating a scatter plot for Duration vs Calories
plt.figure(figsize=(10, 6))
plt.scatter(df['Duration'], df['Calories'], color='blue', alpha=0.5)
plt.title('Scatter Plot of Duration vs Calories')
plt.xlabel('Duration (minutes)')
plt.ylabel('Calories Burned')
plt.show()
