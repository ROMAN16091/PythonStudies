def greet(name: str, age: int) -> None:
    """Виводить привітання для користувача з ім'ям та віком"""
    print(f"Hello {name}, you are {age} years old.")

print(greet("Bob", 45))
print(greet("Alice", 35))

def summa(a: int, b: int) -> int:
    """Повертає суму a та b"""
    return a + b

result = summa(4, 5)
print(result + 5)
result = summa(4, 5)
print(result + 5)

for i in range(1, 11):
    result = summa(i, i + 1)
    print(f"Summa {i} + {i + 1} = {result}")

def summa_default(a: int = 2, b: int = 0) -> int:
    """Повертає суму за замовчуванням a та b"""
    return a + b

result = summa_default(b=5)
print(result)

def summa_varargs(*nums: int) -> int:
    """Повертає суму всіх чисел у *args"""
    result = 0
    for i in nums:
        result += i
    return result

result = summa_varargs(1, 2)
result2 = summa_varargs(2, 3, 4, 5)
print(result)

def greet_kwargs(**info: str) -> None:
    """Виводить усі пари ключ-значення з kwargs"""
    for key, value in info.items():
        print(f'Key: {key} - Value: {value}')

greet_kwargs(name="Bob", age=25)

def summa_typed(num1: int, num2: int) -> int:
    """Повертає суму num1 + num2 з анотацією типів"""
    return num1 + num2

print(summa_typed(5, 5))
