# CAT OR DOG MACHINE LEARNING OBJECT INDENTIFICATION PROGRAM
#### Video Demo: https://youtu.be/sWGO79YA9Xw
#### Description: 
This project was a machine learning object identification program that used a dataset of cats and dogs found on microsoft (https://www.microsoft.com/en-us/download/confirmation.aspx?id=54765). Using this dataset split into a training dataset, validation dataset and a test dataset we trained the model and then evaluated the model against the validation dataset and then tested the model against the test dataset. The training dataset got a 97% accuracy after 2 epochs and then the validation dataset got an accuracy of 94% and the test dataset got an accuracy of 92%. 

This code is a binary image classification model that uses transfer learning with a pre-trained model from TensorFlow Hub (NASNet Mobile) and fine-tunes it on a custom dataset. The model is trained on a binary classification task with a dataset of RGB images and can distinguish between two classes of images.

The model trainer was NasNet_Mobile (https://tfhub.dev/google/imagenet/nasnet_mobile/feature_vector/5).  This code can be done for more epochs if there is a better PC to run them on. If you have a good GPU you can do this for 10 epochs and get closer to a 99% accuracy. I had reduced the size of the training dataset for my PC performance but using all of microsoft dataset will improve the performance. Also the NasNet model isn't the best one. 

The model is trained for 2 epochs with a batch size of 32 using Adam optimizer with a learning rate of 3e-4. The training process uses a ImageDataGenerator for data augmentation, with a rescale factor of 1.0/255 and random rotation and zoom. The model is evaluated on the validation and test datasets using the Binary Crossentropy loss function and accuracy as metrics. The weights of the model are saved in the saved_model/ directory after training and evaluation.

There are other models out there. EfficentNet would likely get you better performance but NasNet gets the job done.  batch size of 32 was chosen because it worked well but other sizes can be tested to compare results  the learning rate of 0.0003 was also a good rate but other rates like 0.0001 can also be tested to compare results  I had saved the loaded model once it iterated through once so that it would have a base of the model to work off of which would be better than running from scratch each time. So this trained model was better to use.

Limitations
The code assumes that the required data and directory structure are in place.
The code only trains the model for 2 epochs for demonstration purposes, in a real-world scenario, the model should be trained for a larger number of epochs.
The code only evaluates the model on validation and test datasets and does not provide any visualizations of the model's performance.

Parameters: Learning rate= 3e-4, epochs= 2, verbose is the display style or running the training
