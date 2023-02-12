import cv2
import numpy as np

# Load the image
img = cv2.imread("red.png")

# Convert the image from BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define a range of color in HSV to detect the traffic cones
lower_color = np.array([0, 200, 140])
upper_color = np.array([160, 255, 230])

# Threshold the HSV image to only get the traffic cones
mask = cv2.inRange(hsv, lower_color, upper_color)

# Find contours in the masked image
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Loop through the contours and find all the cones
cones = []
for c in contours:
    # Get the moment of the contour
    M = cv2.moments(c)
    
    # Compute the center of the contour
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        cones.append((cx, cy))

# Convert the cones list to a numpy array
cones = np.array(cones)

# Split the cones list into 2 lists containing the cones on the left and right
left_cones = []
right_cones = []
for cx, cy in cones:
    if cx < img.shape[1] / 2:
        left_cones.append([cx, cy])
    else:
        right_cones.append([cx, cy])

# Fit a line to the left cones
if len(left_cones) > 0:
    left_cones = np.array(left_cones)
    vx, vy, x, y = cv2.fitLine(left_cones, cv2.DIST_L2, 0, 0.01, 0.01)
    rows, cols = img.shape[:2]
    lefty = int((-x * vy / vx) + y)
    righty = int(((cols - x) * vy / vx) + y)
    cv2.line(img, (cols - 1, righty), (0, lefty), (0, 0, 255), 2)

# Fit a line to the right cones
if len(right_cones) > 0:
    right_cones = np.array(right_cones)
    vx, vy, x, y = cv2.fitLine(right_cones, cv2.DIST_L2, 0, 0.01, 0.01)
    rows, cols = img.shape[:2]
    lefty = int((-x * vy / vx) + y)
    righty = int(((cols - x) * vy / vx) + y)
    cv2.line(img, (cols - 1, righty), (0, lefty), (0, 0, 255), 2)

# Write the image
cv2.imwrite("answer.png", img) 