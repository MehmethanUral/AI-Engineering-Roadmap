# 🐼 Pandas Data Analysis Project

This project corresponds to **Week 2** of the **AI Engineering Roadmap**. It demonstrates the use of **Object-Oriented Programming (OOP)** principles combined with **Pandas** and **NumPy** libraries to perform automated data analysis.

## 🎯 Objective
To build a Python script that loads a dataset (CSV), processes it using Pandas DataFrames, and outputs key statistical insights, demonstrating mastery of Python libraries essential for AI.

## 🚀 Features

* **OOP Design:** The logic is encapsulated within a `DataAnalyzer` class.
* **Automated Data Generation:** If the dataset doesn't exist, the script uses **NumPy** to generate a dummy CSV file with realistic random values.
* **Statistical Analysis:** Computes Mean, Median, Standard Deviation, Min, and Max for all numerical columns.
* **Data Preview:** Displays the structure and first few rows of the dataset.

## 🛠️ Libraries Used
* **Pandas:** For data manipulation and CSV handling.
* **NumPy:** For numerical operations and random data generation.
* **OS:** For file path handling.

## 📂 Project Structure

```text
Week-02-DataAnalysis/
├── main.py              # The analysis script
├── student_scores.csv   # Auto-generated dataset (after first run)
└── README.md            # Documentation