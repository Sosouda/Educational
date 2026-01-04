from openpyxl import load_workbook
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize

def handle_command(command1, command2):
    book = load_workbook(filename= "задание4.xlsx", data_only=True)
    xs = []
    matoj = []
    trend = []
    prognint = []
    progneks = []
    mnka = 0
    mnkb = 0
    L = 0
    _1s = []
    _2s = []
    _3s = []
    nev = []
    disp = []
    sko = []
    nev = []
    match (command1, command2):
        case "1","1":
            Liner = book['1. Точечный прогноз СП']
            a = Liner['G5'].value
            b = Liner['G6'].value
            h = Liner['G7'].value
            print("Количество реализаций =",Liner['B5'].value, "\nИнтервал наблюдения =",Liner['B6'].value,"\n","a =",a,
                  "\n","b =",b,"\n","h =",h,"\n")
            mnka = Liner['M5'].value
            mnkb = Liner['M6'].value
            L =  Liner['M7'].value
            print("МНК оценки параметров модели\n а=",mnka,"\n","b =",mnkb,
                  "\n","Целевая функция апроксимации","\n","L =",L,"\n")
            for i in range(12,137):
                xs.append(Liner['A' + str(i)].value)
                trend.append(Liner['B' + str(i)].value)
                _1s.append(Liner['C' + str(i)].value)
                _2s.append(Liner['D' + str(i)].value)
                _3s.append(Liner['E' + str(i)].value)
                matoj.append(Liner['BC'+str(i)].value)
                disp.append(Liner['BD'+str(i)].value)
                sko.append(Liner['BE'+str(i)].value)
                if i < 74:
                    progneks.append(0)
                    nev.append(0)
                    prognint.append(Liner['BF'+ str(i)].value)
                if i >= 74:
                    progneks.append(Liner['BF'+ str(i)].value)
                    nev.append(Liner['BG'+ str(i)].value)
                    prognint.append(0)

            fig, ax = plt.subplots()
            plt.plot(xs, _1s, label='Наблюдение 1')
            plt.plot(xs, _2s, label='Наблюдение 2')
            plt.plot(xs, _3s, label='Наблюдение 3')

            fig, bx = plt.subplots()
            plt.plot(xs, matoj, label='Мат.ожидание')
            plt.plot(xs, sko, label='СКО')
            plt.plot(xs, disp, label='Дисперсия')
            plt.plot(xs, trend, label='Дет.сост.СП')

            fig, cx = plt.subplots()
            plt.plot(xs, matoj, label='Мат.ожидание')
            plt.plot(xs, prognint, label='Прогноз интер')
            plt.plot(xs, progneks, label='Прогноз экстр')
            plt.plot(xs, nev, label='Ошибка прогноза')
            plt.plot(xs, trend, label='Дет.сост.СП')
            plt.show()
        case "2","1":
            Liner = book['2. Интервальный прогноз СП']
            a = Liner['G5'].value
            b = Liner['G6'].value
            h = Liner['G7'].value
            print("Количество реализаций =",Liner['B5'].value, "\nИнтервал наблюдения =",Liner['B6'].value,"\n","a =",a,
                  "\n","b =",b,"\n","h =",h,"\n")
            mnka = Liner['M5'].value
            mnkb = Liner['M6'].value
            L =  Liner['M7'].value
            print("МНК оценки параметров модели\n а=",mnka,"\n","b =",mnkb,
                  "\n","Целевая функция апроксимации","\n","L =",L,"\n")
            for i in range(12,137):
                xs.append(Liner['A' + str(i)].value)
                trend.append(Liner['B' + str(i)].value)
                _1s.append(Liner['C' + str(i)].value)
                _2s.append(Liner['D' + str(i)].value)
                _3s.append(Liner['E' + str(i)].value)
                matoj.append(Liner['BC'+str(i)].value)
                disp.append(Liner['BD'+str(i)].value)
                sko.append(Liner['BE'+str(i)].value)
                if i < 74:
                    progneks.append(0)
                    nev.append(0)
                    prognint.append(Liner['BF'+ str(i)].value)
                if i >= 74:
                    progneks.append(Liner['BF'+ str(i)].value)
                    nev.append(Liner['BG'+ str(i)].value)
                    prognint.append(0)

            fig, ax = plt.subplots()
            plt.plot(xs, _1s, label='Наблюдение 1')
            plt.plot(xs, _2s, label='Наблюдение 2')
            plt.plot(xs, _3s, label='Наблюдение 3')

            fig, bx = plt.subplots()
            plt.plot(xs, matoj, label='Мат.ожидание')
            plt.plot(xs, sko, label='СКО')
            plt.plot(xs, disp, label='Дисперсия')
            plt.plot(xs, trend, label='Дет.сост.СП')

            fig, cx = plt.subplots()
            plt.plot(xs, matoj, label='Мат.ожидание')
            plt.plot(xs, prognint, label='Прогноз интер')
            plt.plot(xs, progneks, label='Прогноз экстр')
            plt.plot(xs, nev, label='Ошибка прогноза')
            plt.plot(xs, trend, label='Дет.сост.СП')
            

            cells_range = Liner['BK9:CI11']  

            progn = [cell.value for cell in cells_range[0]]  
            prognot = [cell.value for cell in cells_range[1]] 
            progndo = [cell.value for cell in cells_range[2]]
            xss = range(len(progn))
            fig, dx = plt.subplots()
            plt.plot(xss, progn, label='Прогноз')
            plt.plot(xss, prognot, label='Прогноз ОТ')
            plt.plot(xss, progndo, label='Прогноз ДО')
            
            ot1in =[]
            do1in =[]
            ot2in =[]
            do2in =[]
            ot3in =[]
            do3in =[]
            ot1ex =[]
            do1ex =[]
            ot2ex =[]
            do2ex =[]
            ot3ex =[]
            do3ex =[]
            tin = []
            tex = []

            for i in range(13,75):
                ot1in.append(Liner['CM'+ str(i)].value)
                ot2in.append(Liner['CP'+ str(i)].value)
                ot3in.append(Liner['CS'+ str(i)].value)
                do1in.append(Liner['CN'+ str(i)].value)
                do2in.append(Liner['CQ'+ str(i)].value)
                do3in.append(Liner['CT'+ str(i)].value)
                tin.append(Liner['CK'+ str(i)].value)
            for i in range(76, 138):
                ot1ex.append(Liner['CM'+ str(i)].value)
                ot2ex.append(Liner['CP'+ str(i)].value)
                ot3ex.append(Liner['CS'+ str(i)].value)
                do1ex.append(Liner['CN'+ str(i)].value)
                do2ex.append(Liner['CQ'+ str(i)].value)
                do3ex.append(Liner['CT'+ str(i)].value)
                tex.append(Liner['CK'+ str(i)].value)
            
            fig, fx = plt.subplots()
            plt.plot(range(1, len(ot1in)+1), do3in)
            plt.plot(range(1, len(ot1in)+1), do2in)
            plt.plot(range(1, len(ot1in)+1), do1in)
            plt.plot(range(1, len(do1in)+1), ot3in)
            plt.plot(range(1, len(do1in)+1), ot2in)
            plt.plot(range(1, len(do1in)+1), ot1in)
            plt.plot(range(1, len(do1in)+1), tin)
            plt.plot(range(64, 64+len(ot1ex)), tex)
            plt.plot(range(64, 64+len(ot1ex)), do3ex)
            plt.plot(range(64, 64+len(ot1ex)), do2ex)
            plt.plot(range(64, 64+len(ot1ex)), do1ex)
            plt.plot(range(64, 64+len(do1ex)), ot3ex)
            plt.plot(range(64, 64+len(do1ex)), ot2ex)
            plt.plot(range(64, 64+len(do1ex)), ot1ex)
            plt.show()
        case "1","2":
            n = int(input("Введите количество испытаний (n): "))
            k = int(input("Введите количество наблюдений (k): "))

            a_true = float(input("Введите a: "))
            b_true = float(input("Введите b: "))
            h_true = float(input("Введите h: "))

            np.random.seed(2276)

            x = np.arange(1, k + 1)
            y_trend = a_true + b_true * x

            
            Z_norm = stats.norm.rvs(loc=0, scale=1, size=(k, n))
            plt.figure()
            for i in range(min(3, n)):
                plt.plot(x, Z_norm[:, i])
            plt.xlabel("x")
            plt.ylabel("Z_norm")
            plt.grid(True)
            plt.show()

            Z = np.random.uniform(-1, 1, size=(k, n))
            X = np.tile(x.reshape(-1, 1), (1, n))
            Y = a_true + b_true * X + h_true * Z

            mean_Y = np.mean(Y, axis=1)    
            var_Y = np.var(Y, axis=1, ddof=1)
            std_Y = np.sqrt(var_Y)

           
            y_pred_true = a_true + b_true * x
            residuals = mean_Y - y_pred_true
            residuals_sq = residuals ** 2


            if k % 2 == 0:
                first_half = np.arange(0, k // 2)
            else:
                first_half = np.arange(0, k // 2)  

            x_fit = x[first_half]
            y_fit = mean_Y[first_half]

            
            A = np.vstack([np.ones_like(x_fit), x_fit]).T
            a_hat, b_hat = np.linalg.lstsq(A, y_fit, rcond=None)[0]
           
            y_pred_interpol = a_hat + b_hat * x_fit
            x_second = x[k // 2:]  
            y_pred_extrap = a_hat + b_hat * x_second

            
            residuals_second = mean_Y[k // 2:] - y_pred_extrap


            print(f"МНК: a = {a_hat:.4f}, b = {b_hat:.4f}")

            plt.figure()
            plt.plot(x, mean_Y)
            plt.plot(x, var_Y)
            plt.plot(x, std_Y)
            plt.plot(x, y_trend)
            plt.show()

            plt.figure()
            plt.plot(x, mean_Y)
            plt.plot(x, y_trend)
            plt.plot(x_fit, y_pred_interpol)
            plt.plot(x_second, y_pred_extrap)
            plt.plot(x_second, residuals_second)
            plt.show()
        case "2","2":
            n = int(input("Введите количество испытаний (n): "))
            k = int(input("Введите количество наблюдений (k): "))
            a_true = float(input("Введите a: "))
            b_true = float(input("Введите b: "))
            h_true = float(input("Введите h: "))

            np.random.seed(2276)

            x = np.arange(1, k + 1)
            y_trend = a_true + b_true * x
            X = np.tile(x.reshape(-1, 1), (1, n))
            Z = np.random.uniform(-1, 1, size=(k, n))
            Y = a_true + b_true * X + h_true * Z

            if k % 2 == 0:
                first_half_idx = np.arange(0, k // 2)
                second_half_idx = np.arange(k // 2, k)
            else:
                first_half_idx = np.arange(0, k // 2)
                second_half_idx = np.arange(k // 2 + 1, k)
            x_first, x_second = x[first_half_idx], x[second_half_idx]

            a_list, b_list = np.zeros(n), np.zeros(n)
            for j in range(n):
                y_half = Y[first_half_idx, j]
                A = np.vstack([np.ones_like(x_first), x_first]).T
                a_j, b_j = np.linalg.lstsq(A, y_half, rcond=None)[0]
                a_list[j], b_list[j] = a_j, b_j

            L = np.sum((Y - (a_list.reshape(1, n) + b_list.reshape(1, n) * X)) ** 2, axis=0)

            mean_a, mean_b = np.mean(a_list), np.mean(b_list)
            std_a, std_b = np.std(a_list, ddof=1), np.std(b_list, ddof=1)
            corr_ab = np.corrcoef(a_list, b_list)[0, 1]
            print(f"\nmean(a)={mean_a:.4f}, mean(b)={mean_b:.4f}, std(a)={std_a:.4f}, std(b)={std_b:.4f}, corr={corr_ab:.4f}")

            x_last = x[-1]
            cum_forecast, cum_lower_3, cum_upper_3 = [], [], []
            for m in range(1, n + 1):
                a_m, b_m = a_list[:m], b_list[:m]
                mean_a_m, mean_b_m = np.mean(a_m), np.mean(b_m)
                std_a_m, std_b_m = np.std(a_m, ddof=1), np.std(b_m, ddof=1)
                corr_m = np.corrcoef(a_m, b_m)[0, 1] if m > 1 else 0
                forecast = mean_a_m + mean_b_m * x_last
                var_y = std_a_m**2 + 2 * corr_m * std_a_m * std_b_m * x_last + std_b_m**2 * x_last**2
                sigma_y = np.sqrt(max(var_y, 0))
                cum_forecast.append(forecast)
                cum_lower_3.append(forecast - 3 * sigma_y)
                cum_upper_3.append(forecast + 3 * sigma_y)


            plt.figure(figsize=(8, 5))
            plt.plot(range(1, n + 1), cum_forecast)
            plt.plot(range(1, n + 1), cum_lower_3)
            plt.plot(range(1, n + 1), cum_upper_3)
            plt.show()


            var_a, var_b = std_a**2, std_b**2
            cov_ab = corr_ab * std_a * std_b
            y_pred = mean_a + mean_b * x
            sigma_y_x = np.sqrt(np.maximum(0, var_a + 2 * cov_ab * x + var_b * x**2))

            low1, up1 = y_pred - sigma_y_x, y_pred + sigma_y_x
            low2, up2 = y_pred - 2*sigma_y_x, y_pred + 2*sigma_y_x
            low3, up3 = y_pred - 3*sigma_y_x, y_pred + 3*sigma_y_x


            plt.figure(figsize=(10, 6))
            plt.plot(x_first, y_pred[first_half_idx])
            plt.plot(x_second, y_pred[second_half_idx])

  
            plt.plot(x_first, low1[first_half_idx])
            plt.plot(x_first, up1[first_half_idx])
            plt.plot(x_second, low1[second_half_idx])
            plt.plot(x_second, up1[second_half_idx])


            plt.plot(x_first, low2[first_half_idx])
            plt.plot(x_first, up2[first_half_idx])
            plt.plot(x_second, low2[second_half_idx])
            plt.plot(x_second, up2[second_half_idx])


            plt.plot(x_first, low3[first_half_idx])
            plt.plot(x_first, up3[first_half_idx])
            plt.plot(x_second, low3[second_half_idx])
            plt.plot(x_second, up3[second_half_idx])
            plt.show()
        


cont = True
while cont == True:
    choose1 = input("Выберите вид прогноза СП\n1.Точечный\n2.Интервалньый\n" )
    choose2 = input("Выберите режим\n1.Тестовый\n2.Рабочий\n") 
    handle_command(choose1, choose2)
    ans = input("Продолжить?[Y|n]\n")
    if ans == 'n':
        cont = False
    