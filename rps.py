# -*- coding: utf-8 -*-
#!/usr/bin/env python
import cv2, sys
import numpy as np
import os
import webbrowser
import time
import random

url = 'http://localhost/Register'
def OpenUrl():
    
    #os.system("killall -KILL chromium")
    webbrowser.open(url,new=0)
    #pyautogui.hotkey('ctrl', 'w')  # ctrl-w to close the tab
    #keypress('keydown Control_L')
    #keypress('key w')
    #keypress('keyup Control_L')

#def rules():
def savepic():
    IMAGE_FILE = "/var/www/html/Register/pic.jpg"
    cv2.imwrite(IMAGE_FILE, frame)


# Constants
DEVICE_NUMBER = 2
FONT_FACES = [
    cv2.FONT_HERSHEY_SIMPLEX,
    cv2.FONT_HERSHEY_PLAIN,
    cv2.FONT_HERSHEY_DUPLEX,
    cv2.FONT_HERSHEY_COMPLEX,
    cv2.FONT_HERSHEY_TRIPLEX,
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
    cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX
]
# Init the Cascade Classifier
# http://docs.opencv.org/modules/objdetect/doc/cascade_classification.html#cascadeclassifier
    



#eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Init webcam
# http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-videocapture
vc = cv2.VideoCapture(DEVICE_NUMBER)
vc.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 384)
# Check if the webcam init was successful
# http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-isopened
if vc.isOpened(): # try to get the first frame
    # http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-read
    retval, frame = vc.read()
else:
    sys.exit(1)

# If webcam read successful, loop indefinitely
db = 0
ges = 0
i = 0
a = 100
b = 100
c = 200
d = 200
play = 0

