# Driver Drowsiness Detection Using MobileNetV2 and Deep Learning 
 ....

This repository contains the complete implementation of a Driver Drowsiness Detection System using a pre-trained deep learning model. The system identifies drowsiness in drivers through real-time video feed analysis and alerts to ensure safety.
Driver drowsiness is a significant contributor to road accidents, particularly among long-distance drivers. The National Highway Traffic Safety Administration attributes over 1,550 deaths, 71,000 injuries, and $12.5 billion in economic damages annually to drowsiness-induced accidents.
Existing solutions like EEG and ECG are impractical for real-world applications. This system provides a non-invasive, real-time alternative by tracking eye movements to determine drowsiness and triggering alerts or taking corrective actions to mitigate risks.

# Dataset
Dataset
The model is trained on the MRL Eye Dataset, categorized into two classes:
Open Eyes
Closed Eyes
dataset : https://www.kaggle.com/datasets/prasadvpatil/mrl-dataset

# Model Architecture

Base Model: MobileNetV2 pre-trained on ImageNet for feature extraction.
Custom Layers:
Global Average Pooling Layer
Dropout Layer (50% rate for regularization)
Fully Connected Dense Layer (Binary classification using sigmoid activation).
Loss Function: Binary Crossentropy.
Optimizer: Adam with a learning rate of 
1
×
1
0
−
5
1×10 
−5
 .
# Data Augmentation

Rotation, width/height shifts, zoom, and horizontal flipping applied to improve model generalization.
Training Details

Training set: 80%
Validation set: 10%
Testing set: 10%
Early stopping to prevent overfitting.

# III. Results
Accuracy:

Training Accuracy: 99.11%
Test Accuracy: 97.6%

# Confusion Matrix:
True Positive (Correctly detected drowsy states): 678
False Positive: 0
True Negative (Correctly detected non-drowsy states): 1340
False Negative: 215

Summary:
The model demonstrates strong performance in identifying both drowsy and non-drowsy states. High precision and recall values for non-drowsy states indicate reliability in distinguishing alert drivers, while the precision for drowsy states confirms the model's minimal false alarms. However, improving recall for the drowsy class could enhance safety-critical applications.

# IV. Implementation
Real-Time Monitoring
Face and Eye Detection: Using Haar Cascade Classifier.
Webcam Integration: Captures live video feed.
Prediction Pipeline: Extracts eye regions, preprocesses images, and makes predictions using the trained model.

# Actions:
Alarm for drowsy states.
Simulated vehicle control for ignored alarms (speed reduction and lane shifting).

# V. Conclusion
This driver drowsiness detection system offers a reliable and non-invasive solution for enhancing road safety. With its high accuracy and real-time capabilities, it is an effective tool to prevent accidents caused by driver fatigue. Future work includes integrating this system into real vehicles and optimizing response actions for different scenarios.



# requirement.txt
tensorflow==2.9.1
numpy==1.23.5
opencv-python==4.7.0.72
pygame==2.5.0
scikit-learn==1.2.2
pillow==9.4.0

