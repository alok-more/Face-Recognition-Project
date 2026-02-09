import cv2
import numpy as np
import sqlite3

faceDetector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # to detect face in camera
cam=cv2.VideoCapture(0) # to access camera

def insertOrUpdateData(id, name, age):
    conn = sqlite3.connect("database.db") # connect to database
    cmd = "SELECT * FROM student WHERE ID=" + str(id) # check if record with given ID exists
    cursor = conn.execute(cmd)

    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1  
    if isRecordExist == 0: # insert new record
        cmd = "INSERT INTO student(ID, Name, Age) VALUES(" + str(id) + ", '" + str(name) + "', " + str(age) + ")"
    else:
        cmd = "UPDATE student SET Name='" + str(name) + "', Age=" + str(age) + " WHERE ID=" + str(id) # update existing record
    conn.execute(cmd)
    conn.commit()


# Insert user defined values
id = input("Enter your ID: ")
name = input("Enter your Name: ")
age = input("Enter your Age: ")

insertOrUpdateData(id, name, age) # insert or update data in database

# Detect face and save images
sampleNum = 0
while(True):
    ret, img = cam.read() # read frame from camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscalecolor
    faces = faceDetector.detectMultiScale(gray, 1.3, 5) # detect faces in frame
    for(x, y, w, h) in faces:
        sampleNum += 1
        cv2.imwrite("dataSet/User." + str(id) + "." + str(sampleNum) + ".jpg", gray[y:y+h, x:x+w]) # save detected face as image
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) # draw rectangle around detected face
        cv2.waitKey(100)
    cv2.imshow("Face", img) # display frame with detected face
    cv2.waitKey(1)
    
    if(sampleNum > 30):
        break

cam.release() # release camera
cv2.destroyAllWindows() # close all windows