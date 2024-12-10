import numpy as np

# Define your vectors
v1_1 = np.array([0, 1, 3])
v1_2 = np.array([1, 0, 3])
v2_1 = np.array([1, 0.5, 0])
v2_2 = np.array([4, 1, 1])
v3_1 = np.array([1,0,3])
v3_2 = np.array([1,1,3])
# Form matrices A and B
A = np.column_stack((v1_1, v1_2))
B = np.column_stack((v2_1, v2_2))
C = np.column_stack((v3_1, v3_2))
# Define the vector u
u = np.array([4, 1, 12])

# Function to check if u is in the span of a matrix and return coefficients
def span_and_coefficients(matrix, vector):
    coefficients, residuals, _, _ = np.linalg.lstsq(matrix, vector, rcond=None)
    in_span = np.allclose(residuals, 0)
    return in_span, coefficients

# Check if u is in the span of A and B, and get coefficients
in_span_A, coefficients_A = span_and_coefficients(A, u)
in_span_B, coefficients_B = span_and_coefficients(B, u)
in_span_C, coefficients_C = span_and_coefficients(C, u)

print("Is u in the span of A:", in_span_A)
print("Coefficients for A:", coefficients_A if in_span_A else "N/A")

print("Is u in the span of B:", in_span_B)
print("Coefficients for B:", coefficients_B if in_span_B else "N/A")

print("Is u in the span of C:", in_span_C)
print("Coefficients for C:", coefficients_C if in_span_C else "N/A")