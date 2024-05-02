from joblib import load
import numpy as np

loaded_model = load("RegressionLinear.joblib")

new_data = [100, 200, 300]

predicted_prices = loaded_model.predict(np.array(new_data).reshape(-1,1))

#show

for area, price in zip(new_data, predicted_prices):
    print(f"Área da casa {area}: preço {price:.2f}")
