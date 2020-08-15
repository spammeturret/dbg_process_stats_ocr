# take screenshot of region
# send api with image attached

#receive api msg
#store image in path
#opencv convert to greyscale
#opencv convert to binary with defined threshold
#pytesseract to convert image to text
#script sends text to google sheets
#script deletes image

import numpy as np
import argparse
import cv2

#path = 'C:\\project\\OCR\\anti-cheat\\new2\\2.png'


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

# define the list of boundaries
boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
]

# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")

	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)

	# show the images
	# cv2.imshow("images", np.hstack([image, output]))
    cv2.imshow("images", np.hstack(output))
	cv2.waitKey(0)

# path = 'C:\\project\\OCR\\anti-cheat\\new2\\2.png'

# image = cv2.imread(path)
# grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imwrite('test.png', grey_image)


