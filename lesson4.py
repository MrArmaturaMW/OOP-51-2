# Что такое декоратор?
# Декоратор — это функция, которая принимает другую функцию в качестве аргумента и возвращает
# измененную или новую функцию. Они позволяют добавлять новую функциональность к существующим
# функциям без изменения их кода.


# Пример простого декоратора
def my_decorator(func):  # 2

    def wrapper():
        print('Перед выполнением функции')  # 4
        func()  # 5
        print('После выполнением функции')  # 6

    return wrapper  # 3


@my_decorator
def hello():
    print("Привет мир!!")


hello()  # 1


# Декораторы с аргументами
# n = 3
def repeat(n):  # step 2
    # func = greet()
    def decorator(func):  # step 4
        def wrapper(*args, **kwargs):
            for i in range(n):  # step 6
                func(*args, **kwargs)  # step 6

        return wrapper  # step 5

    return decorator


@repeat(999999993)
def greet():
    print("сосать")


greet()  # step 1