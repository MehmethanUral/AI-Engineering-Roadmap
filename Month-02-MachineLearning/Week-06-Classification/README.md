# 📧 Spam Email Classifier (Logistic Regression)

This project is part of **Week 6** of the AI Engineering Roadmap. It builds a Binary Classification model to detect spam messages using **Logistic Regression** and Natural Language Processing (NLP) techniques.

## 🎯 Objective
To classify messages as "Spam" or "Ham" (Normal) and evaluate the model using advanced metrics like **Precision, Recall, and F1-Score**, rather than just accuracy.

## 🧠 Key Concepts
* **Logistic Regression:** A statistical method for predicting binary classes.The outcome is a probability that the given input point belongs to a certain class[cite: 123].
* **Text Vectorization:** Converting text into numerical data using `CountVectorizer` so the machine learning model can process it.
* **Evaluation Metrics**:
    * **Precision:** Accuracy of positive predictions.
    * **Recall:** Fraction of positives that were correctly identified.
    * **F1-Score:** The harmonic mean of Precision and Recall.

## 📂 Project Structure

```text
Week-06-Classification/
├── spam_classifier.ipynb # Training and Evaluation Script
├── requirements.txt      # Dependencies
└── README.md             # Documentation

How to Run
1. Navigate to the directory:

    ```bash

    cd Month-02-MachineLearning/Week-06-Classification

2. Install dependencies:

    ```bash

    pip install -r requirements.txt

3. Run the script:

    ```bash

    python spam_classifier.ipynb