while retval:
    # Define the frame which the webcam will show
    #e1 = cv2.getTickCount()
    frame_show = frame
    height, width, channels = frame.shape
    #print height, width, channels
    #480, 640, 3
    sub_frame = frame_show[a:a+c, b:b+d]
    font_typeface = FONT_FACES[2]
    font_scale = .8
    font_color = (169, 169, 169)
    font_weight = 2
    #sub_frame = frame
    
    cv2.rectangle(frame_show, (a, b), (a+c, b+d), (0, 255, 255), 2)
    cv2.rectangle(frame_show, (0, height-40), (width/2, height), (20, 20, 240), -1)
    cv2.rectangle(frame_show, (width/2, height-40), (width, height), (255,0,0), -1)
    cv2.putText(frame_show, "Dragons", (20, height - 10), font_typeface, font_scale, font_color, font_weight)
    cv2.putText(frame_show, str(db), (width/2 - 100, height - 10), font_typeface, font_scale, font_color, font_weight)
    cv2.putText(frame_show, str(ges), (width/2 + 50, height - 10), font_typeface, font_scale, font_color, font_weight)
    cv2.putText(frame_show, "Mortals", (width - 150, height - 10), font_typeface, font_scale, font_color, font_weight)

    if i%1 == 0:
        if i%31 == 0:
            XML_PATH = "cascades/rock.xml"
            player_rps = "Rock"
        elif i%61 == 0:
            XML_PATH = "cascades/hand.xml"
            player_rps = "Scissors"
        elif i%97 == 0: 
            XML_PATH = "cascades/paper.xml"
            player_rps = "Paper"
        else:
            XML_PATH = "cascades/faces.xml"
            player_rps = " "
            
        faceCascade = cv2.CascadeClassifier(XML_PATH)
	#	cv2.rectangle(frame_show, (a, b), (a+c, b+d), (169, 169, 169), 2)
    	
        # Convert frame to grayscale
        sub_frame = cv2.cvtColor(sub_frame, cv2.COLOR_BGR2GRAY)
            # Detect objects and return an array of faces
            # http://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html#cascadeclassifier-detectmultiscale
        faces = faceCascade.detectMultiScale(
            sub_frame,
            scaleFactor=1.2,
            minNeighbors=2,
            minSize=(50, 50)
            #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

    #Blur the image
 	#cv2.rectangle(frame, (10,10), (160,160), (255,255,0), 5)
 	#sub_face = frame[10:160, 10:160]
    # apply a gaussian blur on this new recangle image
    #sub_face = cv2.GaussianBlur(sub_face,(23, 23), 30)
	# merge this blurry rectangle to our final image
    #frame[10:10+sub_face.shape[0], 10:10+sub_face.shape[1]] = sub_face
    #face_file_name = "./face_" + str(y) + ".jpg"
    #cv2.imwrite(face_file_name, sub_face)

 	

 	# Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        # http://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html#rectangle
        #cv2.rectangle(frame_show, (a+x, b+y), (a+x+w, b+y+h), (0, 0, 255), 2)
        font_typeface = FONT_FACES[2]
        font_scale = .8
        font_color = (20, 20, 240)
        font_weight = 2
        comp = random.randint(0,3)
        if comp == 0:
            comp = "Rock"
        elif comp == 1:
            comp = "Paper"
        else:
            comp = "Scissors"
        
        if player_rps == comp:
            print "It's a tie!"
            cv2.putText(frame_show, "It's a tie!", ( 20, 20), font_typeface, font_scale, font_color, font_weight)
        elif player_rps == "Rock":
              if comp == "Paper":
                  print "The DragonBoard Wins!"
                  cv2.putText(frame_show, "The DragonBoard Wins!", ( 20, 20), font_typeface, font_scale, font_color, font_weight)
                  db += 1
              elif comp == "Scissors":
                  print "You Win!!"
                  cv2.putText(frame_show, "You Win!!", ( 20, 20), font_typeface, font_scale, font_color, font_weight)
                  ges += 1
        elif player_rps == "Paper":
              if comp == "Scissors":
                  print "The DragonBoard Wins!"
                  cv2.putText(frame_show, "The DragonBoard Wins!", ( 20, 20), font_typeface, font_scale, font_color, font_weight)
                  db += 1
              elif comp == "Rock":
                  print "You Win!!"
                  cv2.putText(frame_show, "You Win!!", ( 20, 20), font_typeface, font_scale, font_color, font_weight)
                  ges += 1
        else: #scissors
              if comp == "Rock":
                  print "The DragonBoard Wins!"
                  cv2.putText(frame_show, "The DragonBoard Wins!", ( 20, 20), font_typeface, font_scale, font_color, font_weight)
                  db += 1
              elif comp == "Paper":
                  print "You Win!!"
                  cv2.putText(frame_show, "You Win!!", ( 20, 20), font_typeface, font_scale, font_color, font_weight)
                  ges += 1

        x = 2
        y = 50
        cv2.putText(frame_show, comp, (20, height - 50), font_typeface, font_scale, font_color, font_weight)
        font_color = (255,0,0)
        cv2.putText(frame_show, player_rps, (width - 150, height - 50), font_typeface, font_scale, font_color, font_weight)
        play = 1
        #time.sleep(5.5)
        
    # Show the image on the screen
    # http://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#imshow
    cv2.imshow('Rock Paper Scissors', frame_show)
    #e2 = cv2.getTickCount()
    #time1 = (e2 - e1)/ cv2.getTickFrequency()
    #print i, time1
    #cv2.namedWindow('Facial Detection',cv2.WINDOW_AUTOSIZE)
    #cv2.resizeWindow('Facial Detection', 700,500)

    # Grab next frame from webcam
    retval, frame = vc.read()

    
	# Launch the Borwser if the spacebar is pressed
    # http://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#waitkey
    if cv2.waitKey(1) == 32:
    	#url = 'http://www.google.com'
    	#webbrowser.open_new(url)
        savepic()
        OpenUrl()
    # Exit program after waiting for a pressed key
    # http://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#waitkey
    if cv2.waitKey(1) == 27:
    	break

    i += 1
    if play == 1:
        time.sleep(1.5)
        play = 0



