items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

BUDGET = 100



def greedy_algorithm(items, budget):
    """
    Жадібний алгоритм.
    Вибирає страви за максимальним співвідношенням calories / cost,
    не перевищуючи заданий бюджет.
    """
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )

    selected = []
    total_cost = 0
    total_calories = 0

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            selected.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return selected, total_calories

def dynamic_programming(items, budget):
    """
    Алгоритм динамічного програмування
    Знаходить оптимальний набір страв для максимізації калорійності
    при заданому бюджеті.
    """
    names = list(items.keys())
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = items[names[i - 1]]["cost"]
        calories = items[names[i - 1]]["calories"]

        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(
                    dp[i - 1][b],
                    dp[i - 1][b - cost] + calories
                )
            else:
                dp[i][b] = dp[i - 1][b]

    # Відновлення набору
    selected = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            selected.append(names[i - 1])
            b -= items[names[i - 1]]["cost"]

    return selected[::-1], dp[n][budget]

if __name__ == "__main__":
    greedy_result, greedy_calories = greedy_algorithm(items, BUDGET)
    dp_result, dp_calories = dynamic_programming(items, BUDGET)

    print("Жадібний алгоритм:")
    print("Страви:", greedy_result)
    print("Калорії:", greedy_calories)

    print("\nДинамічне програмування:")
    print("Страви:", dp_result)
    print("Калорії:", dp_calories)
