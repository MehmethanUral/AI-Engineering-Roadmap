# 🏠 House Price Prediction (Linear Regression)

This project marks the beginning of **Month 2 (Machine Learning)** in my AI Engineering Roadmap. It implements a **Linear Regression** model to predict house prices based on various features using the California Housing dataset.

## 🎯 Objective
To build a supervised machine learning model that learns the relationship between housing features (like median income, house age) and the target price, and evaluate its accuracy using **R-squared ($R^2$)**.

## 🧠 Model & Metrics
* [cite_start]**Algorithm:** Linear Regression ($y = w_1x_1 + w_2x_2 + ... + b$)[cite: 112].
* **Dataset:** California Housing Dataset (Scikit-Learn built-in).
* **Evaluation Metric:**
    * [cite_start]**R-squared ($R^2$):** Indicates how well the data fit the regression model (Closer to 1 is better)[cite: 117].
    * [cite_start]**MSE (Mean Squared Error):** Measures the average squared difference between estimated values and the actual value.

## 📂 Project Structure

```text
Week-05-LinearRegression/
├── main.py              # ML Model Training & Prediction
├── prediction_plot.png  # Actual vs Predicted Visualization
├── requirements.txt     # Dependencies
└── README.md            # Documentation