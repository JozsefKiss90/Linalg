import numpy as np

v = np.array([2, 4, 6, 8, 10])

# Create a vector of ones of the same length as v
ones_vector = np.ones(len(v))

# Compute the dot product of v and the ones vector
dot_product = np.dot(v, ones_vector)

# Compute the average
average = dot_product / len(v)

print(average)

# Define a vector v containing some numbers
v1 = np.array([2, 4, 6, 8, 10])

# Define a weight vector w corresponding to each number in v
w = np.array([1, 2, 3, 4, 5])  # Example weights

# Compute the weighted sum using dot product
weighted_sum = np.dot(v1, w)

# Compute the sum of weights
sum_of_weights = np.sum(w)

# Compute the weighted mean
weighted_mean = weighted_sum / sum_of_weights

wAve = np.dot(v1, w/sum(w))

print(weighted_mean)
print(wAve)
