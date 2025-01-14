# Water Potability Prediction App

## Overview

The **Water Potability Prediction App** is a machine learning-based web application that predicts whether water is potable (safe to drink) based on several water quality features. The app uses a trained machine learning model to evaluate water characteristics such as pH, hardness, solids, chloramines, sulfate, conductivity, organic carbon, trihalomethanes, and turbidity.

The app is built using **Streamlit** for the user interface, and it utilizes a pre-trained **XGBoost model** to make predictions based on the user-provided input values.

## Features

- **Predict Potability**: The app takes various water quality features as input and predicts whether the water is potable or not.
- **Easy-to-use Interface**: The user-friendly interface allows users to input values through interactive number inputs (sliders).
- **Model**: The underlying model is trained using machine learning techniques to predict water potability based on historical data.

## Technologies Used

- **Streamlit**: For building the interactive web interface.
- **Python**: For the backend logic and handling data preprocessing.
- **XGBoost**: A powerful machine learning model for prediction.
- **Scikit-learn**: For data preprocessing (imputation and scaling).
- **Pandas**: For handling data and preparing it for prediction.

## How to Use

1. **Input Values**: Enter the values for various water quality features such as pH, hardness, solids, chloramines, sulfate, conductivity, organic carbon, trihalomethanes, and turbidity.
   
2. **Click on "Predict Water Potability"**: After entering the required values, click the "Predict Water Potability" button to get the result.

3. **Result**: The app will display whether the water is **potable** (safe to drink) or **not potable** (unsafe for drinking).

## Installation

To run this project locally, you need to set up your Python environment. Follow these steps:

### 1. Clone the Repository
### 2. Install Dependencies
### 3. Run the App
### 4. Access the App
```bash
git clone https://github.com/your-username/water-potability-prediction.git
cd water-potability-prediction 
pip install -r requirements.txt
streamlit run app.py
Once the app is running, open a browser and go to http://localhost:8501 to use the app.
```
## Model Details

The model used in this app is an **XGBoost classifier** that predicts the potability of water based on the following features:

- **pH**: The acidity or alkalinity of water.
- **Hardness**: The concentration of calcium and magnesium in water.
- **Solids**: The amount of dissolved solids in the water.
- **Chloramines**: The concentration of chloramines used for disinfecting water.
- **Sulfate**: The concentration of sulfate compounds.
- **Conductivity**: A measure of the water's ability to conduct electricity (related to dissolved minerals).
- **Organic Carbon**: A measure of organic contamination in the water.
- **Trihalomethanes**: Compounds formed by chlorine in the water.
- **Turbidity**: The cloudiness or haziness of water due to suspended particles.

The model was trained on a dataset and saved as a `.pkl` file, which is used in the app for making predictions.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Your Name: [Your GitHub Profile](https://github.com/your-profile)

## Acknowledgements

- Thanks to the Streamlit community for building a fantastic tool for rapid app development.
- Thanks to the XGBoost library for providing powerful machine learning tools.

## Contributing

If you'd like to contribute to the project, feel free to fork the repository and create a pull request. Please follow the steps below to contribute:

1. Fork the repository.
2. Clone your forked repository.
3. Create a new branch for your feature or fix.
4. Make your changes and test them locally.
5. Create a pull request with a description of your changes.