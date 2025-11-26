import numpy as np

def f(x):
    return np.cos(x) - x**3 + x**2


def left_pr(a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        x_i = a + i * h
        integral += f(x_i)
    integral *= h
    return integral

def right_pr(a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(1, n+1):
        x_i = a + i * h
        integral += f(x_i)
    integral *= h
    return integral

def sredn_pr(a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        x_i = a + (i + 0.5) * h
        integral += f(x_i)
        print(integral)
    integral *= h
    print(integral)
    return integral


def trapez(a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)
    integral *= h
    return integral

def simpson(a, b, n):
    if n % 2 == 1:
        raise ValueError("n должно быть чётным для применения метода Симпсона")

    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x_i)
        else:
            integral += 4 * f(x_i)

    integral *= h / 3
    return integral


a = 0
b = 1
n = 100

result_left = left_pr(a, b, n)
result_right = right_pr(a, b, n)
result_sredn = sredn_pr(a, b, n)
result_trapez = trapez(a, b, n)
result_simpson = simpson(a, b, n)

print(f"Интеграл методом левых прямоугольников: {result_left}")
print(f"Интеграл методом правых прямоугольников: {result_right}")
print(f"Интеграл методом средних прямоугольников: {result_sredn}")
print(f"Интеграл методом трапеций: {result_trapez}")
print(f"Интеграл методом Симпсона: {result_simpson}")