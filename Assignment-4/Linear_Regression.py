import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Step a: Load the dataset
file_path = "C:/Users/aures/OneDrive/Documents/College Docs/Neural Networks & Deep Learning/Programming_Assignments/Neural_Networks/Assignment-4/Salary_Data.csv"  # Update this path
df_salary = pd.read_csv(file_path)

# Step b: Split the data into training and testing sets
X = df_salary.iloc[:, :-1].values  # Assuming the independent variable is the first column
y = df_salary.iloc[:, 1].values  # Assuming the dependent variable (Salary) is the second column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

# Step c: Train the Linear Regression model on the training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Step d: Predict the Test set results
y_pred = regressor.predict(X_test)

# Step e: Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Step f: Visualize both train and test data using scatter plot
plt.scatter(X_train, y_train, color='blue', label='Training data')
plt.scatter(X_test, y_test, color='red', label='Test data')
plt.plot(X_test, y_pred, color='black', label='Prediction')
plt.title('Salary vs. Experience (Training and Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()
