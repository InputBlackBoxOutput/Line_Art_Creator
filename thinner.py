# Line Art Creator: Convert images to line art using openCV
#
# @file  : thinner.py
# @brief : Performs thinning of edges using Guo-Hall thinning
# @author: Rutuparn Pawar <InputBlackBoxOutput>
# @date_created : 12 Aug 2020

#--------------------------------------------------------------------------------------
import sys
try:
	import itertools as it
	import numpy as np
	import matplotlib.pyplot as plt
except ImportError:
    print('Modules required by thinner.py not found')
    print('Use pip install -r requirements.txt to install modules')
    sys.exit()

#--------------------------------------------------------------------------------------
def thinner(src):
	def iteration(src, iter):
		marker = np.ones(src.shape, np.uint8)
		h,w = src.shape
		changed = 0
		for j,i in np.transpose(np.nonzero(src)):
			if i==0 or i==w-1: continue
			if j==0 or j==h-1: continue
			assert src.item(j,i)!=0
			p2 = src.item((j,   i-1))
			p3 = src.item((j+1, i-1))
			p4 = src.item((j+1, i))
			p5 = src.item((j+1, i+1))
			p6 = src.item((j,   i+1))
			p7 = src.item((j-1, i+1))
			p8 = src.item((j-1, i))
			p9 = src.item((j-1, i-1))
			C = ((~p2 & (p3 | p4)) + (~p4 & (p5 | p6)) + (~p6 & (p7 | p8)) + (~p8 & (p9 | p2)))
			N1 = (p9 | p2) + (p3 | p4) + (p5 | p6) + (p7 | p8)
			N2 = (p2 | p3) + (p4 | p5) + (p6 | p7) + (p8 | p9)
			N = min(N1, N2)
			if iter==0:
				m = (p8 & (p6 | p7 | ~p9))
			else:
				m = (p4 & (p2 | p3 | ~p5))
			# print i,j
			# print p2, p3,p4,p5,p6,p7,p8,p9
			# print "C",C, "N",N, "m", m
			if C==1 and 2<= N <=3 and m==0:
				marker.itemset((j,i),0)
				changed += 1
		return src & marker, changed

	dst = src.copy()
	i=0;
	while True:
		i+=1
		# now = time.clock()
		dst, changed  = iteration(dst, 0)
		dst, changed2 = iteration(dst, 1)
		# dst, changed  = c_iteration(dst, 0)
		# dst, changed2 = c_iteration(dst, 1)

		# print time.clock() - now
		d = changed + changed2
		if d == 0:
			break
			
	return dst 

#--------------------------------------------------------------------------------------
def thinEdges(edges, show=False):
	thinned = thinner(edges)

	if show == True:
		plt.plot(), plt.imshow(255 - thinned, cmap="gray") # Image inverted
		plt.title("O/P"), plt.xticks([]), plt.yticks([])
		plt.show()

	return thinned
#--------------------------------------------------------------------------------------
# EOF