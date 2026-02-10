import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create() # create LBPH face recognizes the face in camera
path = "dataSet"

def getImagesWithID(path):
    imagesPath = [os.path.join(path, f) for f in os.listdir(path)] # get path of all images in dataset
    faces = []
    ids=[]
    for singleImagePath in imagesPath:
        faceImage = Image.open(singleImagePath).convert('L') # convert image to grayscale L = luminance(increases contrast of image)
        faceNP = np.array(faceImage, 'uint8') # convert image to numpy array
        id = int(os.path.split(singleImagePath)[-1].split(".")[1]) # get ID from image name
        print(id)
        faces.append(faceNP) # append face to list of faces
        ids.append(id) # append ID to list of IDs
        cv2.imshow("training", faceNP) # display training image
        cv2.waitKey(10)

    return np.array(ids), faces

ids, faces = getImagesWithID(path) # get IDs and faces from dataset
recognizer.train(faces, ids) # train recognizer with faces and IDs
recognizer.save("recognizer/trainingData.yml") # save trained model to file
cv2.destroyAllWindows()

