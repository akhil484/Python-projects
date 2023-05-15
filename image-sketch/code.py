import cv2
import matplotlib.pyplot as plt


def showImage(img):
	cv2.imshow("Image",img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


def plotImage(img, Name_of_image, grid_dict):
	plt.subplot(grid_dict['row'],grid_dict['col'],grid_dict['index'])
	plt.title(Name_of_image, size=20)
	plt.imshow(img)

	#Hides the axes and their labels
	plt.axis('off')


def invert_image(img):
	return 255-img

def convert_BGR_to_RGB(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def create_sketch():

	original_img=cv2.imread("goku.png")

	# showImage(original_img)

	#Convert to Grey Image
	grey_img=cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
	

	invert_img=invert_image(grey_img)

	#Blur image
	blur_img=cv2.GaussianBlur(invert_img, (3,3),0)


	#Invert Blurred Image
	invblur_img=invert_image(blur_img)

	sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)
	# showImage(sketch_img)

	#Save Sketch
	cv2.imwrite("sketch.png", sketch_img)


	#CV2 uses BGR color scheme whereas plt uses RGB scheme
	#That's why we are converting to RGB
	RGB_IMG=convert_BGR_to_RGB(original_img)
	rgb_sketch=convert_BGR_to_RGB(sketch_img)

	plt.figure(figsize=(20,18))

	plotImage(RGB_IMG, 'Original', {'row':1,'col':2,'index':1})
	plotImage(rgb_sketch, 'Sketch', {'row':1,'col':2,'index':2})

	plt.show()


if __name__ == '__main__':
	create_sketch()