import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv('mtcars.csv')

Y = data['mpg']
X = data.drop(['mpg','model'], axis=1)

model = LinearRegression()
model.fit(X,Y)

def predict(dict_values, X = X, model = model):
  x = np.array([float(dict_values[col]) for col in X])
  x = x.reshape(1,-1)
  y_pred = model.predict(x)[0]
  return y_pred

