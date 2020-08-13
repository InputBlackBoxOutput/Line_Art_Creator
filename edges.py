# Line Art Creator: Convert images to line art using openCV
#
# @file  : edges.py
# @brief : Provides edge extraction 
# @author: Rutuparn Pawar <InputBlackBoxOutput>
# @date_created : 12 Aug 2020 

#--------------------------------------------------------------------------------------
import sys
try:
	import os
	import argparse
	import cv2
	import numpy as np
	from matplotlib import pyplot as plt
	import thinner
except ImportError:
    print('Modules required by edges.py not found')
    print('Use pip install -r requirements.txt to install modules')
    sys.exit()

#------------------------------------------------------------------------------------------------
parser = argparse.ArgumentParser(description='Extracts edges from an image')
parser.add_argument("-img", help="extract edges from this image")
args = parser.parse_args()

#------------------------------------------------------------------------------------------------
def downloadImage(img, imgName="edges.png"):
	plt.plot(), plt.imshow(img, cmap="gray") 
	plt.title("Edges"), plt.xticks([]), plt.yticks([])
	plt.axes("off")
	plt.savefig(imgName)

def showImage(img, title="title"):
	plt.plot(), plt.imshow(img, cmap="gray") 
	plt.title(title), plt.xticks([]), plt.yticks([])
	plt.show()
		
#------------------------------------------------------------------------------------------------
def detectEdges(imgFile, show=False, download=False):
	print(f"Extracting edges from: {imgFile}")
	img = cv2.imread(imgFile)
	
	# Preprocessing image
	try:	
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		gaussian = cv2.GaussianBlur( gray,(5,5),0)
		median = cv2.medianBlur(gaussian, 3)
		bilateral = cv2.bilateralFilter(median, 7, 50, 50)
	except:
		print("Something went wrong!")
		sys.exit()

	# edges = cv2.Canny(bilateral, 60, 120, L2gradient=True)
	edges = cv2.Canny(bilateral, 60, 120, L2gradient=False)

	if show:
		showImage(img, "Original image")
		showImage(gaussian, "Gaussian Blur")
		showImage(median, "Median Blur")
		showImage(bilateral, "Bilateral filtered image")
		showImage(edges, "Edges")

	if download:
		downloadImage(edges, f"{imgFile.split('.')[0]}_edges.png")

	return edges

#------------------------------------------------------------------------------------------------
if __name__ == "__main__":
	# showImage(cv2.imread("images/cat.jpg"), "Original")
	thinner.thinEdges(detectEdges(f"images/{args.img}"), show=True)
	

	# detectEdges("images/cat.jpg", show=True)
	

	# for each in os.listDir("images"):
	#   edges = detectEdges(f"images/{each}")
	#   thinEdges(edges)

#------------------------------------------------------------------------------------------------
# EOF