# Question: Using NumPy create random vector of size 20 having only float in the range 1-20.  
# • Then reshape the array to 4 by 5 
# • Then replace the max in each row by 0 (axis=1) 


import numpy as np
# Creating a vector of size '20'of float values with range between 1 to 20
random_vector = np.random.uniform(1,20,20)
# Shaping the array using reshape() function to 4 by 5 matrix
reshaped_array = random_vector.copy().reshape(4,5)
# Getting the indices of maximum value in each row
max_indices = reshaped_array.argmax(axis=1)
# Making the max values in each row to zero
reshaped_array[np.arange(reshaped_array.shape[0]),max_indices] = 0

print("Original Vector Array: \n")
print(random_vector)
print("\nReshaped Array with 0 replacing the max in each row: \n")
print(reshaped_array)



