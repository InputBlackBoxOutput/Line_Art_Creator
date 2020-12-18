import matplotlib.pyplot as plt

def downloadImage(img, imgName="edges.png"):
	plt.plot(), plt.imshow(img, cmap="gray") 
	plt.title("Edges"), plt.xticks([]), plt.yticks([])
	plt.axes("off")
	plt.savefig(imgName)

def showImage(img, title="title"):
	plt.plot(), plt.imshow(img, cmap="gray") 
	plt.title(title), plt.xticks([]), plt.yticks([])
	plt.show()
