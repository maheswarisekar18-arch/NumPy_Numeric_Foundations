import numpy as np

data = np.array([[22.5, 19.0, 31.2, 28.7, 25.1],
                 [17.3, 22.8, 30.5, 26.4, 21.9],
                 [33.1, 29.6, 18.4, 24.0, 27.8],
                 [20.2, 23.5, 31.9, 28.1, 22.6]])
shape_data = data.shape
print("Shape of the data:", shape_data)

mean_row = np.mean(data, axis=1)
print("Mean of each row:", mean_row)
print("Values greater than 28.0:", data[data>28.0])
# Task 3: Normalize the entire data array to the range [0, 1] using the formula below and print the result rounded to 2 decimal places:

normalized = (data - data.min()) / (data.max() - data.min())
normalized_data = np.round(normalized, 2)
print("Normalized data:\n", normalized_data)