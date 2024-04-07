# salary-predictor
A project for deploying a salary predictor linear regression model using Flask API backend, and Heroku

It project predicts the salary of the employee based on the experience.

Flask is a web framework for Python, meaning that it provides functionality for building APIs and web applications. In this tutorial, we'll use Flask to create a simple web application that integrates our API with some basic html. This was referenced from https://github.com/TomasBeuzen/machine-learning-tutorials/tree/master/ml-deploy-model

## Directory Structure and Environment

```
└── root
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

* Open command Prompt, install `venv` and `requirements.txt` and go to given directory and then run python app.py
* Note that `procfile` is important for Heroku
* use `heroku ps:scale web=0` to shut down dynos or `heroku ps:scale web=1` to reactivate dynos
