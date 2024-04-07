import numpy as np
#request object here contains the data the client (e.g.a browser) has sent to my app
from flask import Flask, request, session, jsonify, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from joblib import load
import pickle

#1. app is an instance of flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'asecretkey'

#2 define a prediction function
def return_prediction(model, input_json):
    '''
    input_json is a dictionary
    '''

    input_data = [[input_json[k] for k in input_json.keys()]]
    prediction = model.predict(input_data)[0]

    return round(prediction,2)

#3. load model
model = load('abalone_predictor.joblib')

#4. create a WTForm class
class PredictForm(FlaskForm):
    exp = StringField("Years of Experience")

#5. set up home page
@app.route('/', methods=["GET","POST"])
def home():

    # Create instance of the form
    form = PredictForm()

    # Validate the form
    if form.validate_on_submit():
        session['exp'] = form.exp.data
        return redirect(url_for("predict"))

    return render_template('home.html', form=form)

# 6. define a new "predict" route that processes form input and returns a model prediction
@app.route('/predict')
def predict():

    content = {}
    content['exp'] = float(session['exp'])
    results = return_prediction(model, content)
    return render_template('prediction.html', results=results)


if __name__ == "__main__":
    app.run(debug=True)