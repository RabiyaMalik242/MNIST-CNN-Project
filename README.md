# 🧠 MNIST Handwritten Digit Recognition using CNN

## 📌 Project Overview
This project implements a **Convolutional Neural Network (CNN)** to classify handwritten digits (0–9) using the MNIST dataset. The model is trained using TensorFlow/Keras and deployed with a Streamlit web application that allows users to draw or upload digits for real-time prediction.

---

## 🎯 Problem Type
- Type: Supervised Learning
- Task: Image Classification
- Category: Multi-class Classification (10 classes: digits 0–9)

---

## 📊 Dataset Information
- Dataset: MNIST (Keras built-in dataset)
- Training samples: 60,000 images
- Test samples: 10,000 images
- Image size: 28 × 28 pixels
- Channels: 1 (Grayscale)

Each image has:
- 784 features (28 × 28 pixels)

---

## 🧠 Model Architecture (CNN)

The model follows this structure:

Input → Conv2D → MaxPooling → Conv2D → MaxPooling → Flatten → Dense → Dropout → Output

### Layers Used:
- Conv2D (32 filters, 3×3, ReLU)
- MaxPooling2D (2×2)
- Conv2D (64 filters, 3×3, ReLU)
- MaxPooling2D (2×2)
- Flatten
- Dense (128 neurons, ReLU)
- Dropout (0.3)
- Dense (10 neurons, Softmax)

---

## ⚙️ Activation Functions
- ReLU:
  $f(x) = max(0, x)$

- Softmax:
  Converts output into probability distribution over 10 classes

---

## 🧪 Loss Function
- Categorical Crossentropy:
  Used for multi-class classification problems

---

## ⚙️ Optimizer
- Adam Optimizer:
  Adaptive learning rate optimization algorithm

---

## 📈 Training Details
- Epochs: 15
- Batch Size: 32
- Validation Split used
- Model trained using CNN architecture

---

## 📊 Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

---

## 📉 Results
- Test Accuracy: ~99%
- Low loss value indicating good convergence
- Minimal overfitting observed

---

## 📊 Visualizations Included

The project includes the following graphs:

- Sample MNIST digits
- Class distribution
- Before preprocessing visualization
- After preprocessing visualization
- Training vs Validation Accuracy
- Training vs Validation Loss
- Confusion Matrix
- Classification Report
- Final Accuracy Comparison Bar Chart
- Sample Predictions

---

## 🚀 Streamlit Web App Features
- Draw digit using canvas
- Upload image for prediction
- Real-time prediction output
- Displays probability scores for all digits

---

## 🧠 Key Concept

CNN learns features hierarchically:
- Early layers → edges and curves  
- Middle layers → shapes and patterns  
- Final layers → digit classification  

---

## 📦 Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run Project
### 1. Run Jupyter Notebook (Training)
jupyter notebook

Open:

model.ipynb

Run all cells to train and save the model.

### 2. Run Streamlit App

After training the model:

streamlit run app.py

Then open in browser:

http://localhost:8501
## 🧾 Requirements

Install dependencies using:

tensorflow
numpy
pandas
matplotlib
seaborn
opencv-python
scikit-learn
streamlit
👨‍💻 Author

MNIST CNN Project – Machine Learning Assignment

## ⭐ Future Improvements
Data augmentation for better generalization
Hyperparameter tuning for improved accuracy
Deployment on cloud (AWS / HuggingFace / Render)
Improve canvas drawing recognition accuracy

---

✔ This is now a **complete final README (no missing sections)**  
✔ Clean for GitHub  
✔ Strong for viva/exam presentation  
✔ Professional ML project format  

---

If you want next, I can help you:
✔ make your GitHub look “top 1% project level” (badges + screenshots layout)  
✔ or prepare viva Q&A from your exact CNN model  
✔ or help you deploy Streamlit online (very impressive for marks) 🚀
























