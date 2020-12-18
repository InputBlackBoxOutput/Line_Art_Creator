# Line Art Creator: Convert images to line art using openCV
#
# @file  : edges.py
# @brief : Performs edge extraction 
# @author: Rutuparn Pawar <InputBlackBoxOutput>
# @date_created : 12 Aug 2020 

#--------------------------------------------------------------------------------------
import sys
# try:
import cv2
import numpy as np
import utils
# except ImportError:
#     print('Modules required by edges.py not found')
#     print('Use pip install -r requirements.txt to install modules')
#     sys.exit()

#------------------------------------------------------------------------------------------------
def detectEdges(imgFile, alpha=60, isFile=False, show=False, download=False):
	if isFile == True:
		print(f"Extracting edges from: {imgFile}")
		img = cv2.imread(imgFile)
	else:
		img = imgFile

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
	edges = cv2.Canny(bilateral, alpha, alpha+60, L2gradient=False)

	if show == True:
		utils.showImage(gray, "Grayscale image")
		utils.showImage(gaussian, "Gaussian Blur")
		utils.showImage(median, "Median Blur")
		utils.showImage(bilateral, "Bilateral filtered image")
		utils.showImage(edges, "Edges")

	if download == True:
		utils.downloadImage(edges, f"{imgFile.split('.')[0]}_edges.png")

	return edges
#------------------------------------------------------------------------------------------------
# EOF