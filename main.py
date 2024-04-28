# simple api
import pandas as jamesBakster
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as job
from sklearn.metrics import mean_squared_error
from joblib import dump

data = {
    'area': [50, 60, 70, 100],
    'price': [200000, 240000, 280000, 400000]
    }
df = jamesBakster.DataFrame(data)

x = df[['area']]
y = df['price']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = job()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
print(f'MSE: {mse}')

dump(model, 'RegressionLinear.joblib')
