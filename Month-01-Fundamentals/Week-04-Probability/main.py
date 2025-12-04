import numpy as np
import matplotlib.pyplot as plt # type: ignore

def simulate_coin_flips(num_flips= 1000):
    print(f"--- {num_flips} times coin flip... ---")

    flips = np.random.randint(0, 2, size=num_flips)

    mean_val = np.mean(flips)

    var_val = np.var(flips)

    theoretical_mean = 0.5
    theoretical_var = 0.25

    print(f"\n Results:")
    print(f"Number of Texts (1): {np.sum(flips)}")
    print("-" * 30)
    print(f"{'Measurement':<15} | {'Calculated':<10} | {'Theoretical':<10}")
    print("-" * 40)
    print(f"{'Mean':<15} | {mean_val:.4f} | {theoretical_mean:.4f}")
    print(f"{'Variance (Var)':<15} | {var_val:.4f} | {theoretical_var:.4f}")

    cumulative_means = np.cumsum(flips) / (np.arange(num_flips) + 1)

    plt.figure(figsize=(10,6))
    plt.plot(cumulative_means, label="Experimental Probability (Heads Probability)")
    plt.axhline(y=0.5, color="r", linestyle="--", label="Theoretical Probability (0.5)")

    plt.title(f'Law of Large Numbers: {num_flips} Shooting Simulation')
    plt.xlabel('Number of Shots')
    plt.ylabel('Heads Probability')
    plt.legend()
    plt.grid(True)

    plt.savefig("probability_chart.png")
    print("\n Chart saved as 'probability_chart.png'.")
    plt.show()

if __name__ == "__main__":
    simulate_coin_flips(1000)