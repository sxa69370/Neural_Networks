import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
glass_data = pd.read_csv('glass.csv')

# Lets assume last column is the target variable
X = glass_data.iloc[:, :-1]  # Features - all columns but the last
y = glass_data.iloc[:, -1]   # Target variable - the last column

# Splitting the dataset into training and testing parts
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Linear SVM model
model = SVC(kernel='linear', random_state=42)

# Train the model
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred) * 100
classification_report_str = classification_report(y_test, y_pred,zero_division=0)

# Display the evaluation metrics
print("\nAccuracy Score: ", accuracy)
print("\nClassification Report: \n", classification_report_str)
