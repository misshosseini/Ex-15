from flask import Flask, request, jsonify, render_template
import joblib
import werkzeug

app = Flask(__name__)

# بارگذاری مدل در سطح جهانی
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    features = [float(data['MedInc']), float(data['HouseAge']), float(data['AveRooms'])]
    prediction = model.predict([features])
    return jsonify(prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)