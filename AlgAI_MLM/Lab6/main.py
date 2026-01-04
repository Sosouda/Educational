from openpyxl import load_workbook
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution

def handle_command(command1, command2):
    book = load_workbook(filename= "задание6.xlsx", data_only=True)
    ishdan=[]
    k=[]
    df1 = []
    fopt = []
    x1 = []
    x2 = []
    x1o = []
    x2o = []
    n = []
    f1u = []
    f1d = []
    f2u = []
    f2d = []
    f3u = []
    f3d = []
    match (command1, command2):
        case "1","1":
            Liner = book['f1 c пост.шг']
            for i in range(4,11):
                ishdan.append(Liner['B' + str(i)].value)
            print(f"c1={ishdan[0]},c2={ishdan[1]},a1={ishdan[2]},a2={ishdan[3]},x10={ishdan[4]}"\
                  f",x20={ishdan[5]},r={ishdan[6]}")
            for i in range(4,105):
                k.append(Liner['K' + str(i)].value)
                df1.append(Liner['R' + str(i)].value)
                fopt.append(Liner['AG' + str(i)].value)
            fig, ax = plt.subplots()
            plt.scatter(k, df1)
            plt.scatter(k, fopt)
            plt.show()
            for i in range(4,105):
                x1.append(Liner['L' + str(i)].value)
                x2.append(Liner['M' + str(i)].value)
                x1o.append(Liner['AH' + str(i)].value)
                x2o.append(Liner['AI' + str(i)].value)
            fig, ax = plt.subplots()
            plt.scatter(k, x1)
            plt.scatter(k, x2)
            plt.scatter(k, x1o)
            plt.scatter(k, x2o)
            plt.show()
            for i in range(8,21):
                n.append(Liner['W' + str(i)].value)
                f1u.append(Liner['X' + str(i)].value)
                f1d.append(Liner['Y' + str(i)].value)
                if i < 10 or i > 18:
                    f2u.append(Liner['Z10'].value - 0.00001)
                    f2d.append(Liner['AA10'].value - 0.00001)
                else:
                    f2u.append(Liner['Z' + str(i)].value)
                    f2d.append(Liner['AA' + str(i)].value)
                if i < 12 or i > 16:
                    f3u.append(Liner['AB12'].value - 0.00001)
                    f3d.append(Liner['AC12'].value - 0.00001)
                else:
                    f3u.append(Liner['AB' + str(i)].value)
                    f3d.append(Liner['AC' + str(i)].value)
            fig, ax = plt.subplots()
            plt.scatter(n, f1u)  
            plt.scatter(n, f2u)
            plt.scatter(n, f3u)
            plt.scatter(n, f1d)
            plt.scatter(n, f2d)
            plt.scatter(n, f3d)
            plt.show()
        case "2","1":
            Liner = book['f1 числ.пр.']
            for i in range(4,12):
                ishdan.append(Liner['B' + str(i)].value)
            print(f"c1={ishdan[0]},c2={ishdan[1]},a1={ishdan[2]},a2={ishdan[3]},x10={ishdan[4]}"\
                  f",x20={ishdan[5]},r={ishdan[6]},dx={ishdan[7]}")
            for i in range(4,105):
                k.append(Liner['K' + str(i)].value)
                df1.append(Liner['R' + str(i)].value)
                fopt.append(Liner['AG' + str(i)].value)
            fig, ax = plt.subplots()
            plt.scatter(k, df1)
            plt.scatter(k, fopt)
            plt.show()
            for i in range(4,105):
                x1.append(Liner['L' + str(i)].value)
                x2.append(Liner['M' + str(i)].value)
                x1o.append(Liner['AH' + str(i)].value)
                x2o.append(Liner['AI' + str(i)].value)
            fig, ax = plt.subplots()
            plt.scatter(k, x1)
            plt.scatter(k, x2)
            plt.scatter(k, x1o)
            plt.scatter(k, x2o)
            plt.show()
            for i in range(8,21):
                n.append(Liner['W' + str(i)].value)
                f1u.append(Liner['X' + str(i)].value)
                f1d.append(Liner['Y' + str(i)].value)
                if i < 10 or i > 18:
                    f2u.append(Liner['Z10'].value - 0.00001)
                    f2d.append(Liner['AA10'].value - 0.00001)
                else:
                    f2u.append(Liner['Z' + str(i)].value)
                    f2d.append(Liner['AA' + str(i)].value)
                if i < 12 or i > 16:
                    f3u.append(Liner['AB12'].value - 0.00001)
                    f3d.append(Liner['AC12'].value - 0.00001)
                else:
                    f3u.append(Liner['AB' + str(i)].value)
                    f3d.append(Liner['AC' + str(i)].value)
            fig, ax = plt.subplots()
            plt.scatter(n, f1u)  
            plt.scatter(n, f2u)
            plt.scatter(n, f3u)
            plt.scatter(n, f1d)
            plt.scatter(n, f2d)
            plt.scatter(n, f3d)
            plt.show()
        case "3","1":
            Liner = book['f2 числ.пр.']
            for i in range(4,12):
                ishdan.append(Liner['B' + str(i)].value)
            for i in range(4,8):
                ishdan.append(Liner['D' + str(i)].value)
            print(ishdan)
            print(f"c1={ishdan[0]},c2={ishdan[1]},a1={ishdan[2]},a2={ishdan[3]},x10={ishdan[4]}"
                  f",x20={ishdan[5]},r={ishdan[6]},dx={ishdan[7]},c0={ishdan[8]},c3={ishdan[9]}"
                  f",c4={ishdan[10]},c5={ishdan[11]}")
            for i in range(4,105):
                k.append(Liner['K' + str(i)].value)
                df1.append(Liner['R' + str(i)].value)
                fopt.append(Liner['AG' + str(i)].value)
            fig, ax = plt.subplots()
            plt.scatter(k, df1)
            plt.scatter(k, fopt)
            plt.show()
            for i in range(4,105):
                x1.append(Liner['L' + str(i)].value)
                x2.append(Liner['M' + str(i)].value)
                x1o.append(Liner['AH' + str(i)].value)
                x2o.append(Liner['AI' + str(i)].value)
            fig, ax = plt.subplots()
            plt.scatter(k, x1)
            plt.scatter(k, x2)
            plt.scatter(k, x1o)
            plt.scatter(k, x2o)
            plt.show()
            for i in range(9,17):
                n.append(Liner['W' + str(i)].value)
                f1u.append(Liner['X' + str(i)].value)
                f1d.append(Liner['Y' + str(i)].value)
                if i < 10 or i > 16:
                    f2u.append(Liner['Z10'].value - 0.00001)
                    f2d.append(Liner['AA10'].value - 0.00001)
                else:
                    f2u.append(Liner['Z' + str(i)].value)
                    f2d.append(Liner['AA' + str(i)].value)
                if i < 11 or i > 15:
                    f3u.append(Liner['AB12'].value - 0.00001)
                    f3d.append(Liner['AC12'].value - 0.00001)
                else:
                    f3u.append(Liner['AB' + str(i)].value)
                    f3d.append(Liner['AC' + str(i)].value)
            fig, ax = plt.subplots()
            plt.plot(n, f1u)  
            plt.plot(n, f2u)
            plt.plot(n, f3u)
            plt.plot(n, f1d)
            plt.plot(n, f2d)
            plt.plot(n, f3d)
            plt.show()
        case "4","1":
            Liner = book['f1 с дробл.шг']
            for i in range(4,13):
                ishdan.append(Liner['B' + str(i)].value)
            print(f"c1={ishdan[0]},c2={ishdan[1]},a1={ishdan[2]},a2={ishdan[3]},x10={ishdan[4]}"\
                  f",x20={ishdan[5]},r={ishdan[6]},f_por={ishdan[7]},k_dropbl={ishdan[8]}")
            for i in range(4,105):
                k.append(Liner['K' + str(i)].value)
                df1.append(Liner['R' + str(i)].value)
                fopt.append(Liner['AG' + str(i)].value)
            fig, ax = plt.subplots()
            plt.scatter(k, df1)
            plt.scatter(k, fopt)
            plt.show()
            for i in range(4,105):
                x1.append(Liner['L' + str(i)].value)
                x2.append(Liner['M' + str(i)].value)
                x1o.append(Liner['AH' + str(i)].value)
                x2o.append(Liner['AI' + str(i)].value)
            fig, ax = plt.subplots()
            plt.scatter(k, x1)
            plt.scatter(k, x2)
            plt.scatter(k, x1o)
            plt.scatter(k, x2o)
            plt.show()
            for i in range(8,21):
                n.append(Liner['W' + str(i)].value)
                f1u.append(Liner['X' + str(i)].value)
                f1d.append(Liner['Y' + str(i)].value)
                if i < 10 or i > 18:
                    f2u.append(Liner['Z10'].value - 0.00001)
                    f2d.append(Liner['AA10'].value - 0.00001)
                else:
                    f2u.append(Liner['Z' + str(i)].value)
                    f2d.append(Liner['AA' + str(i)].value)
                if i < 12 or i > 16:
                    f3u.append(Liner['AB12'].value - 0.00001)
                    f3d.append(Liner['AC12'].value - 0.00001)
                else:
                    f3u.append(Liner['AB' + str(i)].value)
                    f3d.append(Liner['AC' + str(i)].value)
            fig, ax = plt.subplots()
            plt.scatter(n, f1u)  
            plt.scatter(n, f2u)
            plt.scatter(n, f3u)
            plt.scatter(n, f1d)
            plt.scatter(n, f2d)
            plt.scatter(n, f3d)
            plt.show()
        case "5","1":
            Liner = book['f1 наиск.спск']
            for i in range(4,13):
                ishdan.append(Liner['B' + str(i)].value)
            print(f"c1={ishdan[0]},c2={ishdan[1]},a1={ishdan[2]},a2={ishdan[3]},x10={ishdan[4]}"\
                  f",x20={ishdan[5]},r={ishdan[6]},f_por={ishdan[7]},k_dropbl={ishdan[8]}")
            for i in range(4,105):
                k.append(Liner['K' + str(i)].value)
                df1.append(Liner['V' + str(i)].value)
                fopt.append(Liner['AK' + str(i)].value)
            fig, ax = plt.subplots()
            plt.scatter(k, df1)
            plt.scatter(k, fopt)
            plt.show()
            for i in range(4,105):
                x1.append(Liner['L' + str(i)].value)
                x2.append(Liner['M' + str(i)].value)
                x1o.append(Liner['AL' + str(i)].value)
                x2o.append(Liner['AM' + str(i)].value)
            fig, ax = plt.subplots()
            plt.plot(k, x1)
            plt.plot(k, x2)
            plt.scatter(k, x1o)
            plt.scatter(k, x2o)
            plt.show()
            for i in range(8,21):
                n.append(Liner['AA' + str(i)].value)
                f1u.append(Liner['AB' + str(i)].value)
                f1d.append(Liner['AC' + str(i)].value)
                if i < 10 or i > 18:
                    f2u.append(Liner['AD10'].value - 0.00001)
                    f2d.append(Liner['AE10'].value - 0.00001)
                else:
                    f2u.append(Liner['AD' + str(i)].value)
                    f2d.append(Liner['AE' + str(i)].value)
                if i < 12 or i > 16:
                    f3u.append(Liner['AF12'].value - 0.00001)
                    f3d.append(Liner['AG12'].value - 0.00001)
                else:
                    f3u.append(Liner['AF' + str(i)].value)
                    f3d.append(Liner['AG' + str(i)].value)
            fig, ax = plt.subplots()
            plt.scatter(n, f1u)  
            plt.scatter(n, f2u)
            plt.scatter(n, f3u)
            plt.scatter(n, f1d)
            plt.scatter(n, f2d)
            plt.scatter(n, f3d)
            plt.show()
        case "1","2":
            def input_float(prompt, default=None):
                s = input(f"{prompt}" + (f" (по умолчанию {default})" if default is not None else "") + ": ")
                if s.strip() == "" and default is not None:
                    return default
                try:
                    return float(s)
                except:
                    print("Введено не число, попробуйте ещё раз.")
                    return input_float(prompt, default)
            print("Введите параметры (если нажмёте Enter — берутся значения по умолчанию):")
            c1 = input_float("c1", 1.0)
            c2 = input_float("c2", 1.0)
            a1 = input_float("a1", 10.0)
            a2 = input_float("a2", 10.0)
            x1_init = input_float("x1", 0.0)
            x2_init = input_float("x2", 0.0)
            r = input_float("r", 0.1)
            steps = 100
            def stage_one(c1, c2, a1, a2, x1_init, x2_init, r, steps=100):
                x1 = x1_init
                x2 = x2_init
                x1_list, x2_list, f1_list = [], [], []

                for k in range(steps):
                    f1 = c1 * (x1 - a1)**2 + c2 * (x2 - a2)**2
                    x1_list.append(x1)
                    x2_list.append(x2)
                    f1_list.append(f1)
                    x1 = x1 - r * (2 * c1 * (x1 - a1))
                    x2 = x2 - r * (2 * c2 * (x2 - a2))

                x1_list = np.array(x1_list)
                x2_list = np.array(x2_list)
                f1_list = np.array(f1_list)

                # эволюционный поиск минимума
                bounds = [(0, 100), (0, 100)]
                def f_obj(x):
                    return c1 * (x[0] - a1)**2 + c2 * (x[1] - a2)**2

                result = differential_evolution(f_obj, bounds, polish=True)
                x_opt = result.x
                x_opt_updated = np.array([
                    x_opt[0] - r * (2 * c1 * (x_opt[0] - a1)),
                    x_opt[1] - r * (2 * c2 * (x_opt[1] - a2))
                ])
                f1_opt = c1 * (x_opt_updated[0] - a1)**2 + c2 * (x_opt_updated[1] - a2)**2

                return {
                    "x1_list": x1_list,
                    "x2_list": x2_list,
                    "f1_list": f1_list,
                    "x_opt": x_opt,
                    "x_opt_updated": x_opt_updated,
                    "f1_opt": f1_opt
                }
            def plot_stage_one(data, steps=100):
                k = np.arange(1, steps+1)

                # График 1 — f1 и f1_opt
                plt.figure(figsize=(8,5))
                plt.plot(k, data['f1_list'], label='f1 (итерации)')
                plt.plot(k, [data['f1_opt']]*len(k), linestyle='--', label='f1_opt (константа)')
                plt.xlabel('k (шаг)')
                plt.ylabel('f1')
                plt.title('f1 по шагам и f1_opt')
                plt.legend()
                plt.grid(True)
                plt.tight_layout()
                plt.show()

                # График 2 — x1, x2 и их оптимальные линии
                plt.figure(figsize=(8,5))
                plt.plot(k, data['x1_list'], label='x1 (итерации)')
                plt.plot(k, data['x2_list'], label='x2 (итерации)')
                plt.plot(k, [data['x_opt_updated'][0]]*len(k), linestyle='--', label='x1_opt')
                plt.plot(k, [data['x_opt_updated'][1]]*len(k), linestyle='--', label='x2_opt')
                plt.xlabel('k (шаг)')
                plt.ylabel('Значения x')
                plt.title('x1, x2 и их оптимумы')
                plt.legend()
                plt.grid(True)
                plt.tight_layout()
                plt.show()
            data = stage_one(c1, c2, a1, a2, x1_init, x2_init, r, steps)
            print("\nРезультаты этапа 1:")
            print(f"Оптимальные (найденные) x (до обновления): {data['x_opt']}")
            print(f"Оптимальные x после обновления: {data['x_opt_updated']}")
            print(f"f1_opt = {data['f1_opt']:.6g}")
            plot_stage_one(data, steps)
            def stage_two_table_and_plots(c1, a1, a2, x1_min=-1, x1_max=20, f_list=[350,200,50]):
                x1_values = np.arange(x1_min, x1_max+1, 1)
                results = {}
                for F in f_list:
                    plus_vals = []
                    minus_vals = []
                    for x1 in x1_values:
                        denom = a1 if abs(a1) > 1e-12 else 1e-12
                        inside = (F - c1 * (x1 - a1)**2) / denom
                        if inside < 0:
                            plus_vals.append(np.nan)
                            minus_vals.append(np.nan)
                        else:
                            root = np.sqrt(inside)
                            plus_vals.append(a2 + root)
                            minus_vals.append(a2 - root)
                    results[F] = {"plus": np.array(plus_vals), "minus": np.array(minus_vals)}
                header = ["x1"] + [f"F={F} +" for F in f_list] + [f"F={F} -" for F in f_list]
                print("\nТаблица для этапа 2:")
                print("\t".join(header))
                for i, x1 in enumerate(x1_values):
                    row = [str(x1)]
                    for F in f_list:
                        v = results[F]["plus"][i]
                        row.append(f"{v:.6g}" if not np.isnan(v) else "#Число")
                    for F in f_list:
                        v = results[F]["minus"][i]
                        row.append(f"{v:.6g}" if not np.isnan(v) else "#Число")
                    print("\t".join(row))

                # Графики
                plt.figure(figsize=(9,6))
                for F in f_list:
                    plus = results[F]["plus"]
                    minus = results[F]["minus"]
                    mask_p = ~np.isnan(plus)
                    mask_m = ~np.isnan(minus)
                    if mask_p.any():
                        plt.plot(x1_values[mask_p], plus[mask_p], label=f"F={F} (+)")
                    if mask_m.any():
                        plt.plot(x1_values[mask_m], minus[mask_m], label=f"F={F} (-)")

                extra_F = f_list[0]
                extra_series = results[extra_F]["plus"]
                mask_e = ~np.isnan(extra_series)
                if mask_e.any():
                    plt.plot(data['x1_list'], data['x2_list'], linestyle=':', linewidth=2.5, color='black', label='x1 vs x2 (этап 1)')

                plt.xlabel('x1')
                plt.ylabel('x2 (вычислено)')
                plt.title('Этап 2: линии для разных F')
                
                plt.grid(True)
                plt.tight_layout()
                plt.show()

                return results
            results = stage_two_table_and_plots(c1, a1, a2)
        case "2","2":
            def input_float(prompt, default=None):
                s = input(f"{prompt}" + (f" (по умолчанию {default})" if default is not None else "") + ": ")
                if s.strip() == "" and default is not None:
                    return default
                try:
                    return float(s)
                except:
                    print("Введено не число, попробуйте ещё раз.")
                    return input_float(prompt, default)
            print("Введите параметры (если нажмёте Enter — берутся значения по умолчанию):")
            c1 = input_float("c1", 1.0)
            c2 = input_float("c2", 1.0)
            a1 = input_float("a1", 10.0)
            a2 = input_float("a2", 10.0)
            x1_init = input_float("x1)", 0.0)
            x2_init = input_float("x2", 0.0)
            r = input_float("r", 0.1)
            d = input_float("d", 0.1)
            steps = 100
            def stage_one(c1, c2, a1, a2, x1_init, x2_init, r,d, steps=100):
                x1 = x1_init
                x2 = x2_init
                x1_list, x2_list, f1_list = [], [], []

                for k in range(steps):
                    f1 = c1 * (x1 - a1)**2 + c2 * (x2 - a2)**2
                    x1_list.append(x1)
                    x2_list.append(x2)
                    f1_list.append(f1)
                    x1 = x1 - r * (((c1*(x1+d-a1)**2+c2*(x2-a2)**2)-(c1*(x1-a1)**2+c2*(x2-a2)**2))/d)
                    x2 = x2 - r * (((c1*(x1-a1)**2+c2*(x2+d-a2)**2)-(c1*(x1-a1)**2+c2*(x2-a2)**2))/d)

                x1_list = np.array(x1_list)
                x2_list = np.array(x2_list)
                f1_list = np.array(f1_list)

                # эволюционный поиск минимума
                bounds = [(0, 100), (0, 100)]
                def f_obj(x):
                    return c1 * (x[0] - a1)**2 + c2 * (x[1] - a2)**2

                result = differential_evolution(f_obj, bounds, polish=True)
                x_opt = result.x
                x_opt_updated = np.array([
                    x_opt[0] - r * (2 * c1 * (x_opt[0] - a1)),
                    x_opt[1] - r * (2 * c2 * (x_opt[1] - a2))
                ])
                f1_opt = c1 * (x_opt_updated[0] - a1)**2 + c2 * (x_opt_updated[1] - a2)**2

                return {
                    "x1_list": x1_list,
                    "x2_list": x2_list,
                    "f1_list": f1_list,
                    "x_opt": x_opt,
                    "x_opt_updated": x_opt_updated,
                    "f1_opt": f1_opt
                }
            def plot_stage_one(data, steps=100):
                k = np.arange(1, steps+1)

                # График 1 — f1 и f1_opt
                plt.figure(figsize=(8,5))
                plt.plot(k, data['f1_list'], label='f1 (итерации)')
                plt.plot(k, [data['f1_opt']]*len(k), linestyle='--', label='f1_opt (константа)')
                plt.xlabel('k (шаг)')
                plt.ylabel('f1')
                plt.title('f1 по шагам и f1_opt')
                plt.legend()
                plt.grid(True)
                plt.tight_layout()
                plt.show()

                # График 2 — x1, x2 и их оптимальные линии
                plt.figure(figsize=(8,5))
                plt.plot(k, data['x1_list'], label='x1 (итерации)')
                plt.plot(k, data['x2_list'], label='x2 (итерации)')
                plt.plot(k, [data['x_opt_updated'][0]]*len(k), linestyle='--', label='x1_opt')
                plt.plot(k, [data['x_opt_updated'][1]]*len(k), linestyle='--', label='x2_opt')
                plt.xlabel('k (шаг)')
                plt.ylabel('Значения x')
                plt.title('x1, x2 и их оптимумы')
                plt.legend()
                plt.grid(True)
                plt.tight_layout()
                plt.show()
            data = stage_one(c1, c2, a1, a2, x1_init, x2_init, r,d, steps)
            print("\nРезультаты этапа 1:")
            print(f"Оптимальные (найденные) x (до обновления): {data['x_opt']}")
            print(f"Оптимальные x после обновления: {data['x_opt_updated']}")
            print(f"f1_opt = {data['f1_opt']:.6g}")
            plot_stage_one(data, steps)
            def stage_two_table_and_plots(c1, a1, a2, x1_min=-1, x1_max=20, f_list=[350,200,50]):
                x1_values = np.arange(x1_min, x1_max+1, 1)
                results = {}
                for F in f_list:
                    plus_vals = []
                    minus_vals = []
                    for x1 in x1_values:
                        denom = a1 if abs(a1) > 1e-12 else 1e-12
                        inside = (F - c1 * (x1 - a1)**2) / denom
                        if inside < 0:
                            plus_vals.append(np.nan)
                            minus_vals.append(np.nan)
                        else:
                            root = np.sqrt(inside)
                            plus_vals.append(a2 + root)
                            minus_vals.append(a2 - root)
                    results[F] = {"plus": np.array(plus_vals), "minus": np.array(minus_vals)}
                header = ["x1"] + [f"F={F} +" for F in f_list] + [f"F={F} -" for F in f_list]
                print("\nТаблица для этапа 2:")
                print("\t".join(header))
                for i, x1 in enumerate(x1_values):
                    row = [str(x1)]
                    for F in f_list:
                        v = results[F]["plus"][i]
                        row.append(f"{v:.6g}" if not np.isnan(v) else "#Число")
                    for F in f_list:
                        v = results[F]["minus"][i]
                        row.append(f"{v:.6g}" if not np.isnan(v) else "#Число")
                    print("\t".join(row))

                # Графики
                plt.figure(figsize=(9,6))
                for F in f_list:
                    plus = results[F]["plus"]
                    minus = results[F]["minus"]
                    mask_p = ~np.isnan(plus)
                    mask_m = ~np.isnan(minus)
                    if mask_p.any():
                        plt.plot(x1_values[mask_p], plus[mask_p], label=f"F={F} (+)")
                    if mask_m.any():
                        plt.plot(x1_values[mask_m], minus[mask_m], label=f"F={F} (-)")

                extra_F = f_list[0]
                extra_series = results[extra_F]["plus"]
                mask_e = ~np.isnan(extra_series)
                if mask_e.any():
                    plt.plot(data['x1_list'], data['x2_list'], linestyle=':', linewidth=2.5, color='black', label='x1 vs x2 (этап 1)')

                plt.xlabel('x1')
                plt.ylabel('x2 (вычислено)')
                plt.title('Этап 2: линии для разных F')
                
                plt.grid(True)
                plt.tight_layout()
                plt.show()

                return results
            results = stage_two_table_and_plots(c1, a1, a2)
        case "3","2":
            # numeric variant for f2: f2(x1,x2) = c0 + c1*y1 + c2*y2 + c3*y1^2 + c4*y1*y2 + c5*y2^2
            def input_float(prompt, default=None):
                try:
                    s = input(f"{prompt} [{default}]: ")
                    return float(s) if s.strip() != "" else float(default)
                except Exception:
                    return float(default)

            print("Введите параметры (если нажмёте Enter — берутся значения по умолчанию):")
            c0 = input_float("c0", 0.0)
            c1 = input_float("c1", 1.0)
            c2 = input_float("c2", 1.0)
            c3 = input_float("c3", 0.0)
            c4 = input_float("c4", 0.0)
            c5 = input_float("c5", 1.0)
            a1 = input_float("a1", 10.0)
            a2 = input_float("a2", 10.0)
            x1_init = input_float("x1", 0.0)
            x2_init = input_float("x2", 0.0)
            r = input_float("r", 0.1)
            steps = 100

            def f2_xy_point(x1p, x2p):
                y1 = x1p - a1
                y2 = x2p - a2
                return c0 + c1 * y1 + c2 * y2 + c3 * (y1 ** 2) + c4 * y1 * y2 + c5 * (y2 ** 2)

            def f2_xy_vec(x):
                return f2_xy_point(x[0], x[1])

            def grad_f2_at(x1p, x2p):
                y1 = x1p - a1
                y2 = x2p - a2
                # partials dF/dx1 = c1 + 2*c3*y1 + c4*y2
                #          dF/dx2 = c2 + c4*y1 + 2*c5*y2
                return np.array([c1 + 2 * c3 * y1 + c4 * y2,
                                 c2 + c4 * y1 + 2 * c5 * y2])

            def stage_one(c0, c1, c2, c3, c4, c5, a1, a2, x1_init, x2_init, r, steps=100):
                x1 = x1_init
                x2 = x2_init
                x1_list, x2_list, f2_list = [], [], []

                for k in range(steps):
                    f2 = f2_xy_point(x1, x2)
                    x1_list.append(x1)
                    x2_list.append(x2)
                    f2_list.append(f2)
                    g = grad_f2_at(x1, x2)
                    x1 = x1 - r * g[0]
                    x2 = x2 - r * g[1]

                x1_list = np.array(x1_list)
                x2_list = np.array(x2_list)
                f2_list = np.array(f2_list)

                # эволюционный поиск минимума (глобальный)
                bounds = [(0, 100), (0, 100)]
                result = differential_evolution(f2_xy_vec, bounds, polish=True)
                x_opt = result.x
                # обновление аналогично градиентному шагу
                g_opt = grad_f2_at(x_opt[0], x_opt[1])
                x_opt_updated = np.array([x_opt[0] - r * g_opt[0], x_opt[1] - r * g_opt[1]])
                f2_opt = f2_xy_point(x_opt_updated[0], x_opt_updated[1])

                return {
                    "x1_list": x1_list,
                    "x2_list": x2_list,
                    "f2_list": f2_list,
                    "x_opt": x_opt,
                    "x_opt_updated": x_opt_updated,
                    "f2_opt": f2_opt
                }

            def plot_stage_one(data, steps=100):
                k = np.arange(1, len(data['f2_list']) + 1)

                # График 1 — f2 по итерациям и f2_opt
                plt.figure(figsize=(8,5))
                plt.plot(k, data['f2_list'], label='f2 (итерации)')
                plt.plot(k, [data['f2_opt']]*len(k), linestyle='--', label='f2_opt (константа)')
                plt.xlabel('k (шаг)')
                plt.ylabel('f2')
                plt.title('f2 по шагам и f2_opt')
                plt.legend()
                plt.grid(True)
                plt.tight_layout()
                plt.show()

                # График 2 — x1, x2 и их оптимальные линии
                plt.figure(figsize=(8,5))
                plt.plot(k, data['x1_list'], label='x1 (итерации)')
                plt.plot(k, data['x2_list'], label='x2 (итерации)')
                plt.plot(k, [data['x_opt_updated'][0]]*len(k), linestyle='--', label='x1_opt')
                plt.plot(k, [data['x_opt_updated'][1]]*len(k), linestyle='--', label='x2_opt')
                plt.xlabel('k (шаг)')
                plt.ylabel('Значения x')
                plt.title('x1, x2 и их оптимумы')
                plt.legend()
                plt.grid(True)
                plt.tight_layout()
                plt.show()

            data = stage_one(c0, c1, c2, c3, c4, c5, a1, a2, x1_init, x2_init, r, steps)
            print("\nРезультаты этапа 1:")
            print(f"Оптимальные (найденные) x (до обновления): {data['x_opt']}")
            print(f"Оптимальные x после обновления: {data['x_opt_updated']}")
            print(f"f2_opt = {data['f2_opt']:.6g}")
            plot_stage_one(data, steps)

            def stage_two_table_and_plots(c0, c1, c2, c3, c4, c5, a1, a2,
                                          x1_min=-1, x1_max=20, f_list=[350,200,50], points=400, data_stage1=None):
                x1_vals = np.linspace(x1_min, x1_max, points)
                curves = {}
                for f_level in f_list:
                    sols_pos = []
                    sols_neg = []
                    for x1v in x1_vals:
                        y1 = x1v - a1
                        A = c5
                        B = c2 + c4 * y1
                        C = c0 + c1 * y1 + c3 * (y1 ** 2) - f_level
                        disc = B * B - 4 * A * C
                        if abs(A) < 1e-14:
                            # linear in y2: B*y2 + C = 0 -> y2 = -C/B if B !=0
                            if abs(B) > 1e-12:
                                y2 = -C / B
                                x2v = a2 + y2
                                sols_pos.append((x1v, x2v))
                        else:
                            if disc >= 0:
                                sqrt_d = np.sqrt(disc)
                                y2_1 = (-B + sqrt_d) / (2 * A)
                                y2_2 = (-B - sqrt_d) / (2 * A)
                                sols_pos.append((x1v, a2 + y2_1))
                                sols_neg.append((x1v, a2 + y2_2))
                    curves[f_level] = (sols_pos, sols_neg)
                # plotting
                plt.figure(figsize=(9,6))
                colors = ['r', 'g', 'b', 'm', 'c']
                for i, f_level in enumerate(f_list):
                    pos, neg = curves[f_level]
                    if pos:
                        xs_pos, ys_pos = zip(*pos)
                        plt.plot(xs_pos, ys_pos, color=colors[i % len(colors)], label=f"f={f_level} (+)")
                    if neg:
                        xs_neg, ys_neg = zip(*neg)
                        plt.plot(xs_neg, ys_neg, color=colors[i % len(colors)], linestyle='--', label=f"f={f_level} (-)")

                # overlay trajectory from stage 1 if available
                if data_stage1 is not None:
                    if len(data_stage1['x1_list']) > 0:
                        plt.plot(data_stage1['x1_list'], data_stage1['x2_list'], linestyle=':', linewidth=2.5, color='black', label='x1 vs x2 (этап 1)')

                plt.xlabel("x1")
                plt.ylabel("x2")
                plt.legend()
                plt.title("Линии уровня f2")
                plt.grid(True)
                plt.tight_layout()
                plt.show()
                return curves

            results = stage_two_table_and_plots(c0, c1, c2, c3, c4, c5, a1, a2, data_stage1=data)
        case "4","2":
            def input_float(prompt, default=None):
                s = input(f"{prompt}" + (f" (по умолчанию {default})" if default is not None else "") + ": ")
                if s.strip() == "" and default is not None:
                    return default
                try:
                    return float(s)
                except:
                    print("Введено не число, попробуйте ещё раз.")
                    return input_float(prompt, default)
            print("Введите параметры (если нажмёте Enter — берутся значения по умолчанию):")
            c1 = input_float("c1", 1.0)
            c2 = input_float("c2", 1.0)
            a1 = input_float("a1", 10.0)
            a2 = input_float("a2", 10.0)
            x1_init = input_float("x1)", 0.0)
            x2_init = input_float("x2", 0.0)
            r = input_float("r", 0.1)
            f_por = input_float("f_por", 1)
            k_dr = input_float("k_dr", 1)
            steps = 100
            def stage_one(c1, c2, a1, a2, x1_init, x2_init, r, f_por, k_dr, steps=100):
                x1 = x1_init
                x2 = x2_init
                x1_list, x2_list, f1_list = [], [], []

                for k in range(steps):
                    y1 = x1 - a1
                    y2 = x2 - a2
                    f1 = c1 * (y1)**2 + c2 * (y2)**2
                    # градиент
                    g = np.array([2 * c1 * y1, 2 * c2 * y2])
                    gnorm = np.linalg.norm(g)
                    # защита от деления на ноль
                    if gnorm < 1e-12:
                        new_r = 0.0
                    else:
                        if f1 > f_por:
                            new_r = r / gnorm
                        else:
                            new_r = (r / gnorm) / k_dr

                    x1_list.append(x1)
                    x2_list.append(x2)
                    f1_list.append(f1)

                    x1 = x1 - new_r * g[0]
                    x2 = x2 - new_r * g[1]

                x1_list = np.array(x1_list)
                x2_list = np.array(x2_list)
                f1_list = np.array(f1_list)

                # эволюционный поиск минимума
                bounds = [(0, 100), (0, 100)]
                def f_obj(x):
                    return c1 * (x[0] - a1)**2 + c2 * (x[1] - a2)**2

                result = differential_evolution(f_obj, bounds, polish=True)
                x_opt = result.x
                # оставляем обновление как в других кейсах (фиксированный градиентный шаг)
                g_opt = np.array([2 * c1 * (x_opt[0] - a1), 2 * c2 * (x_opt[1] - a2)])
                x_opt_updated = np.array([x_opt[0] - r * g_opt[0], x_opt[1] - r * g_opt[1]])
                f1_opt = c1 * (x_opt_updated[0] - a1)**2 + c2 * (x_opt_updated[1] - a2)**2

                return {
                    "x1_list": x1_list,
                    "x2_list": x2_list,
                    "f1_list": f1_list,
                    "x_opt": x_opt,
                    "x_opt_updated": x_opt_updated,
                    "f1_opt": f1_opt
                }
            def plot_stage_one(data, steps=100):
                k = np.arange(1, steps+1)

                # График 1 — f1 и f1_opt
                plt.figure(figsize=(8,5))
                plt.plot(k, data['f1_list'], label='f1 (итерации)')
                plt.plot(k, [data['f1_opt']]*len(k), linestyle='--', label='f1_opt (константа)')
                plt.xlabel('k (шаг)')
                plt.ylabel('f1')
                plt.title('f1 по шагам и f1_opt')
                plt.legend()
                plt.grid(True)
                plt.tight_layout()
                plt.show()

                # График 2 — x1, x2 и их оптимальные линии
                plt.figure(figsize=(8,5))
                plt.plot(k, data['x1_list'], label='x1 (итерации)')
                plt.plot(k, data['x2_list'], label='x2 (итерации)')
                plt.plot(k, [data['x_opt_updated'][0]]*len(k), linestyle='--', label='x1_opt')
                plt.plot(k, [data['x_opt_updated'][1]]*len(k), linestyle='--', label='x2_opt')
                plt.xlabel('k (шаг)')
                plt.ylabel('Значения x')
                plt.title('x1, x2 и их оптимумы')
                plt.legend()
                plt.grid(True)
                plt.tight_layout()
                plt.show()
            data = stage_one(c1, c2, a1, a2, x1_init, x2_init, r, f_por, k_dr, steps)
            print("\nРезультаты этапа 1:")
            print(f"Оптимальные (найденные) x (до обновления): {data['x_opt']}")
            print(f"Оптимальные x после обновления: {data['x_opt_updated']}")
            print(f"f1_opt = {data['f1_opt']:.6g}")
            plot_stage_one(data, steps)
            def stage_two_table_and_plots(c1, a1, a2, x1_min=-1, x1_max=20, f_list=[350,200,50]):
                x1_values = np.arange(x1_min, x1_max+1, 1)
                results = {}
                for F in f_list:
                    plus_vals = []
                    minus_vals = []
                    for x1 in x1_values:
                        denom = a1 if abs(a1) > 1e-12 else 1e-12
                        inside = (F - c1 * (x1 - a1)**2) / denom
                        if inside < 0:
                            plus_vals.append(np.nan)
                            minus_vals.append(np.nan)
                        else:
                            root = np.sqrt(inside)
                            plus_vals.append(a2 + root)
                            minus_vals.append(a2 - root)
                    results[F] = {"plus": np.array(plus_vals), "minus": np.array(minus_vals)}
                header = ["x1"] + [f"F={F} +" for F in f_list] + [f"F={F} -" for F in f_list]
                print("\nТаблица для этапа 2:")
                print("\t".join(header))
                for i, x1 in enumerate(x1_values):
                    row = [str(x1)]
                    for F in f_list:
                        v = results[F]["plus"][i]
                        row.append(f"{v:.6g}" if not np.isnan(v) else "#Число")
                    for F in f_list:
                        v = results[F]["minus"][i]
                        row.append(f"{v:.6g}" if not np.isnan(v) else "#Число")
                    print("\t".join(row))

                # Графики
                plt.figure(figsize=(9,6))
                for F in f_list:
                    plus = results[F]["plus"]
                    minus = results[F]["minus"]
                    mask_p = ~np.isnan(plus)
                    mask_m = ~np.isnan(minus)
                    if mask_p.any():
                        plt.plot(x1_values[mask_p], plus[mask_p], label=f"F={F} (+)")
                    if mask_m.any():
                        plt.plot(x1_values[mask_m], minus[mask_m], label=f"F={F} (-)")

                extra_F = f_list[0]
                extra_series = results[extra_F]["plus"]
                mask_e = ~np.isnan(extra_series)
                if mask_e.any():
                    plt.plot(data['x1_list'], data['x2_list'], linestyle=':', linewidth=2.5, color='black', label='x1 vs x2 (этап 1)')

                plt.xlabel('x1')
                plt.ylabel('x2 (вычислено)')
                plt.title('Этап 2: линии для разных F')
                
                plt.grid(True)
                plt.tight_layout()
                plt.show()

                return results
            results = stage_two_table_and_plots(c1, a1, a2)
        case "5","2":
            def input_float(prompt, default=None):
                s = input(f"{prompt}" + (f" (по умолчанию {default})" if default is not None else "") + ": ")
                if s.strip() == "" and default is not None:
                    return default
                try:
                    return float(s)
                except:
                    print("Введено не число, попробуйте ещё раз.")
                    return input_float(prompt, default)
            print("Введите параметры (если нажмёте Enter — берутся значения по умолчанию):")
            c1 = input_float("c1", 1.0)
            c2 = input_float("c2", 1.0)
            a1 = input_float("a1", 10.0)
            a2 = input_float("a2", 10.0)
            x1_init = input_float("x1)", 0.0)
            x2_init = input_float("x2", 0.0)
            r = input_float("r", 0.1)  # можно оставить для сравнения, но наискорейший шаг вычисляем явным образом
            f_por = input_float("f_por", 1)  # не обязателен для метода, оставлен для совместимости интерфейса
            k_dr = input_float("k_dr", 1)    # не обязателен
            steps = 100
            def stage_one(c1, c2, a1, a2, x1_init, x2_init, steps=100):
                x1 = x1_init
                x2 = x2_init
                x1_list, x2_list, f1_list = [], [], []

                # матрица Гессиана для квадратичной функции f1
                H = np.array([[2 * c1, 0.0],
                              [0.0, 2 * c2]])

                for k in range(steps):
                    y1 = x1 - a1
                    y2 = x2 - a2
                    f1 = c1 * (y1)**2 + c2 * (y2)**2
                    # градиент
                    g = np.array([2 * c1 * y1, 2 * c2 * y2])

                    # точный шаг для квадратичной функции (наискорейший спуск)
                    denom = g @ (H @ g)
                    if abs(denom) < 1e-14:
                        alpha = 0.0
                    else:
                        alpha = (g @ g) / denom

                    x1_list.append(x1)
                    x2_list.append(x2)
                    f1_list.append(f1)

                    x1 = x1 - alpha * g[0]
                    x2 = x2 - alpha * g[1]

                x1_list = np.array(x1_list)
                x2_list = np.array(x2_list)
                f1_list = np.array(f1_list)

                # эволюционный поиск минимума для сравнения
                bounds = [(0, 100), (0, 100)]
                def f_obj(x):
                    return c1 * (x[0] - a1)**2 + c2 * (x[1] - a2)**2

                result = differential_evolution(f_obj, bounds, polish=True)
                x_opt = result.x
                # обновление: сделать одно наискорейшее-шаговое обновление (alpha в точке x_opt)
                g_opt = np.array([2 * c1 * (x_opt[0] - a1), 2 * c2 * (x_opt[1] - a2)])
                denom_opt = g_opt @ (H @ g_opt)
                alpha_opt = 0.0 if abs(denom_opt) < 1e-14 else (g_opt @ g_opt) / denom_opt
                x_opt_updated = np.array([x_opt[0] - alpha_opt * g_opt[0], x_opt[1] - alpha_opt * g_opt[1]])
                f1_opt = c1 * (x_opt_updated[0] - a1)**2 + c2 * (x_opt_updated[1] - a2)**2

                return {
                    "x1_list": x1_list,
                    "x2_list": x2_list,
                    "f1_list": f1_list,
                    "x_opt": x_opt,
                    "x_opt_updated": x_opt_updated,
                    "f1_opt": f1_opt
                }
            def plot_stage_one(data, steps=100):
                k = np.arange(1, steps+1)

                # График 1 — f1 и f1_opt
                plt.figure(figsize=(8,5))
                plt.plot(k, data['f1_list'], label='f1 (итерации)')
                plt.plot(k, [data['f1_opt']]*len(k), linestyle='--', label='f1_opt (константа)')
                plt.xlabel('k (шаг)')
                plt.ylabel('f1')
                plt.title('f1 по шагам и f1_opt')
                plt.legend()
                plt.grid(True)
                plt.tight_layout()
                plt.show()

                # График 2 — x1, x2 и их оптимальные линии
                plt.figure(figsize=(8,5))
                plt.plot(k, data['x1_list'], label='x1 (итерации)')
                plt.plot(k, data['x2_list'], label='x2 (итерации)')
                plt.plot(k, [data['x_opt_updated'][0]]*len(k), linestyle='--', label='x1_opt')
                plt.plot(k, [data['x_opt_updated'][1]]*len(k), linestyle='--', label='x2_opt')
                plt.xlabel('k (шаг)')
                plt.ylabel('Значения x')
                plt.title('x1, x2 и их оптимумы (наискорейший спуск)')
                plt.legend()
                plt.grid(True)
                plt.tight_layout()
                plt.show()
            data = stage_one(c1, c2, a1, a2, x1_init, x2_init, steps)
            print("\nРезультаты этапа 1:")
            print(f"Оптимальные (найденные) x (до обновления): {data['x_opt']}")
            print(f"Оптимальные x после обновления: {data['x_opt_updated']}")
            print(f"f1_opt = {data['f1_opt']:.6g}")
            plot_stage_one(data, steps)
            def stage_two_table_and_plots(c1, a1, a2, x1_min=-1, x1_max=20, f_list=[350,200,50]):
                x1_values = np.arange(x1_min, x1_max+1, 1)
                results = {}
                for F in f_list:
                    plus_vals = []
                    minus_vals = []
                    for x1 in x1_values:
                        denom = a1 if abs(a1) > 1e-12 else 1e-12
                        inside = (F - c1 * (x1 - a1)**2) / denom
                        if inside < 0:
                            plus_vals.append(np.nan)
                            minus_vals.append(np.nan)
                        else:
                            root = np.sqrt(inside)
                            plus_vals.append(a2 + root)
                            minus_vals.append(a2 - root)
                    results[F] = {"plus": np.array(plus_vals), "minus": np.array(minus_vals)}
                header = ["x1"] + [f"F={F} +" for F in f_list] + [f"F={F} -" for F in f_list]
                print("\nТаблица для этапа 2:")
                print("\t".join(header))
                for i, x1 in enumerate(x1_values):
                    row = [str(x1)]
                    for F in f_list:
                        v = results[F]["plus"][i]
                        row.append(f"{v:.6g}" if not np.isnan(v) else "#Число")
                    for F in f_list:
                        v = results[F]["minus"][i]
                        row.append(f"{v:.6g}" if not np.isnan(v) else "#Число")
                    print("\t".join(row))

                # Графики
                plt.figure(figsize=(9,6))
                for F in f_list:
                    plus = results[F]["plus"]
                    minus = results[F]["minus"]
                    mask_p = ~np.isnan(plus)
                    mask_m = ~np.isnan(minus)
                    if mask_p.any():
                        plt.plot(x1_values[mask_p], plus[mask_p], label=f"F={F} (+)")
                    if mask_m.any():
                        plt.plot(x1_values[mask_m], minus[mask_m], label=f"F={F} (-)")

                extra_F = f_list[0]
                extra_series = results[extra_F]["plus"]
                mask_e = ~np.isnan(extra_series)
                if mask_e.any():
                    plt.plot(data['x1_list'], data['x2_list'], linestyle=':', linewidth=2.5, color='black', label='x1 vs x2 (этап 1)')

                plt.xlabel('x1')
                plt.ylabel('x2 (вычислено)')
                plt.title('Этап 2: линии для разных F')
                
                plt.grid(True)
                plt.tight_layout()
                plt.show()

                return results
            results = stage_two_table_and_plots(c1, a1, a2)

        


cont = True
while cont == True:
    choose1 = input("Выберите вид прогноза СП\n1.f1 c пост.шг\n2.f1 числ.пр.\n3.f2 числ.пр.\n4.f1 с дробл.шг\n5.f1 наиск.спск\n" )
    choose2 = input("Выберите режим\n1.Тестовый\n2.Рабочий\n") 
    handle_command(choose1, choose2)
    ans = input("Продолжить?[Y|n]\n")
    if ans == 'n':
        cont = False
    