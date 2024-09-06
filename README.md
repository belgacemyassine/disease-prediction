# disease-prediction-project
This project is a Web Application for Disease Prediction and Image Classification built using Flask, a Python web framework. The application allows users to perform various tasks such as user authentication (login and registration), disease prediction based on user-input data, and image classification for medical diagnosis.

# Features:
User Authentication:

Allows users to register and log in using their credentials.
Stores user data securely in a MySQL database.
# Disease Prediction:

Predicts the likelihood of various diseases (diabetes, breast cancer, heart disease, kidney disease, and liver disease) based on user input.
Uses pre-trained machine learning models (pickle files) for making predictions.
# Image Classification:

Predicts medical conditions such as malaria, pneumonia, breast cancer, skin disease (derma), and tumors based on uploaded images.
Utilizes deep learning models (stored as .h5 files) to classify images.
Multiple Disease Prediction Pages:

Provides separate pages for different disease predictions, such as diabetes, heart disease, liver disease, and more.
# Error Handling:

Displays user-friendly error messages for invalid data entries or missing files.
Session Management:

Uses Flask sessions to manage user sessions and persist user state across different pages.
Technologies Used:
Flask: Python web framework for creating the web server and handling HTTP requests.
MySQL: Database management system for storing user information.
Machine Learning Models: Pre-trained models for predicting diseases using pickle and TensorFlow/Keras models (.h5 files) for image classification.
HTML/CSS: Frontend for creating the user interface.
Pillow (PIL): Python Imaging Library to handle image processing.
NumPy: For numerical computations and handling image arrays.
TensorFlow/Keras: Deep learning framework for loading and predicting with image classification models.
# How to Run:
Clone the repository to your local machine.
Create a Virtual Environment : python -m venv venv
Activate the Virtual Environment : venv\Scripts\activate
Install Required Packages : pip install Flask Flask-Session Pillow tensorflow mysql-connector-python numpy Collecting Flask
Run the Flask Application : python app.py
Usage:
User Registration/Login: Register a new user or log in with existing credentials.
Predict Disease: Choose a disease from the available options, input the required data, and get the prediction result.
Image Classification: Upload an image for a specific disease and get a diagnosis based on the pre-trained model.
Note:
Ensure all the required models are correctly placed in the models folder and are accessible to the Flask app. Additionally, configure the MySQL database properly to avoid connection issues.


