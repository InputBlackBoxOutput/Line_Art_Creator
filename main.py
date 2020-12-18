# Line Art Creator: Convert images to line art using openCV
#
# @file  : main.py
# @brief : Provides entrypoint
# @author: Rutuparn Pawar <InputBlackBoxOutput>
# @date_created : 18 Dec 2020 

import os, sys, argparse
import cv2
import edges
import thinner
import segmenter

#------------------------------------------------------------------------------------------------
parser = argparse.ArgumentParser(description='Extracts edges from an image')
parser.add_argument("-img", type=str, help="extract edges from this image", default=None)
parser.add_argument("-alpha", type=int, help="use if very few or no edges detected [Accepts values from 0 to 200]", default=60)
parser.add_argument("-colour", type=bool, help="add colour to the lines", default=False)
parser.add_argument("-k", type=int, help="number of cluster to find while segmenting the image (Use only when colour option is defined)", default=5)
args = parser.parse_args()

#------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	# img = cv2.imread("images/cat.jpg")
	# e = edges.detectEdges(img, alpha=40)
	# t = thinner.thinEdges(e)
	# print("Processing please wait ...")
	# segmenter.colouredEdges(img, t, k=5, show=True)

	if args.img != None:
		print("Processing please wait ... ", end="")
		image = cv2.imread(args.img)
		e = edges.detectEdges(image, args.alpha)
		
		if args.colour:	
			t = thinner.thinEdges(e)
			segmenter.colouredEdges(image, t, k=args.k, show=True)

		else:
			thinner.thinEdges(e, show=True)
		print("Done")

	else:
		print("Please provide an image using the -img option")
		sys.exit()

#------------------------------------------------------------------------------------------------
	# EOF