# import the necessary packages
import imutils
import argparse
import time
import cv2
import numpy as np

def pyramid(image, scale=1.5, minSize=(30, 30)):
	# yield the original image
	yield image
	# keep looping over the pyramid
	while True:
		# compute the new dimensions of the image and resize it
		w = int(image.shape[1] / scale)
		image = imutils.resize(image, width=w)
		# if the resized image does not meet the supplied minimum
		# size, then stop constructing the pyramid
		if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
			break
		# yield the next image in the pyramid
		yield image


def sliding_window(image, stepSize, windowSize):
	# slide a window across the image
	for y in range(0, image.shape[0], stepSize):
		for x in range(0, image.shape[1], stepSize):
			# yield the current window
			yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])

def main():
	
	image = cv2.imread("C_1.png")
	

	scale_percent = 60 # percent of original size
	width = int(image.shape[1] * scale_percent / 500)
	height = int(image.shape[0] * scale_percent / 500)
	dim = (width, height)
	# resize image
	image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)


	(winW, winH) = (28, 28)



	# loop over the image pyramid
	for resized in pyramid(image, scale=1.5):
		# loop over the sliding window for each layer of the pyramid
		for (x, y, window) in sliding_window(resized, stepSize=1, windowSize=(winW, winH)):
			# if the window does not meet our desired window size, ignore it
			if window.shape[0] != winH or window.shape[1] != winW:
				continue
			copy = window
			copy = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)
			cv2.imshow('gray', copy)
			# THIS IS WHERE YOU WOULD PROCESS YOUR WINDOW, SUCH AS APPLYING A
			# MACHINE LEARNING CLASSIFIER TO CLASSIFY THE CONTENTS OF THE
			# WINDOW
			copy_Data = copy.astype(np.float32) / 255
			copy_Data = copy_Data.reshape((1, 28, 28, 1))
			print(copy_Data.shape)
			# since we do not have a classifier, we'll just draw the window
			clone = resized.copy()
			cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 1)
			cv2.imshow("Window", clone)
			cv2.waitKey(1)
			time.sleep(0.025)


main()