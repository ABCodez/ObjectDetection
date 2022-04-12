import cv2  # openCV package
import imutils  # openCV functions package


def ObjectDetection(file):
    # import Cascade Classifier to be used
    Cascade = cv2.CascadeClassifier("Assets/CascadeClassifier/haarcascade_frontalface_default.xml")

    # import image and and resize image
    img = cv2.imread('Assets/Images/' + file)
    img = imutils.resize(img, width=900)

    # Convert image to grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect the objects within the image as well as define scaling factor and min neighbours
    objectDetect = Cascade.detectMultiScale(imgGray, 1.1, 4)

    # create a box around the detected object
    boxColor = 127, 255, 0
    textColor = 127, 255, 0
    for (x, y, w, h) in objectDetect:
        cv2.rectangle(img, (x, y), (x + w, y + h), boxColor, 2)  # Define rectangle attributes
        cv2.putText(img, "Face", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, textColor, 2)  # text over object

    # print the final result
    cv2.imshow("Object Detection - ABCodez", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ask user for file and prompt them if file doesn't exist
try:
    ObjectDetection(file=input("Enter Image File name: "))
except:
    print("File not found! Try again.")
    ObjectDetection(file=input("Enter Image File name: "))
