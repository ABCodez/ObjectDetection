# ObjectDetection - Face Detection
This simple object detection app utilizes OpenCV, an open source computer vision and machine learning software library. 
There are countless users that utilizes the OpenCV library in order to create vast projects. In order to create an object detection application, I needed to research the Haar cascade Algorithm. This algorithm is needed in order to create a functioning application. Check out [opencv.org](https://opencv.org/)!

<p align="middle">
  <img src="https://user-images.githubusercontent.com/88639067/163072024-894a54eb-ad8a-4181-9b52-0da6e893ebff.gif" width="800" />
</p>

# HAAR Cascade 

<p align="middle">
  <img src="https://user-images.githubusercontent.com/88639067/163069610-9185fb08-8bce-4900-a283-144618b0e0fc.gif" width="350" />
  <img src="https://user-images.githubusercontent.com/88639067/163070000-8600132f-7577-4be0-a9ea-026ac3b3e508.png" width="560" /> 
</p>


Here's a simple explaination of what happens anytime an image is scanned for a specified object with the use of the Haar cascade algorithm. A small matrix goes across the image from left-to-right and top-to-bottom, gets a "feature" from each section covered and then classifies if the section has the specified feature we're looking for ( "Yes or no" ). So how do we define if the specified feature is a Yes or No feature? Well by training a Cascade Classifier we are able to do so. By feeding a classifier Positive and Negative samples of our desired object, it will start to recognize which sections contain the features. OpenCV has pre-trained Cascade Classifiers that will be used within this project!


# How it Works / Try it out!
Once you run the program, the application will prompt you for an image file. This image file needs to be located within the 'Assets/Images/' directory of the project in order to continue on forward. If the image file is not detected, a simple try and except statement is executed to ask you again for the file. Once the image has been fed to the program, it will resize while maintaining the resolution and aspect ratio for a user friendly experience. This image will then be converted into grayscale and then ran with our specified cascade classifier (in this case we are using the [Haarcascade Frontal Face](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) xml file provided by OpenCV). The program will start to detect any features found. Finally, the result image is displayed on screen with a box highlighting the object detected.

Cascade = cv2.CascadeClassifier("`Assets/CascadeClassifier/haarcascade_frontalface_default.xml`") </br>
If you'd like to test out some of the other Cascade Classifiers, I suggest OpenCV's predefined [Haars Cascade Classifiers](https://github.com/opencv/opencv/tree/master/data/haarcascades). Simply download and export the classifier to the 'Assets/CascadeClassifier/' directory, and then replace the code highlighted above with the path reference of the new classifier.


# Next Steps
Overall, this is a great way of showcasing the first steps in computer vision. My next step will definetly be looking into training my own Cascade Classifier.


