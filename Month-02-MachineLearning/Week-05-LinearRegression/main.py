import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def load_data():

    data = fetch_california_housing()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Price'] = data.target

    print(f"Data loaded! Size: {df.shape}")
    return df

def train_model(df):
     
    X = df.drop('Price', axis=1)
    y = df['Price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("\n Model Performance:")
    print(f"Model trained! MSE: {mse:.4f}")
    print(f"R-Squared: {r2:.4f}")

    return y_test, y_pred

def visualize_results(y_test, y_pred):

    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5, color='blue')

    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)

    plt.xlabel('Actual Prices')
    plt.ylabel('Predicted Prices')
    plt.title('Actual vs Predicted Prices')
    plt.grid(True)

    plt.savefig('linear_regression_results.png')
    plt.show()

if __name__ == "__main__":
    
    print("--- Home Price Prediction Project (Linear Regression) ---")
    df = load_data()

    y_test_data, y_pred_data = train_model(df)
    visualize_results(y_test_data, y_pred_data)
