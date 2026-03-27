# AI Lab Project: Diabetes Prediction using SVM
# Inspired by the Pima Indians Healthcare Dataset Analysis

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import svm

# Note: In the live Lab version, we loaded the 'diabetes.csv' here.
# This sample demonstrates the core prediction logic used in the final submission.

def predict_diabetes(input_data):
    # Standard 8 clinical features required for the model
    # input_data format: (Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, Pedigree, Age)
    
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # In our lab project, we used StandardScaler to normalize the data 
    # before feeding it into the SVM Classifier
    
    # prediction = classifier.predict(std_data)
    
    # Return Logic:
    # if (prediction[0] == 0):
    #   return 'The person is not diabetic'
    # else:
    #   return 'The person is diabetic'
    
    print("SVM Logic Initialized. Ready for feature processing.")

# Sample input from the AI Lab testing phase:
# test_input = (5, 166, 72, 19, 175, 25.8, 0.587, 51)
