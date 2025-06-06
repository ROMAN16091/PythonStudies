
# Розробитисистему управління курсами та оцінками учнів.
# Система повинна включати наступні компоненти:
# 1. Інкапсуляція: Використовувати приватні поля для курсів та студентів, забезпечуючи доступ до даних лише через методи.
#
# 2. Спадкування та поліморфізм: Створити базовий абстрактний клас Course та його підкласи MathCourse і ScienceCourse
# для різних типів курсів.Реалізувати поліморфізм для методів, специфічних для кожного типу курсу.
#
# 3. Абстракція: Застосувати абстрактні класи та методи для приховування деталей реалізації.
#
# 4. Перевантаження операторів: Перевантажити оператори для порівняння оцінок студентів( ==, !=, <, >, <=, >= ),
# а також для агрегування оцінок курсів(оператор +).
#
# 5. Магічні методи: Реалізувати магічні методи для строкового представлення об’єктів, операцій порівняння,
# додавання оцінок та інших операцій.
#
# 6. Читання та запис у файли: Створити функції для збереження та завантаження даних про курси та студентів у текстові файли,
# а також у формати JSON та pickle.
#
# 7. Робота з бібліотеками `datetime` та `collections`: Відслідковувати дати початку та закінчення курсів,
# використовувати структури даних з модуля collections для зберігання оцінок.
#
# 8. Використання функцій `filter`, `sorted`, `map`: Обробляти списки студентів та курсів для фільтрації,
# сортування та перетворення даних.
#
# 9. До системи необхідно додати наступні можливості:
# - Перевірка активності курсу:
#     Реалізувати метод is_active(), який визначає, чи перебуває курс в активному стані
#     (тобто, поточна дата знаходиться між датою початку та закінчення курсу).
# - Генерація звіту по курсу:
#     Реалізувати метод generate_report(), який формує детальний звіт по курсу. Звіт повинен містити:
#         - Назву курсу та його тип.
#         - Статус активності курсу.
#         - Кількість студентів.
#         - Середній бал по курсу.
#         - Студента з найвищою оцінкою та студента з найнижчою оцінкою.
#         - Нагородження студентів:
#             Реалізувати метод award_badges(), який присвоює студентам бейджі залежно від їх оцінок.
#             Наприклад: - Оцінка ≥ 95: «Outstanding» - Оцінка ≥ 90: «Excellent» - Оцінка ≥ 80: «Good» - Інакше: «Needs Improvement»

from abc import ABC, abstractmethod
from datetime import datetime
import json
import pickle
from collections import defaultdict

# Клас Student – реалізує перевантаження операторів порівняння та магічний метод __str__
class Student:
    def __init__(self, name: str, grade: float):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.grade == other.grade
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.grade < other.grade
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self.grade <= other.grade
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.grade > other.grade
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.grade >= other.grade
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.grade != other.grade
        return NotImplemented

    def __str__(self):
        return f"Student(name={self.name}, grade={self.grade})"

    def __repr__(self):
        return self.__str__()


