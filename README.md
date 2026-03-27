Diabetes Prediction REST API
Developed by Subhan Nayyar
A production-ready Flask API designed to predict the likelihood of diabetes based on medical diagnostic measurements.

🚀 Overview
This project demonstrates the successful deployment of a Machine Learning model as a scalable web service. It accepts structured JSON requests containing 8 critical clinical features and provides real-time predictions.

🛠️ Technical Stack
Language: Python 3.8+

Framework: Flask

Libraries: NumPy, Scikit-Learn, Pickle

📊 Feature Architecture
The API processes the following clinical features:

Pregnancies | 2. Glucose | 3. Blood Pressure | 4. Skin Thickness | 5. Insulin | 6. BMI | 7. Pedigree | 8. Age

📡 Sample API Request
Endpoint: POST /predict

Sample JSON Body:
{
"pregnancies": 2,
"glucose": 135,
"blood_pressure": 82,
"skin_thickness": 31,
"insulin": 0,
"bmi": 29.8,
"pedigree": 0.881,
"age": 28
}

🔜 Future Enhancements
Full model weight integration (.pkl loading logic).

Docker containerization for cloud deployment.

Authentication endpoints for secure access.
