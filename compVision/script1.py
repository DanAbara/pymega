# opencv means open computer vision used for loading, displaying, resizing and writing images.
import cv2

img=cv2.imread("galaxy.jpg",0) # second parameter 1 means RGB while 0 means greyscale, -1 is colour with ability to use transparency
print(type(img))
print(img)
print(img.shape) # python stores an image as a numpy array (matrix of numbers)
print(img.ndim) # check dimension, height x width

resized_img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))) # resize/reshape to widht x height, here we are resizing it by half

cv2.imshow("Galaxy",resized_img) # imshow(titleofimage,imageobject)
cv2.imwrite("Galaxy_resized.jpg",resized_img) # params - titleofresizedimg, resizedimgobject

cv2.waitKey(0) # display image for 2 seconds (2000ms), 0 means image is displayed until window is closed manually
cv2.destroyAllWindows() # close window
