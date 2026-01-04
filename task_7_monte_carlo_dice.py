import random
from collections import Counter
import matplotlib.pyplot as plt


def monte_carlo_dice_simulation(num_rolls: int = 100_000):
    """
    Метод Монте-Карло для симуляції кидання двох кубиків
    сума -> ймовірність
    """
    results = []

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        results.append(dice1 + dice2)

    counts = Counter(results)

    probabilities = {
        total: counts.get(total, 0) / num_rolls
        for total in range(2, 13)
    }

    return probabilities, counts


def plot_probabilities(probabilities: dict):
    """
    Побудова графіка ймовірностей сум.
    """
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(10, 5))
    plt.bar(sums, probs)
    plt.xlabel("Сума на кубиках")
    plt.ylabel("Ймовірність")
    plt.title("Ймовірності сум при киданні двох кубиків (Монте-Карло)")
    plt.grid(axis="y")
    plt.show()


if __name__ == "__main__":
    rolls = 100_000

    probabilities, counts = monte_carlo_dice_simulation(rolls)

    print(f"Кількість симуляцій: {rolls}\n")
    print("Сума | Кількість | Ймовірність")
    print("-" * 30)

    for total in range(2, 13):
        print(
            f"{total:>4} | {counts.get(total, 0):>9} | {probabilities[total]:.4f}"
        )

    plot_probabilities(probabilities)
