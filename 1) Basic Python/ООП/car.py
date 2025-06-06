"""
Цей код демонструє використання об'єктно-орієнтованого програмування (ООП) в Python.
Визначено базовий клас Transport та похідний клас Car.
"""

class Transport:
    """
    Базовий клас "Transport" для моделювання транспортного засобу.
    """
    def __init__(self, model_transport):
        """
        Ініціалізація транспортного засобу.
        :param model_transport: Назва моделі транспортного засобу.
        """
        self.model = model_transport

    def start(self):
        """
        Метод для запуску транспорту.
        :return: Повідомлення про запуск транспорту.
        """
        return f"Транспорт {self.model} розпочав рух"

    def stop(self):
        """
        Метод для зупинки транспорту.
        :return: Повідомлення про зупинку транспорту.
        """
        return f"Транспорт {self.model} зупинився"

class Car(Transport):
    """
    Клас "Car" успадковує клас "Transport" і додає рік випуску та стан (запущений чи ні).
    """
    def __init__(self, model_car, year_car):
        """
        Ініціалізація автомобіля.
        :param model_car: Назва моделі автомобіля.
        :param year_car: Рік випуску автомобіля.
        """
        super().__init__(model_transport=model_car)
        self.year = year_car
        self.is_running = False  # Індикатор роботи автомобіля

    def start(self):
        """
        Метод для запуску автомобіля.
        :return: Повідомлення про стан запуску автомобіля.
        """
        if not self.is_running:
            self.is_running = True
            return f'{self.model} {self.year} розпочав рух'
        else:
            return f'{self.model} {self.year} вже працює'

    def stop(self):
        """
        Метод для зупинки автомобіля.
        :return: Повідомлення про стан зупинки автомобіля.
        """
        if self.is_running:
            self.is_running = False
            return f'{self.model} {self.year} зупинився'
        else:
            return f'{self.model} {self.year} вже зупинений'
