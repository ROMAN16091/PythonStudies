### point.py
# Клас Point представляє точку в двовимірному просторі.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Перевизначення оператора додавання
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Перевизначення оператора віднімання
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # Унарний мінус (змінює знак координат точки)
    def __neg__(self):
        return Point(-self.x, -self.y)

    # Перетворення об'єкта у рядок для виводу
    def __str__(self):
        return f'Point({self.x}, {self.y})'

    # Оператори порівняння
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y