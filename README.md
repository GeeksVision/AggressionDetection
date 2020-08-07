# AggressionDetection
AggreVision analyzes facial expressions to detect aggressive driving.

code_aggrevision.ipynb: our Jupyter Notebook code for our neural network + cv2 implementation!
haarcascade_frontalface_default.xml: our Cascade Classification file that is required to run the code

In the code (ipynb):
- load dataset of 'neutral' and 'aggressive' facial images
- transform and prepare images to be transfered to a neural network
- define the layers of the VGG Neural Network
- train the model on our training dataset
- run epochs on the loss functions to maximize accuracy
- test model on testing dataset
- implement cv2 to allow video stream expression detection!

This repository does not include our large dataset.

Let us know if you have any questions about the code, and enjoy AggreVision.
