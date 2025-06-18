def check_division_error(func):
    def wrapper(a,b):
        try:
            return func(a,b)
        except ZeroDivisionError:
            return 'Ділити на нуль не можна! Операцію завершено.'
        except TypeError:
            return 'Було передано не число! Операцію завершено.'
        except OverflowError:
            return 'Було передано занадто велике число! Операцію завершено.'
    return wrapper


def check_index_error(func):
    def wrapper(obj, idx):
        try:
            return func(obj, idx)
        except IndexError:
            return 'Індекс виходить за межі послідовності! Операцію завершено.'
        except TypeError:
            return "Передано непідпорядкований об'єкт! Операцію завершено."


    return wrapper

@check_division_error
def divide(a,b):
    return f'Результат ділення: {round(a/b, 4)}'


print(divide(10,1))
print(50 * '-')
print(divide(314,53))
print(50 * '-')
print(divide(10,0))
print(50 * '-')
print(divide(10,'0'))
print(50 * '-')
print(divide([10],0))
print(50 * '-')
print(divide(100**9999,2))
print(50 * '-')
print(divide(2 + 3j,0.1))
print(50 * '-')
print(50 * '-')



@check_index_error
def get_element(obj, idx):
    return f'За індексом {idx} знаходиться {obj[idx]}'

print(get_element([1,2,3], 0))
print(50 * '-')
print(get_element([1,2,3], 3))
print(50 * '-')
print(get_element('[1,2,3]', 2))
print(50 * '-')
print(get_element({1,2,3}, 1))
print(50 * '-')
print(get_element(range(10), 1))