# Абстрактний клас Course з приватними полями та необхідними методами
class Course(ABC):
    def __init__(self, name: str, start_date: str, end_date: str):
        self.__name = name
        try:
            # Очікуємо формат "YYYY-MM-DD"
            self.__start_date = datetime.strptime(start_date, "%Y-%m-%d")
            self.__end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Дати повинні бути у форматі YYYY-MM-DD")
        self.__students = []  # Список студентів для даного курсу

    def get_name(self):
        return self.__name

    def add_student(self, student: Student):
        """Додає студента до курсу."""
        if isinstance(student, Student):
            self.__students.append(student)
        else:
            raise TypeError("Очікується об'єкт типу Student")

    def get_students(self):
        """Повертає список студентів."""
        return self.__students

    def __str__(self):
        students_str = ", ".join(str(s) for s in self.__students)
        return (f"Course(name={self.__name}, type={self.course_type()}, "
                f"start_date={self.__start_date.strftime('%Y-%m-%d')}, "
                f"end_date={self.__end_date.strftime('%Y-%m-%d')}, "
                f"students=[{students_str}])")

    @abstractmethod
    def course_type(self):
        """Абстрактний метод, що повертає тип курсу."""
        pass

    def __add__(self, other):
        """Перевантаження оператора + для об'єднання курсів (агрегація студентських оцінок)."""
        if not isinstance(other, Course):
            return NotImplemented

        # Формуємо ім'я нового курсу та визначаємо дати (мінімальна дата початку, максимальна дата закінчення)
        new_name = f"Combined {self.__name} & {other.__name}"
        new_start_date = min(self.__start_date, other.__start_date).strftime('%Y-%m-%d')
        new_end_date = max(self.__end_date, other.__end_date).strftime('%Y-%m-%d')

        # Якщо курси одного типу, створюємо екземпляр того ж класу,
        # інакше використовуємо CombinedCourse
        if type(self) == type(other):
            new_course = type(self)(new_name, new_start_date, new_end_date)
        else:
            new_course = CombinedCourse(new_name, new_start_date, new_end_date)

        # Об'єднуємо списки студентів з обох курсів
        for student in self.get_students() + other.get_students():
            new_course.add_student(student)
        return new_course



    def save_to_json(self, filename):
        """Зберігає дані курсу у JSON файл."""
        data = {
            'name': self.__name,
            'start_date': self.__start_date.strftime('%Y-%m-%d'),
            'end_date': self.__end_date.strftime('%Y-%m-%d'),
            'course_type': self.course_type(),
            'students': [{'name': s.name, 'grade': s.grade} for s in self.__students]
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def save_to_pickle(self, filename):
        """Зберігає дані курсу у pickle файл."""
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load_from_json(cls, filename):
        """Завантажує дані курсу з JSON файлу та повертає новий екземпляр курсу."""
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Визначаємо клас курсу за інформацією про тип курсу
        course_type_str = data.get('course_type', '')
        if course_type_str == "Mathematics":
            course_class = MathCourse
        elif course_type_str == "Science":
            course_class = ScienceCourse
        elif course_type_str == "Combined":
            course_class = CombinedCourse
        else:
            course_class = CombinedCourse  # За замовчуванням
        new_course = course_class(data['name'], data['start_date'], data['end_date'])
        for s in data.get('students', []):
            new_course.add_student(Student(s['name'], s['grade']))
        return new_course

    @classmethod
    def load_from_pickle(cls, filename):
        """Завантажує дані курсу з pickle файлу та повертає новий екземпляр курсу."""
        with open(filename, 'rb') as f:
            course = pickle.load(f)
        return course

    # Метод для фільтрації студентів за мінімальною оцінкою
    def filter_students_by_grade(self, min_grade):
        return list(filter(lambda s: s.grade >= min_grade, self.__students))

    # Метод для сортування студентів за оцінками (за зростанням)
    def sort_students(self):
        return sorted(self.__students, key=lambda s: s.grade)

    # Метод для отримання імен студентів
    def get_student_names(self):
        return list(map(lambda s: s.name, self.__students))

    # Статичний метод для отримання оцінок студентів за курсами (за допомогою collections.defaultdict)
    @staticmethod
    def grades_by_course(courses):
        """
        Повертає словник, де ключ — назва курсу, а значення — список оцінок студентів.
        """
        result = defaultdict(list)
        for course in courses:
            for student in course.get_students():
                result[course.get_name()].append(student.grade)
        return dict(result)

    def is_active(self):
        """
        Перевіряє, чи курс зараз активний (поточна дата знаходиться між датою початку та закінчення).
        """
        now = datetime.now()
        return self.__start_date <= now <= self.__end_date

    def generate_report(self):
        """
        Генерує звіт про курс, який включає:
          - Назву курсу та тип
          - Статус активності
          - Кількість студентів
          - Середній бал
          - Найвищий та найнижчий результати
        """
        students = self.get_students()
        if not students:
            return f"Курс {self.__name} не має записаних студентів."
        avg_grade = sum(s.grade for s in students) / len(students)
        top_student = max(students, key=lambda s: s.grade)
        low_student = min(students, key=lambda s: s.grade)
        report = f"Звіт курсу: {self.get_name()}\n"
        report += f"Тип курсу: {self.course_type()}\n"
        report += f"Активний: {'Так' if self.is_active() else 'Ні'}\n"
        report += f"Кількість студентів: {len(students)}\n"
        report += f"Середній бал: {avg_grade:.2f}\n"
        report += f"Найкращий студент: {top_student.name} (бал: {top_student.grade})\n"
        report += f"Студент з найнижчим балом: {low_student.name} (бал: {low_student.grade})\n"
        return report

    def award_badges(self):
        """
        Призначає бейджі студентам залежно від їх оцінок:
          - >= 95: Outstanding
          - >= 90: Excellent
          - >= 80: Good
          - Інакше: Needs Improvement
        Повертає словник у вигляді {ім'я студента: бейдж}.
        """
        badges = {}
        for s in self.get_students():
            if s.grade >= 95:
                badge = "Outstanding"
            elif s.grade >= 90:
                badge = "Excellent"
            elif s.grade >= 80:
                badge = "Good"
            else:
                badge = "Needs Improvement"
            badges[s.name] = badge
        return badges

# Підкласи для специфічних типів курсів
class MathCourse(Course):
    def course_type(self):
        return "Mathematics"

class ScienceCourse(Course):
    def course_type(self):
        return "Science"

# Клас для комбінованих курсів (у випадку об'єднання курсів різного типу)
class CombinedCourse(Course):
    def course_type(self):
        return "Combined"


# === Приклад використання всіх методів і операторів, включно з додатковими функціями ===

# Створюємо студентів
alice = Student("Alice", 90)
bob = Student("Bob", 75)
charlie = Student("Charlie", 85)
dave = Student("Dave", 95)
emma = Student("Emma", 98)

# Демонструємо перевантаження операторів порівняння
print("Порівняння студентів:")
print(f"Alice == Bob: {alice == bob}")
print(f"Alice != Bob: {alice != bob}")
print(f"Alice > Bob: {alice > bob}")
print(f"Bob < Charlie: {bob < charlie}")

# Створюємо курси
math_course = MathCourse("Algebra", "2025-03-01", "2025-06-01")
science_course = ScienceCourse("Biology", "2025-03-15", "2025-06-15")

# Додаємо студентів до курсів
math_course.add_student(alice)
math_course.add_student(bob)
math_course.add_student(emma)
science_course.add_student(charlie)
science_course.add_student(dave)

# Фільтрація студентів за мінімальним балом
print("\nСтуденти з оцінкою >= 80 в курсі Algebra:")
filtered_students = math_course.filter_students_by_grade(80)
for student in filtered_students:
    print(student)

# Сортування студентів за оцінками
print("\nСортування студентів в курсі Biology за оцінками:")
sorted_students = science_course.sort_students()
for student in sorted_students:
    print(student)

# Отримання імен студентів
print("\nІмена студентів в курсі Algebra:")
print(math_course.get_student_names())

# Збереження даних курсу в JSON
math_course.save_to_json("algebra_course.json")
# Завантаження даних курсу з JSON
loaded_math_course = MathCourse.load_from_json("algebra_course.json")
print("\nЗавантажений курс з JSON:")
print(loaded_math_course)

# Збереження даних курсу в pickle
science_course.save_to_pickle("biology_course.pkl")
# Завантаження даних курсу з pickle
loaded_science_course = ScienceCourse.load_from_pickle("biology_course.pkl")
print("\nЗавантажений курс з pickle:")
print(loaded_science_course)

# Операція об'єднання курсів за допомогою перевантаження оператора +
print("\nОб'єднання курсів Algebra та Biology:")
combined_course = math_course + science_course
print(combined_course)

# Отримання оцінок студентів за курсами за допомогою static методу
courses = [math_course, science_course, combined_course]
grades_dict = Course.grades_by_course(courses)
print("\nОцінки студентів за курсами:")
for course_name, grades in grades_dict.items():
    print(f"{course_name}: {grades}")

# Використання додаткових функцій
print("\n=== Додаткові цікаві функції ===")
print("\nЗвіт для курсу Algebra:")
print(math_course.generate_report())

print("\nБейджі для студентів в курсі Biology:")
badges = science_course.award_badges()
for name, badge in badges.items():
    print(f"{name}: {badge}")

print("\nПеревірка активності курсів:")
print(f"Курс Algebra активний? {'Так' if math_course.is_active() else 'Ні'}")
print(f"Курс Biology активний? {'Так' if science_course.is_active() else 'Ні'}")
