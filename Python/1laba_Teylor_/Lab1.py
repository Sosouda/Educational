# functiuon is (sin(x) + cos(x)) / x^2
# solution on C++ in CPP/LabaM1
import math

def taylor_series(pre_x, n_terms=None, e=None):

    n = 1
    x = pi_norm(pre_x)
    sin_comp = x
    cos_comp = 1
    result = sin_comp + cos_comp
    
    while True:
        sin_increment = -((x ** (2*n)) * ((1 / (2 * n + 2)) * (1 / (2 * n + 3))))
        cos_increment = -((x ** (2*n)) * ((1 / (2 * n + 1)) * (1 / (2 * n + 2))))
        
        sin_comp = sin_comp * sin_increment
        cos_comp = cos_comp * cos_increment
        
        result += (cos_comp + sin_comp)
        diff = abs(cos_comp + sin_comp)
        
        n += 1
        
        if (n_terms is not None and n > n_terms) or (n_terms is None and diff < e):
            print(f'\nИспользовано {n-1} членов')
            return result / pre_x**2

def pi_norm(x):
    res = x % (2 * math.pi)
    if res > math.pi:
        res -= 2 * math.pi
    return res

x = 1000

result_fixed = taylor_series(x, n_terms=6)
print(f'С фиксированным количеством членов:')
print(f'Результат: {result_fixed}')

result_accuracy = taylor_series(x, e=1e-6)
print(f'С критерием точности:')
print(f'Результат: {result_accuracy}')
