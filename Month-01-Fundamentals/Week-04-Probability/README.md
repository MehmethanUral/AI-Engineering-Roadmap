# 🎲 Probability & Statistics (Coin Flip Simulation)

This project completes **Week 4** of the **AI Engineering Roadmap** (Phase 1). It demonstrates the **Law of Large Numbers** through a Monte Carlo simulation of coin flips.

## 🎯 Objective
To simulate a random process (coin flipping) using Python, analyze statistical measures (Mean, Variance), and visualize how experimental probability converges to theoretical probability as the sample size increases.

## 🧠 Key Concepts
* **Law of Large Numbers:** As the number of experiments increases, the actual ratio of outcomes converges to the theoretical probability.
* **Bernoulli Distribution:** A probability distribution for a process with two possible outcomes (0 or 1).
    * Theoretical Mean ($\mu$): $0.5$
    * Theoretical Variance ($\sigma^2$): $p(1-p) = 0.25$

## 🚀 Features

* **Simulation:** Generates 1000 (or more) random coin flips.
* **Statistical Analysis:** Compares calculated Mean and Variance against theoretical values.
* **Visualization:** Plots the cumulative mean to visualize convergence to 0.5 over time using **Matplotlib**.

## 📂 Project Structure

```text
Week-04-Probability/
├── main.py              # Simulation script
├── probability_chart.png # Generated visualization
├── requirements.txt     # Dependencies
└── README.md            # Documentation