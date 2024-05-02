#  carregar modelo

from joblib import load

loaded_model = load("RegressionLinear.joblib")

new_area = [100, 200, 350]

predicted_prices = loaded_model.predict(np.array(new_area).reshape(-1,1))

# Show

for area, price in zip(new_area, predicted_prices):
    print(f'Area em metros quadrados {area}: Preço estimado ${price:.2f}')
