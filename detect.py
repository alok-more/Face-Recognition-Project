import cv2
import numpy as np
import sqlite3

# Load Haar Cascade for face detection
faceDetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Open camera
cam = cv2.VideoCapture(0)

# Load trained LBPH recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizer/trainingData.yml")


# Function to get student profile from database
def getProfile(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.execute(
        "SELECT * FROM student WHERE id = ?",
        (int(id),)
    )
    profile = cursor.fetchone()
    conn.close()
    return profile


while True:
    ret, img = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = faceDetect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Predict face
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        # Lower confidence = better match
        if confidence < 80:
            profile = getProfile(id)

            if profile is not None:
                cv2.putText(
                    img,
                    "Name: " + str(profile[1]),
                    (x, y + h + 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )
                cv2.putText(
                    img,
                    "Age: " + str(profile[2]),
                    (x, y + h + 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )
        else:
            cv2.putText(
                img,
                "Unknown",
                (x, y + h + 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

    cv2.imshow("Face Recognition", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()
