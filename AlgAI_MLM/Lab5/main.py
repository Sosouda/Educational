from openpyxl import load_workbook
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def handle_command(command1, command2):
    book = load_workbook(filename= "задание5.xlsx", data_only=True)
    xs = []
    fotx = []
    ys = []
    fprognk = []
    fprognm = []
    x3 = []
    menmnk = []
    mexmnk = []
    detmnk = []
    menmnm = []
    mexmnm = []
    detmnm = []
    karm1 = []
    karm2 = []
    karm3 = []
    chast1m = []
    chast2m = []
    chast3m = []
    chast1p = []
    chast2p = []
    chast3p = []
    match (command1, command2):
        case "1","1":
            Liner = book['Эксп. апрокс. МНК-МНМ']
            a = Liner['B7'].value
            b = Liner['B8'].value
            c = Liner['B9'].value
            h = Liner['B10'].value
            print("Объем выборки = ",Liner['B4'].value,'\n',
                  "Начало диапазона варьир. x,p= ",Liner['B5'].value,'\n',
                  "Конец диапазона варьир. x, q=",Liner['B6'].value,'\n',
                  "Параметры эксп. модели:\n"
                  "m_a=",a,'\n',
                  "m_b=",b,'\n',
                  "m_c=",c,'\n',
                  "m_h",h,'\n')
            a_mnk = Liner['F3'].value
            b_mnk = Liner['F4'].value
            c_mnk = Liner['F5'].value
            v_mnk = Liner['F6'].value
            
            print("MHK оценки параметров модели\n",
                  "a =",a_mnk,"\n",
                  "b =",b_mnk,"\n",
                  "c =",c_mnk,"\n",
                  "v =",v_mnk,"\n")
            
            for i in range(23,126):
                xs.append(Liner['B' + str(i)].value)
                fotx.append(Liner['D' + str(i)].value)
                ys.append(Liner['E' + str(i)].value)
                fprognk.append(Liner['G' + str(i)].value)
                fprognm.append(Liner['AD'+str(i)].value)
            for i in range(23,32):
                karm1.append(Liner['T' + str(i)].value)
                chast1m.append(Liner['U' + str(i)].value)
            for i in range(36,45):
                chast1p.append(Liner['U' + str(i)].value)
            for i in range(50,59):
                karm2.append(Liner['T' + str(i)].value)
                chast2m.append(Liner['U' + str(i)].value)
            for i in range(63,72):
                chast2p.append(Liner['U' + str(i)].value)
            for i in range(79,88):
                karm3.append(Liner['T' + str(i)].value)
                chast3m.append(Liner['U' + str(i)].value)
            for i in range(92,101):
                chast3p.append(Liner['U' + str(i)].value)

            x3.append(Liner['I16'].value)
            x3.append(Liner['J16'].value)
            x3.append(Liner['K16'].value)
            menmnk.append(Liner['P11'].value)
            menmnk.append(Liner['Q11'].value)
            menmnk.append(Liner['R11'].value)
            mexmnk.append(Liner['P12'].value)
            mexmnk.append(Liner['Q12'].value)
            mexmnk.append(Liner['R12'].value)
            detmnk.append(Liner['M13'].value)
            detmnk.append(Liner['N13'].value)
            detmnk.append(Liner['O13'].value)
            
            fig, ax = plt.subplots()
            plt.scatter(xs, fotx)
            plt.scatter(xs, ys)
            plt.scatter(xs, fprognk)
            fig, bx = plt.subplots()
            plt.scatter(xs,ys)
            plt.scatter(x3, menmnk)
            plt.scatter(x3, mexmnk) 
            plt.scatter(x3, detmnk)
            fig, bx = plt.subplots()
            plt.scatter(xs,ys)
            fig, bx = plt.subplots()
            plt.bar(karm1, chast1m)
            plt.bar(karm1, chast1p) 
            fig, bx = plt.subplots()
            plt.bar(karm2, chast2m)
            plt.bar(karm2, chast2p)
            fig, bx = plt.subplots()
            plt.bar(karm3, chast3m)
            plt.bar(karm3, chast3p)
            plt.show()

            a_mnm = Liner['H3'].value
            b_mnm = Liner['H4'].value
            c_mnm = Liner['H5'].value
            v_mnm = Liner['H6'].value
            print("MHM оценки параметров модели\n",
                  "a =",a_mnm,"\n",
                  "b =",b_mnm,"\n",
                  "c =",c_mnm,"\n",
                  "v =",v_mnm,"\n")
            
            menmnm.append(Liner['AM22'].value)
            menmnm.append(Liner['AN22'].value)
            menmnm.append(Liner['AO22'].value)
            mexmnm.append(Liner['AM23'].value)
            mexmnm.append(Liner['AN23'].value)
            mexmnm.append(Liner['AO23'].value)
            detmnm.append(Liner['AI24'].value)
            detmnm.append(Liner['AJ24'].value)
            detmnm.append(Liner['AK24'].value)

            fig, cx = plt.subplots()
            plt.scatter(xs, fotx)
            plt.scatter(xs, ys)
            plt.scatter(xs, fprognm)
            fig, dx = plt.subplots()
            plt.scatter(xs, ys)
            plt.scatter(x3, menmnm)
            plt.scatter(x3, mexmnm) 
            plt.scatter(x3, detmnm)
            plt.show()
        case "2","1":
            Liner = book['Син. апрокс. МНК-МНМ']
            a = Liner['B11'].value
            b = Liner['B12'].value
            c = Liner['B13'].value
            d = Liner['B14'].value
            f = Liner['B15'].value
            h = Liner['B16'].value
            print("Объем выборки = ",Liner['B4'].value,'\n',
                  "Начало диапазона варьир. x,p= ",Liner['B5'].value,'\n',
                  "Конец диапазона варьир. x, q=",Liner['B6'].value,'\n',
                  "Параметры эксп. модели:\n"
                  "m_a=",a,'\n',
                  "m_b=",b,'\n',
                  "m_c=",c,'\n',
                  "m_d=",d,"\n",
                  "m_f=",f,"\n",
                  "m_h",h,'\n')
            a_mnk = Liner['F3'].value
            b_mnk = Liner['F4'].value
            c_mnk = Liner['F5'].value
            d_mnk = Liner['F6'].value
            f_mnk = Liner['F7'].value
            v_mnk = Liner['F8'].value

            
            print("MHK оценки параметров модели\n",
                  "a =",a_mnk,"\n",
                  "b =",b_mnk,"\n",
                  "c =",c_mnk,"\n",
                  "d =",d_mnk,"\n",
                  "f =",f_mnk,"\n",
                  "v =",v_mnk,"\n")
            
            for i in range(23,126):
                xs.append(Liner['B' + str(i)].value)
                fotx.append(Liner['D' + str(i)].value)
                ys.append(Liner['E' + str(i)].value)
                fprognk.append(Liner['G' + str(i)].value)
                fprognm.append(Liner['AD'+str(i)].value)
            for i in range(23,32):
                karm1.append(Liner['T' + str(i)].value)
                chast1m.append(Liner['U' + str(i)].value)
            for i in range(36,45):
                chast1p.append(Liner['U' + str(i)].value)
            for i in range(50,59):
                karm2.append(Liner['T' + str(i)].value)
                chast2m.append(Liner['U' + str(i)].value)
            for i in range(63,72):
                chast2p.append(Liner['U' + str(i)].value)
            for i in range(79,88):
                karm3.append(Liner['T' + str(i)].value)
                chast3m.append(Liner['U' + str(i)].value)
            for i in range(92,101):
                chast3p.append(Liner['U' + str(i)].value)

            x3.append(Liner['I16'].value)
            x3.append(Liner['J16'].value)
            x3.append(Liner['K16'].value)
            menmnk.append(Liner['P11'].value)
            menmnk.append(Liner['Q11'].value)
            menmnk.append(Liner['R11'].value)
            mexmnk.append(Liner['P12'].value)
            mexmnk.append(Liner['Q12'].value)
            mexmnk.append(Liner['R12'].value)
            detmnk.append(Liner['M13'].value)
            detmnk.append(Liner['N13'].value)
            detmnk.append(Liner['O13'].value)
            
            fig, ax = plt.subplots()
            plt.scatter(xs, fotx)
            plt.scatter(xs, ys)
            plt.scatter(xs, fprognk)
            fig, bx = plt.subplots()
            plt.scatter(xs,ys)
            plt.scatter(x3, menmnk)
            plt.scatter(x3, mexmnk) 
            plt.scatter(x3, detmnk)
            fig, bx = plt.subplots()
            plt.scatter(xs,ys)
            fig, bx = plt.subplots()
            plt.bar(karm1, chast1m)
            plt.bar(karm1, chast1p) 
            fig, bx = plt.subplots()
            plt.bar(karm2, chast2m)
            plt.bar(karm2, chast2p)
            fig, bx = plt.subplots()
            plt.bar(karm3, chast3m)
            plt.bar(karm3, chast3p)
            plt.show()

            a_mnm = Liner['H3'].value
            b_mnm = Liner['H4'].value
            c_mnm = Liner['H5'].value
            d_mnm = Liner['H6'].value
            f_mnm = Liner['H7'].value
            v_mnm = Liner['H8'].value
            print("MHM оценки параметров модели\n",
                  "a =",a_mnm,"\n",
                  "b =",b_mnm,"\n",
                  "c =",c_mnm,"\n",
                  "d =",d_mnm,"\n",
                  "f =",f_mnm,"\n",
                  "v =",v_mnm,"\n")
            
            menmnm.append(Liner['AM22'].value)
            menmnm.append(Liner['AN22'].value)
            menmnm.append(Liner['AO22'].value)
            mexmnm.append(Liner['AM23'].value)
            mexmnm.append(Liner['AN23'].value)
            mexmnm.append(Liner['AO23'].value)
            detmnm.append(Liner['AI24'].value)
            detmnm.append(Liner['AJ24'].value)
            detmnm.append(Liner['AK24'].value)

            fig, cx = plt.subplots()
            plt.scatter(xs, fotx)
            plt.scatter(xs, ys)
            plt.scatter(xs, fprognm)
            fig, dx = plt.subplots()
            plt.scatter(xs, ys)
            plt.scatter(x3, menmnm)
            plt.scatter(x3, mexmnm) 
            plt.scatter(x3, detmnm)
            plt.show()
        case "1","2":
            def model(x, params):
                a, b, c = params
                return a - b * np.exp(-c * x)

            def sum_squares_obj(params, x, y):
                res = y - model(x, params)
                return np.sum(res**2)

            def sum_abs_obj(params, x, y):
                res = y - model(x, params)
                return np.sum(np.abs(res))
            n = int(input("Объем выборки n: "))
            p = float(input("начало диапазона x, p: "))
            q = float(input("конец диапазона x, q: ") or 5.0)
            print("параметры истинной экспоненциальной модели (a, b, c, h):")
            a_true = float(input("   a: "))
            b_true = float(input("   b: "))
            c_true = float(input("   c: "))
            h = float(input("   h: "))
        
           
            x = np.random.uniform(p, q, size=n)
            z = np.random.normal(0.0, 1.0, size=n)  
            y_true_det = model(x, (a_true, b_true, c_true))  
            y = y_true_det + h * z  
        
            
            init_guess = np.array([np.mean(y), 1.0, 0.5])
            res_ls = minimize(sum_squares_obj, init_guess, args=(x, y), method='Nelder-Mead')
            params_ls = res_ls.x
            print("\nОценки (метод МНК): a, b, c =", params_ls)
        
        
            x_plot = np.linspace(p, q, 400)
            f_true_plot = model(x_plot, (a_true, b_true, c_true))
            f_ls_plot = model(x_plot, params_ls)
        
            
            plt.figure(figsize=(10,6))
            plt.scatter(x, y, s=15, alpha=0.6, label='y')
            plt.plot(x_plot, f_true_plot, linewidth=2, label='f_true ', linestyle='--')
            plt.plot(x_plot, f_ls_plot, linewidth=2, label='f_MNK ')
            plt.xlabel('x')
            plt.ylabel('y / f(x)')
            plt.legend()
            plt.grid(True)
            plt.show()
        
            
            s = int(input("\n Объем прогнозной выборки s: "))
            u = float(input(" Интервал прогнозирования: "))
            karm = int(input(" Количество карманов karm для гистограмм: "))
        
            
            x1 = q + u
            x2 = x1 + u
            x3 = x2 + u
            x_fore_list = [x1, x2, x3]
            print("\nПрогнозные x:", x_fore_list)
        
            
            forecast_results = []
            for xf in x_fore_list:
                zf = np.random.normal(0.0, 1.0, size=s) 
                y_mod = model(xf, (a_true, b_true, c_true)) + h * zf  
                y_progn = model(xf, params_ls) + h * zf  
                det = model(xf, (a_true, b_true, c_true))
                forecast_results.append({
                    'x': xf,
                    'z': zf,
                    'y_mod': y_mod,
                    'y_progn': y_progn,
                    'det': det
                })
        
            
            fig_hist, axes = plt.subplots(3, 1, figsize=(8, 10))
            fig_hist.suptitle('Гистограммы: моделируемые и прогнозные по карманам')
            for i, res in enumerate(forecast_results):
                y_mod = res['y_mod']
                y_progn = res['y_progn']
                ymin = y_mod.min()
                ymax = y_mod.max()
                if np.isclose(ymin, ymax):
                    ymax = ymin + 1e-6
                bin_width = (ymax - ymin) / karm
                bins = np.linspace(ymin, ymax, karm+1)
                ax = axes[i]
                counts_mod, _ = np.histogram(y_mod, bins=bins)
                counts_progn, _ = np.histogram(y_progn, bins=bins)
                centers = (bins[:-1] + bins[1:]) / 2
                width = (bins[1] - bins[0]) * 0.4
                ax.bar(centers - width/2, counts_mod, width=width, alpha=0.7, label='y_mod ')
                ax.bar(centers + width/2, counts_progn, width=width, alpha=0.7, label='y_progn ')
                ax.set_xlabel(f'Значение y (карманы) для x={res["x"]:.3f}')
                ax.set_ylabel('Частота')
                ax.legend()
                ax.grid(True)
            plt.tight_layout(rect=[0, 0.03, 1, 0.95])
            plt.show()
        
            
            det_orig = y_true_det  
        
            
            plt.figure(figsize=(10,6))
            plt.scatter(x, y, s=15, alpha=0.5, label='Наблюдения y ')
            
            sort_idx = np.argsort(x_plot)
            plt.plot(x_plot[sort_idx], model(x_plot[sort_idx], (a_true, b_true, c_true)), label='det_true ', linewidth=2)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Данные, детерминантная функция и прогнозные интервалы')
            
            for res in forecast_results:
                xf = res['x']
                det = res['det']
                y_mod = res['y_mod']
                mean_y = np.mean(y_mod)
                std_y = np.std(y_mod, ddof=1)
                
                plt.scatter([xf], [det], color='black', marker='D', s=60, label=f'det @ x={xf:.2f}' if xf==x1 else "")
                plt.errorbar([xf], [mean_y], yerr=[3*std_y], fmt='o', capsize=6, label=f'mean(y_mod)±3σ @ x={xf:.2f}' if xf==x1 else "")
            plt.legend()
            plt.grid(True)
            plt.show()
        
            
            res_lad = minimize(sum_abs_obj, init_guess, args=(x, y), method='Nelder-Mead')
            params_lad = res_lad.x
            print("\nОценки (метод наименьших модулей): a, b, c =", params_lad)
        
            
            x_plot = np.linspace(p, q, 400)
            plt.figure(figsize=(10,6))
            plt.scatter(x, y, s=15, alpha=0.5, label='Наблюдения y ')
            plt.plot(x_plot, model(x_plot, (a_true, b_true, c_true)), linewidth=2, linestyle='--', label='f_true')
            plt.plot(x_plot, model(x_plot, params_lad), linewidth=2, label='f_MNM (наим. модулей)')
            plt.xlabel('x')
            plt.ylabel('y')
            
            plt.legend()
            plt.grid(True)
            plt.show()
        
            
            plt.figure(figsize=(10,6))
            plt.scatter(x, y, s=15, alpha=0.5, label='Наблюдения y ')
            plt.plot(x_plot, model(x_plot, (a_true, b_true, c_true)), linewidth=2, linestyle='--', label='f_true')
            plt.plot(x_plot, model(x_plot, params_lad), linewidth=2, label='f_MNM')
            
            for res in forecast_results:
                xf = res['x']
                plt.scatter([xf], [res['det']], marker='D', s=60, label=f'det @ {xf:.2f}' if xf==x1 else "")
            plt.xlabel('x')
            plt.ylabel('y')
            
            plt.legend()
            plt.grid(True)
            plt.show()
        
            
            print("\nСводка оценок:")
            print("True parameters: a, b, c =", (a_true, b_true, c_true))
            print("MNK estimates   : a, b, c =", params_ls)
            print("MNM estimates   : a, b, c =", params_lad)
        case "2","2":
            def model(x, params):
                a, b, c, d, f = params
                return a + b * x + c * np.sin(d * (x - f))

            def sum_squares_obj(params, x, y):
                res = y - model(x, params)
                return np.sum(res**2)

            def sum_abs_obj(params, x, y):
                res = y - model(x, params)
                return np.sum(np.abs(res))
            n = int(input("Объем выборки n: "))
            p = float(input("начало диапазона x, p: "))
            q = float(input("конец диапазона x, q: ") or 5.0)
            print("параметры истинной экспоненциальной модели (a, b, c,d,f, h):")
            a_true = float(input("   a: "))
            b_true = float(input("   b: "))
            c_true = float(input("   c: "))
            d_true = float(input("   d: "))
            f_true = float(input("   f: "))
            h = float(input("   h: "))
        
           
            x = np.random.uniform(p, q, size=n)
            z = np.random.normal(0.0, 1.0, size=n)  
            y_true_det = model(x, (a_true, b_true, c_true, d_true, f_true))
            y = y_true_det + h * z  
        
            
            init_guess = np.array([np.mean(y), 1.0, 1.0, 1.0, 0.0])
            res_ls = minimize(sum_squares_obj, init_guess, args=(x, y), method='Nelder-Mead')
            params_ls = res_ls.x
            print("\nОценки (метод МНК): a, b, c,d,f =", params_ls)
        
        
            x_plot = np.linspace(p, q, 400)
            f_true_plot = model(x_plot, (a_true, b_true, c_true, d_true, f_true))
            f_ls_plot = model(x_plot, params_ls)
        
            
            plt.figure(figsize=(10,6))
            plt.scatter(x, y, s=15, alpha=0.6, label='y')
            plt.plot(x_plot, f_true_plot, linewidth=2, label='f_true ', linestyle='--')
            plt.plot(x_plot, f_ls_plot, linewidth=2, label='f_MNK ')
            plt.xlabel('x')
            plt.ylabel('y / f(x)')
            plt.legend()
            plt.grid(True)
            plt.show()
        
            
            s = int(input("\n Объем прогнозной выборки s: "))
            u = float(input(" Интервал прогнозирования: "))
            karm = int(input(" Количество карманов karm для гистограмм: "))
        
            
            x1 = q + u
            x2 = x1 + u
            x3 = x2 + u
            x_fore_list = [x1, x2, x3]
            print("\nПрогнозные x:", x_fore_list)
        
            
            forecast_results = []
            for xf in x_fore_list:
                zf = np.random.normal(0.0, 1.0, size=s) 
                y_mod = model(xf, (a_true, b_true, c_true,d_true,f_true)) + h * zf  
                y_progn = model(xf, params_ls) + h * zf  
                det = model(xf, (a_true, b_true, c_true,d_true,f_true))
                forecast_results.append({
                    'x': xf,
                    'z': zf,
                    'y_mod': y_mod,
                    'y_progn': y_progn,
                    'det': det
                })
        
            
            fig_hist, axes = plt.subplots(3, 1, figsize=(8, 10))
            fig_hist.suptitle('Гистограммы: моделируемые и прогнозные по карманам')
            for i, res in enumerate(forecast_results):
                y_mod = res['y_mod']
                y_progn = res['y_progn']
                ymin = y_mod.min()
                ymax = y_mod.max()
                if np.isclose(ymin, ymax):
                    ymax = ymin + 1e-6
                bin_width = (ymax - ymin) / karm
                bins = np.linspace(ymin, ymax, karm+1)
                ax = axes[i]
                counts_mod, _ = np.histogram(y_mod, bins=bins)
                counts_progn, _ = np.histogram(y_progn, bins=bins)
                centers = (bins[:-1] + bins[1:]) / 2
                width = (bins[1] - bins[0]) * 0.4
                ax.bar(centers - width/2, counts_mod, width=width, alpha=0.7, label='y_mod ')
                ax.bar(centers + width/2, counts_progn, width=width, alpha=0.7, label='y_progn ')
                ax.set_xlabel(f'Значение y (карманы) для x={res["x"]:.3f}')
                ax.set_ylabel('Частота')
                ax.legend()
                ax.grid(True)
            plt.tight_layout(rect=[0, 0.03, 1, 0.95])
            plt.show()
        
            
            det_orig = y_true_det  
        
            
            plt.figure(figsize=(10,6))
            plt.scatter(x, y, s=15, alpha=0.5, label='Наблюдения y ')
            
            sort_idx = np.argsort(x_plot)
            plt.plot(x_plot[sort_idx], model(x_plot[sort_idx], (a_true, b_true, c_true,d_true,f_true)), label='det_true ', linewidth=2)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Данные, детерминантная функция и прогнозные интервалы')
            
            for res in forecast_results:
                xf = res['x']
                det = res['det']
                y_mod = res['y_mod']
                mean_y = np.mean(y_mod)
                std_y = np.std(y_mod, ddof=1)
                
                plt.scatter([xf], [det], color='black', marker='D', s=60, label=f'det @ x={xf:.2f}' if xf==x1 else "")
                plt.errorbar([xf], [mean_y], yerr=[3*std_y], fmt='o', capsize=6, label=f'mean(y_mod)±3σ @ x={xf:.2f}' if xf==x1 else "")
            plt.legend()
            plt.grid(True)
            plt.show()
        
            
            res_lad = minimize(sum_abs_obj, init_guess, args=(x, y), method='Nelder-Mead')
            params_lad = res_lad.x
            print("\nОценки (метод наименьших модулей): a, b, c =", params_lad)
        
            
            x_plot = np.linspace(p, q, 400)
            plt.figure(figsize=(10,6))
            plt.scatter(x, y, s=15, alpha=0.5, label='Наблюдения y ')
            plt.plot(x_plot, model(x_plot, (a_true, b_true, c_true,d_true,f_true)), linewidth=2, linestyle='--', label='f_true')
            plt.plot(x_plot, model(x_plot, params_lad), linewidth=2, label='f_MNM (наим. модулей)')
            plt.xlabel('x')
            plt.ylabel('y')
            
            plt.legend()
            plt.grid(True)
            plt.show()
        
            
            plt.figure(figsize=(10,6))
            plt.scatter(x, y, s=15, alpha=0.5, label='Наблюдения y ')
            plt.plot(x_plot, model(x_plot, (a_true, b_true, c_true,d_true,f_true)), linewidth=2, linestyle='--', label='f_true')
            plt.plot(x_plot, model(x_plot, params_lad), linewidth=2, label='f_MNM')
            
            for res in forecast_results:
                xf = res['x']
                plt.scatter([xf], [res['det']], marker='D', s=60, label=f'det @ {xf:.2f}' if xf==x1 else "")
            plt.xlabel('x')
            plt.ylabel('y')
            
            plt.legend()
            plt.grid(True)
            plt.show()
        
            
            print("\nСводка оценок:")
            print("True parameters: a, b, c =", (a_true, b_true, c_true))
            print("MNK estimates   : a, b, c =", params_ls)
            print("MNM estimates   : a, b, c =", params_lad)
            
        


cont = True
while cont == True:
    choose1 = input("Выберите вид прогноза СП\n1.Экспоненциальный\n2.Синусоидальный\n" )
    choose2 = input("Выберите режим\n1.Тестовый\n2.Рабочий\n") 
    handle_command(choose1, choose2)
    ans = input("Продолжить?[Y|n]\n")
    if ans == 'n':
        cont = False
    