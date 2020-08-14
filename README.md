# Line_Art_Creator
Convert any image to line art using computer vision

## Ignore if not a geek or a nerd
#### Steps involved in converting an image to line art

1. Get the image from the user
<img src="images/cat.jpg">

2. Convert the image to a grayscale image
<img src="images/readme/1_grayscale.png" height="300">

3. Apply gaussian filter to remove noise from the image
<img src="images/readme/2_gaussian_blur.png" height="300">

4. Apply median filter to remove 'salt and pepper' noise
<img src="images/readme/3_median_blur.png" height="300">

5. Apply bilateral filter to remove more noise from the image
<img src="images/readme/4_bilateral_filtered.png" height="300">

6. Apply Canny filter to detect edges <br> 
**Note**:Edge detection is achieved mostly by the Sobel filter present in Canny filter <br>
<img src="images/readme/5_edges.png" height="300">

7. Use Guo-Hall thinning for skeletonizing the image
<img src="images/readme/6_thinned.png" height="300">

**Note**: The effect of thinning can be observed in the image below (Removed areas marked in red): <br>
<img src="images/readme/thinning_diff.png" height="300">

8. Invert the pixels in the image
<img src="images/readme/7_inverted.png" height="300">

### Made with lots of ⏱️, 📚 and ☕ by InputBlackBoxOutput
