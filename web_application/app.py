import numpy as np
#request object here contains the data the client (e.g.a browser) has sent to my app
from flask import Flask, request, jsonify, render_template, send_from_directory
from joblib import load
import pickle

#app is an instant of Flask
app = Flask(__name__)
model = load('abalone_predictor.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_dynamic',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    #basically makes a new html instance, with prediction_test filed in
    return render_template('index.html', prediction_text='Salary is {}'.format(output))


# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     '''
#     For direct API calls trought request
#     '''
#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)