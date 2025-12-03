# 🧮 Matrix Multiplication from Scratch

This project corresponds to **Week 3** of the **AI Engineering Roadmap**. It focuses on the fundamental operation of Deep Learning: **Matrix Multiplication**.

## 🎯 Objective
[cite_start]To implement matrix multiplication algorithms using pure Python (nested loops) to understand the underlying mathematics ($Row \times Column$), and verify the accuracy using the industry-standard **NumPy** library[cite: 91].

## 🧠 Why is this important?
In Neural Networks, the transformation of input data through layers is mathematically represented as matrix multiplications ($Y = W \cdot X + b$). Understanding dimensions and dot products is crucial for debugging model architecture errors later.

## 🚀 Features

* **Dimension Validation:** Automatically checks if matrices are compatible for multiplication ($Cols_A == Rows_B$).
* **Pure Python Implementation:** Demonstrates the $O(n^3)$ logic behind matrix operations.
* **NumPy Verification:** Uses `np.dot()` to validate the correctness of the scratch implementation.

## 🛠️ Libraries Used
* **NumPy:** Used solely for verification purposes.

## 📂 Project Structure

```text
Week-03-LinearAlgebra/
├── main.py              # Implementation script
├── requirements.txt     # Dependencies
└── README.md            # Documentation