# Diabetes Prediction System: SVM Implementation
### AI Lab Semester Project | B.S. Artificial Intelligence

A machine learning application developed to predict the onset of diabetes based on diagnostic measurements. This project was built to demonstrate the practical application of supervised learning in healthcare informatics.

## 🚀 Project Context
Developed as a core Semester Project for the AI Lab, this system utilizes a Support Vector Machine (SVM) classifier to process clinical data. The project focuses on high-precision binary classification (Diabetic vs. Non-Diabetic).

## 📊 Dataset: Pima Indians Diabetes
The model was trained on the standardized Pima Indians dataset, featuring 8 specific medical predictors:
* Pregnancies | Glucose | Blood Pressure | Skin Thickness
* Insulin | BMI | Diabetes Pedigree Function | Age

## 🛠️ Technical Stack
* **Algorithm:** Support Vector Machine (SVM) with a Linear Kernel.
* **Libraries:** Scikit-Learn, NumPy, Pandas.
* **Environment:** Python 3.x (Local Lab Environment).

## 🧠 Key Learnings
* **Data Standardization:** Learned the importance of `StandardScaler` to ensure all 8 features (like Age vs. Insulin) are on the same scale for the SVM.
* **Model Evaluation:** Analyzed accuracy scores to ensure the classifier wasn't just "guessing" but finding the optimal hyperplane for the data.
* **Healthcare AI:** Explored the ethical and technical challenges of building predictive tools for medical diagnostics.

## 📡 Sample Logic
The system allows a user to input clinical measurements and returns a real-time prediction using the pre-trained SVM weights.
