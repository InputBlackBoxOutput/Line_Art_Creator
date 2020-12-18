# Line Art Creator: Convert images to line art using openCV
#
# @file  : segmenter.py
# @brief : Segments images using kmeans clustering (Default k=5)
# @author: Rutuparn Pawar <InputBlackBoxOutput>
# @date_created : 12 Aug 2020 

import cv2
import numpy as np
import matplotlib.pyplot as plt
import utils

#------------------------------------------------------------------------------------------------
def segmenter(image, k, show=False):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pixel_values = image.reshape((-1, 3))
    pixel_values = np.float32(pixel_values)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, (centers) = cv2.kmeans(pixel_values, k, None,
                                  criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers) 
    seg_image = centers[labels.flatten()]
    seg_image = seg_image.reshape(image.shape)

    if show:
        utils.showImage(seg_image, f"Segmented image (k={k})")

    return seg_image


def colouredEdges(image, edges, k=5, show=False):
    seg = segmenter(image, k)
    edge_stack = np.dstack((edges, edges, edges))
    col_edge = cv2.bitwise_and(seg, seg, mask=edges)
    col_edge[col_edge == 0] = 255
    
    utils.showImage(col_edge, "O/P")
        
    return col_edge
#------------------------------------------------------------------------------------------------
# EOF