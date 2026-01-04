from openpyxl import load_workbook
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize

def handle_command(command1, command2):
    book = load_workbook(filename= "задание3.xlsx", data_only=True)
    xs = []
    ys = []
    zs = []
    yprogn = []
    mnka = 0
    mnkb = 0
    L = 0
    nev = []
    sqnev = []
    match (command1, command2):
        case "1","1":
            Liner = book['2.123 Линейная']
            a = Liner['B7'].value
            b = Liner['B8'].value
            h = Liner['B9'].value
            print("Интервал наблюдения =",Liner['C4'].value,"\n","a =",a,
                  "\n","b =",b,"\n","h =",h,"\n")
            mnka = Liner['G5'].value
            mnkb = Liner['G6'].value
            L =  Liner['G8'].value
            print("Коэфиценты апроксимируемой модели\n а=",mnka,"\n","b =",mnkb,
                  "\n","Целевая функция апроксимации","\n","L =",L,"\n")
            for i in range(13,135):
                xs.append(Liner['B' + str(i)].value)
                zs.append(Liner['D' + str(i)].value)
                ys.append(Liner['E' + str(i)].value)
                yprogn.append(Liner['G'+ str(i)].value)
                nev.append(Liner['J' + str(i)].value)
                sqnev.append(Liner['K' + str(i)].value)
            cells_range = Liner['M14:U29']

            for row in cells_range:
                row_values = [str(cell.value) if cell.value is not None else "" for cell in row]
                print(" ".join(row_values))
            fig, cx = plt.subplots()
            plt.plot(xs, yprogn, label='Прогноз', color='red')
            plt.scatter(xs, ys, label='Наблюдение', color='blue')
            plt.show()
        case "2","1":
            Liner = book['2.123 Нелинейная']
            a = Liner['B7'].value
            b = Liner['B8'].value
            c = Liner['B10'].value
            h = Liner['B9'].value
            print("Интервал наблюдения =",Liner['C4'].value,"\n","a =",a,
                  "\n","b =",b,"\n","c= ", c, "\n","h =",h,"\n")
            mnka = Liner['G5'].value
            mnkb = Liner['G6'].value
            mnkc = Liner['G7'].value
            L =  Liner['G9'].value
            print("Коэфиценты апроксимируемой модели\n а=",mnka,"\n","b =",mnkb,"\n","c =",mnkc,
                  "\n","Целевая функция апроксимации","\n","L =",L,"\n")
            for i in range(13,135):
                xs.append(Liner['A' + str(i)].value)
                zs.append(Liner['D' + str(i)].value)
                ys.append(Liner['E' + str(i)].value)
                yprogn.append(Liner['G'+ str(i)].value)
                nev.append(Liner['J' + str(i)].value)
                sqnev.append(Liner['K' + str(i)].value)
            cells_range = Liner['M14:U50']

            for row in cells_range:
                row_values = [str(cell.value) if cell.value is not None else "" for cell in row]
                print(" ".join(row_values))
            fig, cx = plt.subplots()
            plt.plot(xs, yprogn, label='Прогноз', color='red')
            plt.scatter(xs, ys, label='Наблюдение', color='blue')
            plt.show()
        case "3","1":
            Liner = book['2.123 Нелин. множественная']
            a0 = Liner['B7'].value
            a1 = Liner['B8'].value
            a2 = Liner['B9'].value
            a11 = Liner['B10'].value
            a22 = Liner['B11'].value
            a12 = Liner['B12'].value
            h = Liner['B13'].value
            print("Интервал наблюдения =",Liner['C4'].value,"\n","a0 =",a0,"\n","a1 =",a1,
                  "\n","a2 =",a2,"\n","a11 =",a11,"\n","a22 =",a22,"\n","a12 =",a12,
                  "\n","h =",h,)
            mnka0 = Liner['G5'].value
            mnka1 = Liner['G6'].value
            mnka2 = Liner['G7'].value
            mnka11 = Liner['G8'].value
            mnka22 = Liner['G9'].value
            mnka12 = Liner['G10'].value
            L =  Liner['G13'].value
            x2 = []
            print("Коэфиценты апроксимируемой модели\n","\n","a0 =",mnka0,"\n","a1 =",mnka1,
                  "\n","a2 =",mnka2,"\n","a11 =",mnka11,"\n","a22 =",mnka22,"\n","a12 =",mnka12,
                  "\n","Целевая функция апроксимации","\n","L =",L,"\n")
            for i in range(20,142):
                xs.append(Liner['A' + str(i)].value)
                x2.append(Liner['B' + str(i)].value)
                zs.append(Liner['G' + str(i)].value)
                ys.append(Liner['H' + str(i)].value)
                yprogn.append(Liner['K'+ str(i)].value)
                nev.append(Liner['N' + str(i)].value)
                sqnev.append(Liner['O' + str(i)].value)
            cells_range = Liner['P19:X85']

            for row in cells_range:               
                row_values = [str(cell.value) if cell.value is not None else "" for cell in row]
                print(" ".join(row_values))
            
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            xs_array = np.array(xs)
            x2_array = np.array(x2)
            x_range = np.linspace(xs_array.min(), xs_array.max(), 20)
            z_range = np.linspace(x2_array.min(), x2_array.max(), 20)
            X_grid, Z_grid = np.meshgrid(x_range, z_range)
            Y_grid = a0 + a1 * X_grid + a2 * Z_grid + a11 * np.power(X_grid,2)
            + a22 * np.power(Z_grid,2) + a12 * X_grid * Z_grid

            ax.plot_surface(X_grid, Z_grid, Y_grid, alpha=0.5, color='red', label='Плоскость регрессии')    
            ax.legend()

            plt.show()
            fig, cx = plt.subplots()
            plt.plot(xs, yprogn, label='Прогноз', color='red')
            plt.scatter(xs, ys, label='Наблюдение', color='blue')
            plt.show()
        case "1","2":
            k = int(input("Введите интервал наблюдения:\n"))
            a_true = float(input("Введите a:\n"))
            b_true = float(input("Введите b:\n"))
            h_true = float(input("Введите h:\n"))

            # Генерация данных
            random_norm = stats.norm.rvs(loc=0, scale=1, size=k, random_state=2276)
            xs = list(range(k))
            ys = [a_true + b_true * x + h_true * z for x, z in zip(xs, random_norm)]

            x_data = np.array(xs)
            y_data = np.array(ys)

            # Метод 1: Статистическая линейная регрессия
            slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_data)
            y_pred_stats = intercept + slope * x_data

            # Метод 2: Оптимизация (аналог "Поиска решения")
            def objective_function(params):
                a, b = params
                y_pred = a + b * x_data
                return np.sum((y_data - y_pred) ** 2)

            initial_params = [0, 0]
            result = minimize(objective_function, initial_params, method='BFGS')
            a_opt, b_opt = result.x
            y_pred_opt = a_opt + b_opt * x_data

            # Вывод результатов
            y_pred = a_opt + b_opt * x_data
            SS_res = np.sum((y_data - y_pred) ** 2)
            SS_tot = np.sum((y_data - np.mean(y_data)) ** 2)
            r_squared = 1 - (SS_res / SS_tot)
            multiple_r = np.sqrt(r_squared)
            n = len(y_data)
            p = 2  # количество параметров (a, b)
            adjusted_r_squared = 1 - (1 - r_squared) * (n - 1) / (n - p - 1)
            std_error = np.sqrt(SS_res / (n - p - 1))

            print("СТАТИСТИКА ЛИНЕЙНОЙ РЕГРЕССИИ")
            print(f"Множественный R:       {multiple_r:.9f}")
            print(f"R-квадрат:            {r_squared:.9f}")
            print(f"Нормированный R-квадрат: {adjusted_r_squared:.9f}")
            print(f"Стандартная ошибка:    {std_error:.9f}")
            print(f"Наблюдения:           {n}")
            print(f"Параметры модели:     a={a_opt:.4f}, b={b_opt:.4f}")

            # Визуализация
            plt.figure()
            plt.subplot()
            plt.scatter(x_data, y_data, alpha=0.7)
            plt.plot(x_data, y_pred_opt)
            plt.show()   
        case "2","2":
            k = int(input("Введите интервал наблюдения:\n"))
            a_true = float(input("Введите a:\n"))
            b_true = float(input("Введите b:\n"))
            c_true = float(input("Введите c:\n"))
            h_true = float(input("Введите h:\n"))

            random_norm = stats.norm.rvs(loc=0, scale=1, size=k, random_state=2276)
            xs = list(range(k))
            ys = [a_true + b_true * x + c_true * x**2 + h_true * z for x, z in zip(xs, random_norm)]

            x_data = np.array(xs)
            y_data = np.array(ys)

            def nonlinear_objective(params):
                a, b, c = params
                y_pred = a + b * x_data + c * x_data**2
                return np.sum((y_data - y_pred) ** 2)

            initial_params = [0, 0, 0]
            result_nonlinear = minimize(nonlinear_objective, initial_params, method='BFGS')
            a_opt_nl, b_opt_nl, c_opt_nl = result_nonlinear.x
            y_pred_nonlinear = a_opt_nl + b_opt_nl * x_data + c_opt_nl * x_data**2

            y_pred = a_opt_nl + b_opt_nl * x_data + c_opt_nl * x_data**2
            SS_res = np.sum((y_data - y_pred) ** 2)
            SS_tot = np.sum((y_data - np.mean(y_data)) ** 2)
            r_squared = 1 - (SS_res / SS_tot)
            multiple_r = np.sqrt(r_squared)
            n = len(y_data)
            p = 3  
            adjusted_r_squared = 1 - (1 - r_squared) * (n - 1) / (n - p - 1)
            std_error = np.sqrt(SS_res / (n - p - 1))

            print("СТАТИСТИКА НЕЛИНЕЙНОЙ РЕГРЕССИИ")
            print(f"Множественный R:       {multiple_r:.9f}")
            print(f"R-квадрат:            {r_squared:.9f}")
            print(f"Нормированный R-квадрат: {adjusted_r_squared:.9f}")
            print(f"Стандартная ошибка:    {std_error:.9f}")
            print(f"Наблюдения:           {n}")
            print(f"Параметры модели:     a={a_opt_nl:.4f}, b={b_opt_nl:.4f}, c={c_opt_nl:.4f}")

            plt.figure(figsize=(8, 6))
            plt.scatter(x_data, y_data, alpha=0.6)
            plt.plot(x_data, y_pred_nonlinear, 'r-', linewidth=2)
            plt.show()
        case "3","2":
            k = int(input("Введите интервал наблюдения:\n"))
            a_true = float(input("Введите a0:\n"))
            b_true = float(input("Введите a1:\n"))
            c_true = float(input("Введите a2:\n"))
            d_true = float(input("Введите a11:\n"))
            e_true = float(input("Введите a22:\n"))
            f_true = float(input("Введите a12:\n"))
            h_true = float(input("Введите h:\n"))

            
            np.random.seed(2276)
            x1_data = np.random.uniform(0, 10, k)
            x2_data = np.random.uniform(0, 10, k)
            noise = np.random.normal(0, h_true, k)

            z_data = (a_true + b_true * x1_data + c_true * x2_data + 
                      d_true * x1_data**2 + e_true * x2_data**2 + 
                      f_true * x1_data * x2_data + noise)

            
            def multiple_nonlinear_objective(params):
                a0, a1, a2, a11, a22, a12 = params
                z_pred = (a0 + a1 * x1_data + a2 * x2_data + 
                          a11 * x1_data**2 + a22 * x2_data**2 + 
                          a12 * x1_data * x2_data)
                return np.sum((z_data - z_pred) ** 2)

            
            initial_params = [0, 0, 0, 0, 0, 0]
            result_multiple = minimize(multiple_nonlinear_objective, initial_params, method='BFGS')
            a0_opt, a1_opt, a2_opt, a11_opt, a22_opt, a12_opt = result_multiple.x

           
            z_pred = (a0_opt + a1_opt * x1_data + a2_opt * x2_data + 
                      a11_opt * x1_data**2 + a22_opt * x2_data**2 + 
                      a12_opt * x1_data * x2_data)

            SS_res = np.sum((z_data - z_pred) ** 2)
            SS_tot = np.sum((z_data - np.mean(z_data)) ** 2)
            r_squared = 1 - (SS_res / SS_tot)
            multiple_r = np.sqrt(r_squared)
            n = len(z_data)
            p = 6  
            adjusted_r_squared = 1 - (1 - r_squared) * (n - 1) / (n - p - 1)
            std_error = np.sqrt(SS_res / (n - p - 1))

            print("СТАТИСТИКА МНОЖЕСТВЕННОЙ НЕЛИНЕЙНОЙ РЕГРЕССИИ")
            print(f"Множественный R:       {multiple_r:.9f}")
            print(f"R-квадрат:            {r_squared:.9f}")
            print(f"Нормированный R-квадрат: {adjusted_r_squared:.9f}")
            print(f"Стандартная ошибка:    {std_error:.9f}")
            print(f"Наблюдения:           {n}")
            print("\nПараметры модели:")
            print(f"a0  = {a0_opt:.4f}  (истинное: {a_true})")
            print(f"a1  = {a1_opt:.4f}  (истинное: {b_true})")
            print(f"a2  = {a2_opt:.4f}  (истинное: {c_true})")
            print(f"a11 = {a11_opt:.4f}  (истинное: {d_true})")
            print(f"a22 = {a22_opt:.4f}  (истинное: {e_true})")
            print(f"a12 = {a12_opt:.4f}  (истинное: {f_true})")


            fig = plt.figure(figsize=(12, 5))

            ax1 = fig.add_subplot(121, projection='3d')
            ax1.scatter(x1_data, x2_data, z_data, alpha=0.6)
            ax1.set_xlabel('X1')
            ax1.set_ylabel('X2')
            ax1.set_zlabel('Z')

            ax2 = fig.add_subplot(122, projection='3d')
            x1_grid, x2_grid = np.meshgrid(np.linspace(0, 10, 20), np.linspace(0, 10, 20))
            z_grid = (a0_opt + a1_opt * x1_grid + a2_opt * x2_grid + 
                      a11_opt * x1_grid**2 + a22_opt * x2_grid**2 + 
                      a12_opt * x1_grid * x2_grid)
            ax2.plot_surface(x1_grid, x2_grid, z_grid, alpha=0.7, cmap='viridis')
            ax2.set_xlabel('X1')
            ax2.set_ylabel('X2')
            ax2.set_zlabel('Z')

            plt.tight_layout()
            plt.show()
    


cont = True
while cont == True:
    choose1 = input("Выберите регрессию\n1.Линейная\n2.Нелинейная\n3.Нелинейная множественная\n" )
    choose2 = input("Выберите режим\n1.Тестовый\n2.Рабочий\n") 
    handle_command(choose1, choose2)
    ans = input("Продолжить?[Y|n]\n")
    if ans == 'n':
        cont = False
    