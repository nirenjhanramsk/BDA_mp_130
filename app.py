from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('fraud_detection_model (2).pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form  # Collect form data
    # Create DataFrame from form input, converting to numeric format
    input_data = pd.DataFrame({
        'Time': [float(data['Time'])],
        'V1': [float(data['V1'])],
        'V2': [float(data['V2'])],
        'V3': [float(data['V3'])],
        'V4': [float(data['V4'])],
        'V5': [float(data['V5'])],
        'V6': [float(data['V6'])],
        'V7': [float(data['V7'])],
        'V8': [float(data['V8'])],
        'V9': [float(data['V9'])],
        'V10': [float(data['V10'])],
        'Amount': [float(data['Amount'])]
    })

    prediction = model.predict(input_data)
    result = "Fraudulent" if prediction[0] == 1 else "Legitimate"
    
    return render_template('index.html', prediction_text=f'Transaction is {result}')

if __name__ == '__main__':
    app.run(debug=True)
