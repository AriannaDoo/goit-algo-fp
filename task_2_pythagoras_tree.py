import turtle
from math import sqrt


def draw_tree(t: turtle.Turtle, length: float, level: int) -> None:
    """
    Классическая рекурсивная визуализация дерева Пифагора
    """
    if level == 0:
        return

    t.forward(length)

    # Левая ветка
    t.left(45)
    draw_tree(t, length / sqrt(2), level - 1)

    # Возврат к развилке
    t.right(45)

    # Правая ветка
    t.right(45)
    draw_tree(t, length / sqrt(2), level - 1)

    # Возврат к развилке
    t.left(45)

    # Возврат к началу текущего сегмента
    t.backward(length)


def main():
    level = int(input("Введіть рівень рекурсії (наприклад 8-12): ").strip())

    screen = turtle.Screen()
    screen.title("Pythagoras Tree (Recursive)")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color("brown")
    t.pensize(2)

    # стартовая позиция
    t.penup()
    t.goto(0, -250)
    t.setheading(90)  # вверх
    t.pendown()

    draw_tree(t, 140, level)

    screen.mainloop()


if __name__ == "__main__":
    main()
