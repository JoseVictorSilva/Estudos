import cv2
import numpy as np

# Generate a random bit image of size 28x28
bit_image = np.random.randint(0, 2, (28, 28))

# Convert the bit image to a grayscale image
image = bit_image.astype(np.uint8) * 255

# Define the 3x3 averaging filter
# Define the 1D filter for the horizontal direction
filter_h = np.array([1/4, 1/2, 1/4], dtype=np.float32)

# Define the 1D filter for the vertical direction
filter_v = np.array([[1/4], [1/2], [1/4]], dtype=np.float32)

# Compute the 2D filter by multiplying the two 1D filters
filter_2d = np.matmul(filter_v, filter_h.reshape(1, -1))

# Apply the filter to the image using convolution
blurred_image = cv2.filter2D(image, -1, filter_2d)

# Display the original and blurred images
cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred_image)
cv2.waitKey(0)