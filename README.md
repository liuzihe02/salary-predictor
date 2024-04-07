# salary-predictor
A project for deploying a salary predictor linear regression model using Flask API backend, and Heroku

It project predicts the salary of the employee based on the experience.

Flask is a web framework for Python, meaning that it provides functionality for building APIs and web applications. In this tutorial, we will explore:

1. using Flask to create a RESTful web API to interface with a machine leanring model; and,
2. using Flask to create a simple web application that integrates our API with some basic html.

## Directory Structure and Environment

```
flask
├── build_model.ipynb  # this notebook contains the model building code
├── web_api
│   └── abalone_predictor.joblib  # this is the machine learning model we have built locally
│   └── app.py  # the file that defines our flask API
│   └── Procfile  # required by Heroku to help start flask app
│   └── requirements.txt  # file containing required packages
│   
└── web_application
    └── abalone_predictor.joblib  # this is the machine learning model we have built locally
    └── app.py  # the file that defines our flask API
    └── Procfile  # required by Heroku to help start flask app
    └── requirements.txt  # file containing required packages
    └── static # this subdirectory contains CSS style sheets
    │   └── style.css  # css template to be used in web application
    └── templates  # this subdirectory contains HTML templates to help us build the web application
        └── home.html  # html template to be used in web application
        └── prediction.html  # html template to be used in web application
```

Open command Prompt, install `venv` and `requirements.txt` and go to given directory and then run python app.py
