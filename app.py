from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('heart_disease_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get all feature inputs from the form
        features = [float(request.form[feature]) for feature in [
            'male', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds',
            'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP',
            'diaBP', 'BMI', 'heartRate', 'glucose'
        ]]
        
        # Convert to NumPy array and make prediction
        final_features = np.array([features])
        prediction = model.predict(final_features)

        output = '⚠️ U may have Heart Disease' if prediction[0] == 1 else '💚 Healthy,You may not have Heart Disease'

    except Exception as e:
        output = f"⚠️ Error: {e}"

    return render_template('index.html', prediction_text=f'Result: {output}')

if __name__ == "__main__":
    app.run(debug=True)
