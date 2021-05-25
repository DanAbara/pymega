import cv2, time

# start webcam, default is 0
video=cv2.VideoCapture(0,cv2.CAP_DSHOW) 

# trick to compute no of frames
nf = 0

while True:
    # obtain frames for video capture object, 'check' is bool to confirm video is working
    # frame is the first frame of the video, python cv2 reads videos as frames of separate images
    nf = nf + 1
    check, frame = video.read() 

    print(check)
    print(frame)

    # Convert to gray scale - 
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #time.sleep(3) # hold camera on for 3 seconds

    # Show a window
    cv2.imshow("Capturing", gray)

    key = cv2.waitKey(1) # show next frame after the specified no of seconds
    
    # Break loop when key q is pressed
    if key==ord('q'): 
        break

print(nf) # show no of frames (no of iterations) after loop breaks

video.release()
cv2.destroyAllWindows
