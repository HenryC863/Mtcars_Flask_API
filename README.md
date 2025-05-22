# Mtcars Flask API

- Author - Gaohong Chen 
- Course - STAT 418
- Subject - Homework 3

This project is a linear regression model API built with Flask and deployed using Docker and Google Cloud Run. The model is trained using the `mtcars.csv` dataset to predict a car’s MPG (miles per gallon) based on various vehicle specifications.

# Project Structure

- `prediction.py` – trains the linear regression model and defines the `predict()` function.
- `server.py` – Flask API to receive JSON input and return the predicted MPG.
- `curl_test.sh` – Example curl script to test the deployed endpoint.
- `Dockerfile` – Defines how the app is containerized.
- `docker-compose.yml` – Optional tool to manage local development and testing.

# Test on local machine

1. Clone this repo to your local machine.
2. To run this API, change your directory to the docker folder and run:

   `docker compose up -d`
   
4. Open a new terminal and run the following code to get a response `server is up - nice job!`

   `curl http://localhost:5050/`

5. Finally, send a test prediction by making a curl POST request to the API locally using the command below:
   
   `curl -X POST http://localhost:5050/predict_price \-H "Content-Type: application/json" \-d '{"cyl": 8, "disp": 360.0, "hp": 175, "drat": 3.15, "wt": 3.44, "qsec": 17.02, "vs": 0, "am": 0, "gear": 3, "carb": 2}'`

# Test on Google Cloud

Use the following curl command that calls the model API:

   `curl -X POST https://mtcars-flask-app-693104809772.us-central1.run.app/predict_price \ -H "Content-Type: application/json" \ -d '{"cyl": 8, "disp": 360.0, "hp": 175, "drat": 3.15, "wt": 3.44, "qsec": 17.02, "vs": 0, "am": 0, "gear": 3, "carb": 2}'`

Then you will receive the following response:

   `{"predict cost": 17.6934340286975}`
