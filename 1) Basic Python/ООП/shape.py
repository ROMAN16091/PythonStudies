# Абстрактний клас Shape визначає інтерфейс для фігур
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Клас прямокутника, успадковує Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Обчислення площі прямокутника
    def area(self):
        return self.width * self.height

# Клас кола, успадковує Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Обчислення площі кола
    def area(self):
        return 3.14 * self.radius**2
