import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Load the trained model
model = joblib.load('xgboost_model.pkl')


# Function to preprocess input data (impute and scale)
def preprocess_input_data(input_data):
    """Preprocess input data by imputing missing values and scaling features."""
    imputer = SimpleImputer(strategy='mean')
    scaler = StandardScaler()

    # Impute missing values and scale data
    input_data_imputed = imputer.fit_transform(input_data)
    input_data_scaled = scaler.fit_transform(input_data_imputed)

    return input_data_scaled


# Set the page configuration
st.set_page_config(page_title="Water Potability Prediction", page_icon="💧", layout="centered")

# Custom CSS for centering the title and description with a background
st.markdown("""
    <style>
        .header-container {
            background-color: #f0f8ff;
            padding: 50px 20px;
            text-align: center;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 50px;
        }
        .header-container h1 {
            font-size: 36px;
            color: #0078d4;
            font-weight: bold;
        }
        .header-container p {
            font-size: 18px;
            color: #333;
            line-height: 1.6;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 5px;
            padding: 10px 24px;
        }
    </style>
""", unsafe_allow_html=True)

# Display the title and description within a styled container
st.markdown("""
    <div class="header-container">
        <h1>Water Potability Prediction</h1>
        <p>This application predicts the potability of water based on key physicochemical features. 
        Simply enter the required values below and let the app determine whether the water is potable.</p>
    </div>
""", unsafe_allow_html=True)

# Feature input form layout
st.write("### Enter Water Quality Parameters")

# Create a 2-column layout for user input
col1, col2 = st.columns(2)

with col1:
    ph = st.number_input("pH (0.0 to 14.0)", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
    hardness = st.number_input("Hardness (mg/L)", min_value=0, max_value=500, value=150)
    solids = st.number_input("Total Dissolved Solids (mg/L)", min_value=0, max_value=61228, value=1000)
    chloramines = st.number_input("Chloramines (mg/L)", min_value=0, max_value=15, value=1)
    sulfate = st.number_input("Sulfate (mg/L)", min_value=0, max_value=500, value=200)

with col2:
    conductivity = st.number_input("Conductivity (μS/cm)", min_value=0, max_value=5000, value=2000)
    organic_carbon = st.number_input("Organic Carbon (mg/L)", min_value=0, max_value=50, value=10)
    trihalomethanes = st.number_input("Trihalomethanes (μg/L)", min_value=0, max_value=124, value=2)
    turbidity = st.number_input("Turbidity (NTU)", min_value=0, max_value=10, value=2)

# Button to trigger the prediction
if st.button("Predict Water Potability"):
    # Prepare input data for prediction
    input_data = pd.DataFrame({
        'ph': [ph],
        'Hardness': [hardness],
        'Solids': [solids],
        'Chloramines': [chloramines],
        'Sulfate': [sulfate],
        'Conductivity': [conductivity],
        'Organic_carbon': [organic_carbon],
        'Trihalomethanes': [trihalomethanes],
        'Turbidity': [turbidity]
    })

    try:
        # Preprocess input data
        input_data_scaled = preprocess_input_data(input_data)

        # Make the prediction
        prediction = model.predict(input_data_scaled)

        # Display the prediction result dynamically
        if prediction == 0:
            st.error("❌ **The water is not potable.** Please treat the water before consumption.")
        else:
            st.success("✅ **The water is potable.** You can safely consume the water.")

    except Exception as e:
        st.error(f"An error occurred while making the prediction: {e}")

# Footer with additional information
st.write("""
    --- 
    Developed by: **Priyangka Roy**
    - Model: Trained using XGBoost
    - Contact: priyangka.roy016@gmail.com
""")
