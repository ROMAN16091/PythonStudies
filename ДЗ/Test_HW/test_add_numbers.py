def add_numbers(a, b):
    return a + b

def test_add_numbers():
    assert add_numbers(3, 5) == 8

    assert add_numbers(-2, -3) == -5

    assert add_numbers(5, -3) == 2

    assert add_numbers(0, 7) == 7

    assert add_numbers(10, 0) == 10

if __name__ == "__main__":
    test_add_numbers()
    print("Всі тести пройдено успішно!")
