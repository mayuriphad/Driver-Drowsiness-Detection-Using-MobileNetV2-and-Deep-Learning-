# Driver Drowsiness Detection Using MobileNetV2 and Deep Learning

This repository contains a complete implementation of a **Driver Drowsiness Detection System** using a pre-trained deep learning model. The system identifies drowsiness in drivers through real-time video feed analysis and provides alerts to ensure safety.

---

## 🚗 Motivation

Driver drowsiness is a significant contributor to road accidents, particularly among long-distance drivers. According to the National Highway Traffic Safety Administration:

- **1,550+ deaths**
- **71,000 injuries**
- **$12.5 billion** in economic damages annually

Existing solutions like EEG and ECG are impractical for real-world applications. This system offers a **non-invasive, real-time alternative** by tracking eye movements to determine drowsiness and triggering alerts or corrective actions.

---

## 📂 Dataset

- **Source:** [MRL Eye Dataset on Kaggle](https://www.kaggle.com/datasets/prasadvpatil/mrl-dataset)
- **Classes:** 
  - Open Eyes
  - Closed Eyes

---

## 🏗️ Model Architecture

- **Base Model:** MobileNetV2 (pre-trained on ImageNet)
- **Custom Layers:**
  - Global Average Pooling
  - Dropout (50% rate for regularization)
  - Fully Connected Dense Layer (Sigmoid activation for binary classification)
- **Loss Function:** Binary Crossentropy
- **Optimizer:** Adam (`learning rate = 1×10⁻⁵`)

---

## 🧪 Data Augmentation

- Rotation
- Width/Height Shifts
- Zoom
- Horizontal Flipping

---

## 🏋️ Training Details

- **Training Set:** 80%
- **Validation Set:** 10%
- **Testing Set:** 10%
- **Early Stopping:** To prevent overfitting

---

## 📊 Results

### Accuracy

- **Training Accuracy:** 99.11%
- **Test Accuracy:** 97.6%

### Confusion Matrix

|                | Predicted Drowsy | Predicted Non-Drowsy |
|----------------|:----------------:|:--------------------:|
| **Actual Drowsy**     | TP: 678           | FN: 215               |
| **Actual Non-Drowsy** | FP: 0             | TN: 1340              |

- **TP:** True Positive (Correctly detected drowsy states)
- **FP:** False Positive
- **TN:** True Negative (Correctly detected non-drowsy states)
- **FN:** False Negative

### Summary

The model demonstrates strong performance in identifying both drowsy and non-drowsy states. High precision and recall for non-drowsy states indicate reliability in distinguishing alert drivers, while the precision for drowsy states confirms minimal false alarms. Improving recall for the drowsy class could further enhance safety-critical applications.

---

## ⚙️ Implementation

- **Real-Time Monitoring**
  - Face and Eye Detection: Haar Cascade Classifier
  - Webcam Integration: Captures live video feed
  - Prediction Pipeline: Extracts eye regions, preprocesses images, and makes predictions using the trained model

- **Actions:**
  - Alarm for drowsy states
  - Simulated vehicle control for ignored alarms (speed reduction and lane shifting)

---

## 🏁 Conclusion

This driver drowsiness detection system offers a reliable and non-invasive solution for enhancing road safety. With high accuracy and real-time capabilities, it is an effective tool to prevent accidents caused by driver fatigue.

**Future Work:**  
Integrate this system into real vehicles and optimize response actions for different scenarios.

## 📄 Publication

This project is published in IEEE Xplore.  
🔗 [Read the Paper](https://ieeexplore.ieee.org/abstract/document/10864200)

---

