Color Segmentation using Single Gaussian
===================================

In this project, I have implemented an approach for robust color segmentation which was further used to detect a blue barrel. 

* Python 3.0, OpenCV 3.4

# Functions implemented
blue_barrel --> implemented roipoly function to get mask for blue barrel class
brown --> implemented roipoly function to get mask for brown class
green --> implemented roipoly function to get mask for green class
non_blue --> implemented roipoly function to get mask to non-barrel blue class
prob --> Gaussian classifier to calculate probablity of each class and to classify the image and produce the mask image
bluenp --> implemented roipoly and used np.load and np.save
get_mean --> To calculate mean and covariance for each class
logreg --> logistic regression function
barrel_detector --> implements the segmentation and calculates the bounding box of the segmented image
