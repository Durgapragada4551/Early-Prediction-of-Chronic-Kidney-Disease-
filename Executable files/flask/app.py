from flask import Flask, render_template, request
import numpy as np
import joblib  # Assuming you're using joblib to load your ML model

app = Flask(__name__)

# Load your pre-trained model (update the path as necessary)
# model = joblib.load('path/to/your/model.pkl')

@app.route('/')
def home():
    return render_template('home.html')  # Home page

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Extract form data
        blood_urea = float(request.form['blood_urea'])
        blood_glucose = float(request.form['blood_glucose'])
        anemia = 1 if request.form['anemia'] == 'yes' else 0
        coronary_artery_disease = 1 if request.form['coronary_artery_disease'] == 'yes' else 0
        pus_cell = 1 if request.form['pus_cell'] == 'yes' else 0
        red_blood_cell = request.form['red_blood_cell']
        diabetes_mellitus = 1 if request.form['diabetes_mellitus'] == 'yes' else 0
        pedal_edema = 1 if request.form['pedal_edema'] == 'yes' else 0

        # Prepare input for the model
        input_data = np.array([[blood_urea, blood_glucose, anemia, coronary_artery_disease, pus_cell,
                                 red_blood_cell, diabetes_mellitus, pedal_edema]])

        # Get prediction (replace this with your model's prediction logic)
        # prediction = model.predict(input_data)
        
        # For demonstration, let's assume the following simple logic
        prediction = "Yes" if blood_urea > 50 else "No"  # Replace with actual model prediction

        if prediction == "Yes":
            return render_template('result.html')  # Chronic Kidney Disease
        else:
            return render_template('result1.html')  # No Chronic Kidney Disease

    return render_template('predict.html')  # Prediction input page

if __name__ == '__main__':
    app.run(debug=True)
