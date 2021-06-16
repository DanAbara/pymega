import cv2, time
from datetime import datetime
import pandas as pd

first_frame = None # none is a special keyword to allocate an empty variable.
status_list=[None,None] 
times=[]
df=pd.DataFrame(columns=["Start","End"])

# start webcam, default is 0
video=cv2.VideoCapture(0,cv2.CAP_DSHOW) 

while True:
    # obtain frames for video capture object, 'check' is bool to confirm video is working
    # frame is the first frame of the video, python cv2 reads videos as frames of separate images
    check, frame=video.read() 
    status=0 

    # Convert to gray scale - 
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0) # make the image blurry; useful for better accuracy in computing differences

    # if first frame is none, assign the gray frame to it. Then re-run while-loop from beginning. 
    # This will be the case for the first iteration of the while loop. 
    # The statements in the if statement will not run for the second and following iterations because the if condition will return false.
    if first_frame is None:
        first_frame=gray
        continue 


    delta_frame=cv2.absdiff(first_frame,gray)

    # If the difference 'delta_frame' is > 30, assign white which is 255, else assign 0 which is black
    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1] # THRESH_BINARY is one of several threshold methods which returns a tuple of 2 values. The second value is what we need.

    # smooth out the thresh_frame
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2) # iterations defines how many times you want to go through the smoothing. the larger iterations is, the smoother the image
    
    # Find the contours on the thresh frame. I'm using cv2 so its (cnts,_). Cv3 is (_,cnts,_).
    (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get only contours > a certain no of pixels eg. 1000. If less than 1000, check the next contour by running the next iteration of the for loop.
    for contour in cnts:
        if cv2.contourArea(contour) < 100000:
            continue

        status=1

        (x,y,w,h)=cv2.boundingRect(contour) # if > 1000 create a rectangle with that countour
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)
    
    status_list.append(status)
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    # Show a window
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Thresh Frame", thresh_frame)
    cv2.imshow("Color", frame) # show the color frame with the rectangle

    key = cv2.waitKey(1) # show next frame after the specified no of seconds
    
    # Break loop when key q is pressed
    if key==ord('q'): 
        if status==1:
            times.append(datetime.now())
        break

    
print(status_list)
print(times)

for t in range(0,len(times),2):
    df=df.append({"Start":times[t], "End":times[t+1]},ignore_index=True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows
