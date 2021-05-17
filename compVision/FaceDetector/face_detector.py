import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # load the classifier to be used on the image

img=cv2.imread("news.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # make the image 'img' a black and white image

# using the classifier to detect the top left cartesian point of the image, the width and the height
face_coordinate = face_cascade.detectMultiScale(img_gray,
    scaleFactor=1.1,
    minNeighbors=4) # scaleFactor - no of passes on the image. 1.05 means 5% reduction in size on each pass. Higher values mean less accuracy

# draw a rectangle representing the coordinates on the image, x cord, y cord, w width, and h height
for x,y,w,h in face_coordinate:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) # imageToUpdate, topLeftCoord, buttomRightCoord, BGRspecifier, rectangleThickness

# resize image

img=cv2.resize(img,(int(img.shape[1]/3), int(img.shape[0]/3))) # imageToResize, width, height

print(type(face_coordinate))
print(face_coordinate)
print(img.shape)

cv2.imshow("Gray",img)
cv2.waitKey(0) # wait until user closed window manually
cv2.destroyAllWindows()