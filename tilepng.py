import sys
import cv2
import numpy as np

infile = sys.argv[1]  # Use sys.argv[1] to get the first command line argument
outfile = infile + "_tiled_shifted.png"

# Read the input image
img = cv2.imread(infile)

# Check if the image has an alpha channel (4 channels)
if img.shape[2] == 4:
    # Convert to BGR by dropping the alpha channel
    img = img[:, :, :3]

# Calculate the new size
new_width = int(img.shape[1] * 0.25)
new_height = int(img.shape[0] * 0.25)
img = cv2.resize(img, (new_width, new_height))
# Tile the image
vertical_repetitions = 15
horizontal_repetitions = 5
#vertical_repetitions = 3
#horizontal_repetitions = 3
imgTiled = np.tile(img, (vertical_repetitions, horizontal_repetitions, 1))

imgHeight, imgWidth = img.shape[:2]
# Parameters for shifting
shift_step = int(0.3333*imgWidth)  # Number of pixels to shift each successive row
# Apply horizontal shift
for i in range(vertical_repetitions):
    row_shift = i * shift_step  # Calculate shift for the current row
    vertStart = i*imgHeight
    vertEnd = vertStart + imgHeight
    imgTiled[vertStart:vertEnd, :, :] = np.roll(imgTiled[vertStart:vertEnd, :, :], row_shift, axis=1)

# Write the tiled and shifted image to a file
cv2.imwrite(outfile, imgTiled)
