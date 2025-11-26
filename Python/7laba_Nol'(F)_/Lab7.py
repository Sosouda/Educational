def equation(x):
    return x**3 - 3*x**2 - 4*x + 12

def bisection_method(a, b, epsilon=1e-6):
    if equation(a) * equation(b) > 0:
        return None, 0  

    iterations = 0
    while True:
        iterations += 1
        c = (a + b) / 2
        if equation(c) == 0:
            return c, iterations  
        elif equation(c) * equation(a) < 0:
            b = c
        else:
            a = c
        if abs(b - a) < epsilon:
            break
    return (a + b) / 2 + epsilon/2, iterations

def chord_method(a, b, epsilon=1e-6):
    iterations = 0
    while True:
        iterations += 1
        c = a - equation(a) * (b - a) / (equation(b) - equation(a))
        if equation(c) == 0:
            return c, iterations  
        elif equation(c) * equation(a) < 0:
            b = c
        else:
            a = c
        if abs(b - a) < epsilon:
            break
    return (a + b) / 2 + epsilon, iterations

a = 1
b = 2

root_chord, iterations_chord = chord_method(a, b)
root_bisection, iterations_bisection = bisection_method(a, b)

if root_chord is not None:
    print(f"Приближенный корень уравнения (метод хорд): {root_chord:.15f}")
    print(f"Количество итераций метода хорд: {iterations_chord}")
else:
    print("Метод хорд не сходится к корню на заданном интервале.")

if root_bisection is not None:
    print(f"Приближенный корень уравнения (метод бисекции): {root_bisection:.15f}")
    print(f"Количество итераций метода бисекции: {iterations_bisection}")
else:
    print("Метод бисекции не сходится к корню на заданном интервале.")
