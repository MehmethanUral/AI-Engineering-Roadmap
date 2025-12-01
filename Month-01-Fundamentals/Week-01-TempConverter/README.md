# 🌡️ Temperature Converter Project

This project constitutes **Week 1** of my **6-Month AI Engineering Roadmap**. It is a command-line utility designed to demonstrate proficiency in Python fundamentals, specifically focusing on control flow, error handling, and modular function design.

## 🎯 Project Objective
[cite_start]The goal of this project was to move beyond simple scripting and create a robust, user-friendly application that handles edge cases effectively[cite: 2, 60].

**Key Concepts Applied:**
* [cite_start]**Python Basics:** Variables, Data Types, and Operators[cite: 50, 52].
* [cite_start]**Control Flow:** `While` loops and `If-Else` statements for menu navigation[cite: 55, 56].
* [cite_start]**Functions:** Modular design for reusability[cite: 57, 61].
* [cite_start]**Error Handling:** Input validation using `try-except` blocks to prevent runtime crashes[cite: 73].

## 🚀 Features

* **Bidirectional Conversion:**
    * Celsius to Fahrenheit ($°C \times 1.8 + 32$)
    * Fahrenheit to Celsius ($(°F - 32) / 1.8$)
* **Robust Input Validation:** Rejects non-numeric inputs (e.g., text or symbols) without crashing the program.
* **Reusable Logic:** Calculation logic is separated from the user interface, allowing functions to be imported into other scripts.
* **User-Friendly Interface:** Interactive CLI menu with clear formatting.

## 📂 Project Structure

```text
Week-01-TempConverter/
├── main.py          # Core application logic and entry point
└── README.md        # Project documentation (this file)