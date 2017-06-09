# Standard imports
import cv2
import numpy as np

# Read images
src = cv2.imread("../data/airplane.jpg")
dst = cv2.imread("../data/sky.jpg")


# Create a rough mask around the airplane.
src_mask = np.zeros(src.shape, src.dtype)
poly = np.array([ [4,80], [30,54], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
cv2.fillPoly(src_mask, [poly], (255, 255, 255))

cv2.imshow('masked', src & src_mask)

# This is where the CENTER of the airplane will be placed
center = (800,100)

# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)

# Save result
cv2.imwrite("./opencv-seamless-cloning-example.jpg", output);
cv2.imshow('synthesized', output)
cv2.waitKey(0)
cv2.destroyAllWindows()