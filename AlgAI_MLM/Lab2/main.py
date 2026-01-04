from openpyxl import load_workbook
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
def beta_calcing(Beta, command):
    num = []
    ind = []
    karm = []
    chast = []
    otn = []
    teor = []
    fotx = []
    ro =[]
    karms = []
    match(command):
        case "1":
            print("a =",Beta['D5'].value,"\n","b =",Beta['D6'].value,
                  "\n","Объем выборки K =",Beta['J9'].value)
            for i in range(12,116):
                num.append(Beta['C' + str(i)].value)
                ind.append(Beta['A' + str(i)].value)
            for i in range(15,29):
                chast.append(Beta['I' + str(i)].value)
                karm.append(Beta['H' + str(i)].value)
                otn.append(Beta['K' + str(i)].value)
                teor.append(Beta['M' + str(i)].value)
                fotx.append(Beta['N' + str(i)].value)
                ro.append(Beta['O' + str(i)].value)
                karms.append(i-14)
            
            print("Мин= ",Beta['J5'].value,"\n","Макс= ",Beta['J6'].value,"\n",
                  "Карман= ",Beta['J7'].value,"\n","Число карманов= ",Beta['J8'].value,"\n",)

            print("Карман|Частота\n")
            for i in range(len(karm)):
               print(str(karm[i])+"|"+str(chast[i])+ "\n") 
            print("Отн.частота|Теор.|F(x)|Плотность\n")
            for i in range(len(otn)):
               print(str(otn[i])+"|"+str(teor[i])+"|"+str(fotx[i])+"|"+str(ro[i])+"\n")

            fig, ax = plt.subplots()
            ax.plot(ind, num, label="Равномерное")
            ax.legend()

            fig, bx = plt.subplots()
            bx.bar(chast, karm,label="Частота")
            bx.legend()

            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x, otn,width = 0.15, label='Отн.частота', color='red')
            plt.plot(x, ro, label='Плотность', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])

            fig, fx = plt.subplots()
            fx.plot(karms, fotx, label="F(x)")
            print("MO= ",Beta['L101'].value,"\n","CKO= ",Beta['L102'].value,"\n",
                  "Disp= ",Beta['L103'].value,"\n","Assim= ",Beta['L104'].value,"\n",
                  "Excess= ",Beta['L105'].value,"\n",)
            plt.show()
        case "2":
            print("a =",Beta['V5'].value,"\n","b =",Beta['V6'].value,
                  "\n","Объем выборки K =",Beta['AB9'].value)
            for i in range(12,1061):
                num.append(Beta['U' + str(i)].value)
                ind.append(Beta['S' + str(i)].value)
            for i in range(15,30):
                chast.append(Beta['Z' + str(i)].value)
                karm.append(Beta['Y' + str(i)].value)
                otn.append(Beta['AB' + str(i)].value)
                teor.append(Beta['AD' + str(i)].value)
                fotx.append(Beta['AE' + str(i)].value)
                ro.append(Beta['AF' + str(i)].value)
                karms.append(i-14)
            
            print("Мин= ",Beta['AB5'].value,"\n","Макс= ",Beta['AB6'].value,"\n",
                  "Карман= ",Beta['AB7'].value,"\n","Число карманов= ",Beta['AB8'].value,"\n",)

            print("Карман|Частота\n")
            for i in range(len(karm)):
               print(str(karm[i])+"|"+str(chast[i])+ "\n") 
            print("Отн.частота|Теор.|F(x)|Плотность\n")
            for i in range(len(otn)):
               print(str(otn[i])+"|"+str(teor[i])+"|"+str(fotx[i])+"|"+str(ro[i])+"\n")

            fig, ax = plt.subplots()
            ax.plot(ind, num, label="Равномерное")
            ax.legend()

            fig, bx = plt.subplots()
            bx.bar(chast, karm,label="Частота")
            bx.legend()

            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x, otn,width = 0.15, label='Отн.частота', color='red')
            plt.plot(x, ro, label='Плотность', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])

            fig, fx = plt.subplots()
            fx.plot(karms, fotx, label="F(x)")
            print("MO= ",Beta['AC95'].value,"\n","CKO= ",Beta['AC96'].value,"\n",
                  "Disp= ",Beta['AC97'].value,"\n","Assim= ",Beta['AC98'].value,"\n",
                  "Excess= ",Beta['AC99'].value,"\n",)
            plt.show()
        case "3":
            print("a =",Beta['AL5'].value,"\n","b =",Beta['AL6'].value,
                  "\n","Объем выборки K =",Beta['AQ9'].value)
            for i in range(12,1061):
                num.append(Beta['AK' + str(i)].value)
                ind.append(Beta['AI' + str(i)].value)
            for i in range(15,30):
                chast.append(Beta['AP' + str(i)].value)
                karm.append(Beta['AO' + str(i)].value)
                otn.append(Beta['AR' + str(i)].value)
                teor.append(Beta['AT' + str(i)].value)
                fotx.append(Beta['AU' + str(i)].value)
                ro.append(Beta['AV' + str(i)].value)
                karms.append(i-14)
            
            print("Мин= ",Beta['AQ5'].value,"\n","Макс= ",Beta['AQ6'].value,"\n",
                  "Карман= ",Beta['AQ7'].value,"\n","Число карманов= ",Beta['AQ8'].value,"\n",)

            print("Карман|Частота\n")
            for i in range(len(karm)):
               print(str(karm[i])+"|"+str(chast[i])+ "\n") 
            print("Отн.частота|Теор.|F(x)|Плотность\n")
            for i in range(len(otn)):
               print(str(otn[i])+"|"+str(teor[i])+"|"+str(fotx[i])+"|"+str(ro[i])+"\n")

            fig, ax = plt.subplots()
            ax.plot(ind, num, label="Равномерное")
            ax.legend()

            fig, bx = plt.subplots()
            bx.bar(chast, karm,label="Частота")
            bx.legend()

            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x, otn,width = 0.15, label='Отн.частота', color='red')
            plt.plot(x, ro, label='Плотность', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])

            fig, fx = plt.subplots()
            fx.plot(karms, fotx, label="F(x)")
            print("MO= ",Beta['AS99'].value,"\n","CKO= ",Beta['AS100'].value,"\n",
                  "Disp= ",Beta['AS101'].value,"\n","Assim= ",Beta['AS102'].value,"\n",
                  "Excess= ",Beta['AS103'].value,"\n",)
            plt.show()
        case "4":
            print("a =",Beta['BB5'].value,"\n","b =",Beta['BB6'].value,
                  "\n","Объем выборки K =",Beta['BH9'].value)
            for i in range(12,1061):
                num.append(Beta['BA' + str(i)].value)
                ind.append(Beta['AY' + str(i)].value)
            for i in range(15,31):
                chast.append(Beta['BF' + str(i)].value)
                karm.append(Beta['BE' + str(i)].value)
                otn.append(Beta['BH' + str(i)].value)
                teor.append(Beta['BJ' + str(i)].value)
                fotx.append(Beta['BK' + str(i)].value)
                ro.append(Beta['BL' + str(i)].value)
                karms.append(i-14)
            
            print("Мин= ",Beta['BH5'].value,"\n","Макс= ",Beta['BH6'].value,"\n",
                  "Карман= ",Beta['BH7'].value,"\n","Число карманов= ",Beta['BH8'].value,"\n",)

            print("Карман|Частота\n")
            for i in range(len(karm)):
               print(str(karm[i])+"|"+str(chast[i])+ "\n") 
            print("Отн.частота|Теор.|F(x)|Плотность\n")
            for i in range(len(otn)):
               print(str(otn[i])+"|"+str(teor[i])+"|"+str(fotx[i])+"|"+str(ro[i])+"\n")

            fig, ax = plt.subplots()
            ax.plot(ind, num, label="Равномерное")
            ax.legend()

            fig, bx = plt.subplots()
            bx.bar(karm, chast,label="Частота")
            bx.legend()

            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x, otn,width = 0.15, label='Отн.частота', color='red')
            plt.plot(x, ro, label='Плотность', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])

            fig, fx = plt.subplots()
            fx.plot(karms, fotx, label="F(x)")
            print("MO= ",Beta['BJ99'].value,"\n","CKO= ",Beta['BJ100'].value,"\n",
                  "Disp= ",Beta['BJ101'].value,"\n","Assim= ",Beta['BJ102'].value,"\n",
                  "Excess= ",Beta['BJ103'].value,"\n",)
            plt.show()

def handle_command(command1, command2):
    book = load_workbook(filename= "задание2.xlsx", data_only=True)
    num = []
    ind = []
    karm = []
    chast = []
    otn = []
    teor = []
    fotx = []
    ro =[]
    karms = []
    match (command1, command2):
        case "1","1":
            Ravnom = book['1.2.1 Равномерное']

            print("a =",Ravnom['A7'].value,"\n","B =",Ravnom['B7'].value,
                  "\n","Объем выборки K =",Ravnom['C8'].value)
            for i in range(12,133):
                num.append(Ravnom['B' + str(i)].value)
                ind.append(Ravnom['A' + str(i)].value)
            for i in range(29,43):
                chast.append(Ravnom['F' + str(i)].value)
                karm.append(Ravnom['G' + str(i)].value)
                otn.append(Ravnom['H' + str(i)].value)
                teor.append(Ravnom['I' + str(i)].value)
                fotx.append(Ravnom['J' + str(i)].value)
                ro.append(Ravnom['K' + str(i)].value)
                karms.append(i-28)
            
            print("Мин= ",Ravnom['G6'].value,"\n","Макс= ",Ravnom['G7'].value,"\n",
                  "Карман= ",Ravnom['G8'].value,"\n","Число карманов= ",Ravnom['G9'].value,"\n",)

            print("Карман|Частота\n")
            for i in range(len(karm)):
               print(str(karm[i])+"|"+str(chast[i])+ "\n") 
            print("Отн.частота|Теор.|F(x)|Плотность\n")
            for i in range(len(otn)):
               print(str(otn[i])+"|"+str(teor[i])+"|"+str(fotx[i])+"|"+str(ro[i])+"\n")

            fig, ax = plt.subplots()
            ax.plot(ind, num, label="Равномерное")
            ax.legend()

            fig, bx = plt.subplots()
            bx.bar(chast, karm, label="Частота")
            bx.legend()

            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x+0.15, otn,width = 0.15, label='Отн.частота', color='red')
            plt.plot(x, ro, label='Плотность', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])

            fig, fx = plt.subplots()
            fx.plot(karms, fotx, label="F(x)")
            print("MO= ",Ravnom['S44'].value,"\n","CKO= ",Ravnom['S45'].value,"\n",
                  "Disp= ",Ravnom['S46'].value,"\n","Assim= ",Ravnom['S47'].value,"\n",
                  "Excess= ",Ravnom['S48'].value,"\n",)
            plt.show()
        case "2","1":
            Norm = book['1.2.2 Нормальное']

            print("a =",Norm['C5'].value,"\n","B =",Norm['C6'].value,
                  "\n","Объем выборки K =",Norm['C7'].value)
            for i in range(12,130):
                num.append(Norm['B' + str(i)].value)
                ind.append(Norm['A' + str(i)].value)
            for i in range(29,40):
                chast.append(Norm['F' + str(i)].value)
                karm.append(Norm['G' + str(i)].value)
                otn.append(Norm['H' + str(i)].value)
                teor.append(Norm['I' + str(i)].value)
                fotx.append(Norm['J' + str(i)].value)
                ro.append(Norm['K' + str(i)].value)
                karms.append(i-28)
            
            print("Мин= ",Norm['G6'].value,"\n","Макс= ",Norm['G7'].value,"\n",
                  "Карман= ",Norm['G8'].value,"\n","Число карманов= ",Norm['G9'].value,"\n",)

            print("Карман|Частота\n")
            for i in range(len(karm)):
               print(str(karm[i])+"|"+str(chast[i])+ "\n") 
            print("Отн.частота|Теор.|F(x)|Плотность\n")
            for i in range(len(otn)):
               print(str(otn[i])+"|"+str(teor[i])+"|"+str(fotx[i])+"|"+str(ro[i])+"\n")

            fig, ax = plt.subplots()
            ax.plot(ind, num, label="Равномерное")
            ax.legend()

            fig, bx = plt.subplots()
            bx.bar(chast, karm, width=0.3,label="Частота")
            bx.legend()

            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x, otn,width = 0.15, label='Отн.частота', color='red')
            plt.plot(x, ro, label='Плотность', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])

            fig, fx = plt.subplots()
            fx.plot(karms, fotx, label="F(x)")
            print("MO= ",Norm['S44'].value,"\n","CKO= ",Norm['S45'].value,"\n",
                  "Disp= ",Norm['S46'].value,"\n","Assim= ",Norm['S47'].value,"\n",
                  "Excess= ",Norm['S48'].value,"\n",)
            plt.show()
        case "3","1":
            Gama = book['1.2.3 Гамма-распределение']

            print("alpha =",Gama['C5'].value,"\n","beta =",Gama['C6'].value,
                  "\n","Объем выборки K =",Gama['C7'].value)
            for i in range(12,129):
                num.append(Gama['C' + str(i)].value)
                ind.append(Gama['A' + str(i)].value)
            for i in range(29,40):
                chast.append(Gama['F' + str(i)].value)
                karm.append(Gama['G' + str(i)].value)
                otn.append(Gama['H' + str(i)].value)
                teor.append(Gama['I' + str(i)].value)
                fotx.append(Gama['J' + str(i)].value)
                ro.append(Gama['K' + str(i)].value)
                karms.append(i-28)
            
            print("Мин= ",Gama['G6'].value,"\n","Макс= ",Gama['G7'].value,"\n",
                  "Карман= ",Gama['G8'].value,"\n","Число карманов= ",Gama['G9'].value,"\n",)

            print("Карман|Частота\n")
            for i in range(len(karm)):
               print(str(karm[i])+"|"+str(chast[i])+ "\n") 
            print("Отн.частота|Теор.|F(x)|Плотность\n")
            for i in range(len(otn)):
               print(str(otn[i])+"|"+str(teor[i])+"|"+str(fotx[i])+"|"+str(ro[i])+"\n")

            fig, ax = plt.subplots()
            ax.plot(ind, num, label="Равномерное")
            ax.legend()

            fig, bx = plt.subplots()
            bx.bar(chast, karm,label="Частота")
            bx.legend()

            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x, otn,width = 0.15, label='Отн.частота', color='red')
            plt.plot(x, ro, label='Плотность', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])

            fig, fx = plt.subplots()
            fx.plot(karms, fotx, label="F(x)")
            print("MO= ",Gama['S44'].value,"\n","CKO= ",Gama['S45'].value,"\n",
                  "Disp= ",Gama['S46'].value,"\n","Assim= ",Gama['S47'].value,"\n",
                  "Excess= ",Gama['S48'].value,"\n",)
            plt.show()
        case "4","1":
            Beta = book['1.2.4 Бета-распределение']
            optinon = input("Выберите вариант бета распределения\n1.Обычное\n2.X10 выборка\n3.b=a*4\n4.a=1 и b=1\n")
            beta_calcing(Beta,optinon)
        case "1","2":
            a = input("Введите a:\n")
            b = input("Введите b:\n")
            k = input("Введите объем выборки k:\n")
            for i in range(0,int(k)):
               ind.append(i)
            random_ravn = stats.uniform.rvs(loc=int(a),
                                             scale=int(b)-int(a),size=int(k),random_state=2276)
            num = random_ravn.tolist()
            fig, ax = plt.subplots()
            ax.plot(ind, num, label="Равномерное")
            ax.legend()
            
            minimum = int(a)-(int(b)-int(a))
            maximum = int(b)+(int(b)-int(a))
            karman = input("Введите шаг кармана:\n")
            karman_count = input("Введите число карманов:\n")
            karm.append(float(karman))
            for i in range(1,int(karman_count)):
                karm.append(round(karm[i-1] + float(karman), 1))
            chast = [0] * len(karm)
            for value in num:
                closest_idx = min(range(len(karm)), key=lambda i: abs(karm[i]-value))
                chast[closest_idx] += 1
            print("Карман|Частота\n")
            for i in range(len(karm)):
               print(str(karm[i])+"|"+str(chast[i])+ "\n")
            fig, bx = plt.subplots()
            bx.bar(karm, chast, label="Частота")
            bx.legend()

            otn = [0] * len(karm)
            fotx = [0] * len(karm)
            teor = [0] * len(karm)
            for i in range(0,len(karm)):
                otn[i] = chast[i]/int(k)
                fotx[i] = otn[i] + fotx[i-1]
                if otn[i] == 0:
                    teor[i] = 0
                else:
                    teor[i] = 1
            total_teor = sum(teor)
            ro = [0] * len(karm)
            for i in range(0,len(karm)):
                ro[i] = teor[i]/total_teor
            print("Отн.частота|Теор.|F(x)|Плотность\n")
            for i in range(len(otn)):
               print(str(otn[i])+"|"+str(teor[i])+"|"+str(fotx[i])+
                     "|"+str(ro[i])+"\n")
            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x, otn, label='Теор.', color='red')
            plt.plot(x, ro, label='Плотность', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])

            fig, fx = plt.subplots()
            fx.plot(karm, fotx, label="F(x)")
            print("MO= ",np.mean(num),"\n","CKO= ",np.std(num, ddof=1),"\n",
                  "Disp= ",np.var(num, ddof=1),"\n","Assim= ",stats.skew(num),"\n",
                  "Excess= ",stats.kurtosis(num),"\n",)
            plt.show()
        case "2","2":
            mat_oj = input("Введите математическое ожидание:\n")
            st_otk = input("Введите стандартное отклонение:\n")
            k = input("Введите объем выборки k:\n")
            for i in range(0,int(k)):
               ind.append(i)
            random_norm = stats.norm.rvs(loc=int(mat_oj),
                                             scale=float(st_otk),size=int(k),random_state=2276)
            num = random_norm.tolist()
            fig, ax = plt.subplots()
            ax.plot(ind, num, label="Нормальное")
            ax.legend()
            
            minimum = min(num)
            maximum = max(num)
            karman = input("Введите шаг кармана:\n")
            karman_count = input("Введите число карманов:\n")
            karm.append(float(minimum))
            for i in range(1,int(karman_count)):
                karm.append(round(karm[i-1] + float(karman), 1))
            chast = [0] * len(karm)
            for value in num:
                closest_idx = min(range(len(karm)), key=lambda i: abs(karm[i]-value))
                chast[closest_idx] += 1
            print("Карман|Частота\n")
            for i in range(len(karm)):
               print(str(karm[i])+"|"+str(chast[i])+ "\n")
            fig, bx = plt.subplots()
            bx.bar(karm, chast, label="Частота")
            bx.legend()

            otn = [0] * len(karm)
            fotx = [0] * len(karm)
            teor = [0] * len(karm)
            for i in range(0,len(karm)):
                otn[i] = chast[i]/int(k)
                fotx[i] = otn[i]
                teor[i] = stats.norm.pdf(karm[i], loc=int(mat_oj), scale=float(st_otk))
            total_teor = sum(teor)
            ro = [0] * len(karm)
            for i in range(0,len(karm)):
                ro[i] = teor[i]/total_teor
            print("Отн.частота|Теор.|F(x)|Плотность\n")
            for i in range(len(otn)):
               print(str(otn[i])+"|"+str(teor[i])+"|"+str(fotx[i])+
                     "|"+str(ro[i])+"\n")
            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x, otn, label='Теор.', color='red')
            plt.plot(x, ro, label='Плотность', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])

            fig, fx = plt.subplots()
            fx.plot(karm, fotx, label="F(x)")
            print("MO= ",np.mean(num),"\n","CKO= ",np.std(num, ddof=1),"\n",
                  "Disp= ",np.var(num, ddof=1),"\n","Assim= ",stats.skew(num),"\n",
                  "Excess= ",stats.kurtosis(num),"\n",)
            plt.show()
        case "3","2":
            alpha = input("Введите альфа параметр:\n")
            beta = input("Введите бета параметр:\n")
            k = input("Введите объем выборки k:\n")
            for i in range(0,int(k)):
               ind.append(i)
            random_gamma = stats.uniform.rvs(loc = 0,scale=1,size=int(k),random_state=2276)
            rand_p = random_gamma.tolist()
            
            num = [0] * len(ind)
            for i in range(len(rand_p)):
                num[i] = float(stats.gamma.ppf(rand_p[i], a=int(alpha), scale=int(beta)))
            fig, ax = plt.subplots()
            ax.plot(ind, num, label="Гамма")
            ax.legend()
            
            minimum = min(num)
            maximum = max(num)
            karman = input("Введите шаг кармана:\n")
            karman_count = input("Введите число карманов:\n")
            karm.append(round(float(minimum), 1))
            karms.append(1)
            for i in range(1,int(karman_count)):
                karm.append(round(karm[i-1] + float(karman), 1))
                karms.append(i+1)
            chast = [0] * len(karm)
            for value in num:
                closest_idx = min(range(len(karm)), key=lambda i: abs(karm[i]-value))
                chast[closest_idx] += 1
            print("Карман|Частота\n")
            for i in range(len(karm)):
               print(str(karm[i])+"|"+str(chast[i])+ "\n")
            fig, bx = plt.subplots()
            bx.bar(karm, chast, label="Частота")
            bx.legend()

            otn = [0] * len(karm)
            fotx = [0] * len(karm)
            teor = [0] * len(karm)
            for i in range(0,len(karm)):
                otn[i] = chast[i]/int(k)
                fotx[i] = otn[i]
                teor[i] = stats.gamma.pdf(karm[i], a=int(alpha), scale=int(beta))
            total_teor = sum(teor)
            ro = [0] * len(karm)
            for i in range(0,len(karm)):
                ro[i] = teor[i]/total_teor
            print("Отн.частота|Теор.|F(x)|Плотность\n")
            for i in range(len(otn)):
               print(str(otn[i])+"|"+str(teor[i])+"|"+str(fotx[i])+
                     "|"+str(ro[i])+"\n")
            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x, otn, label='Теор.', color='red')
            plt.plot(x, ro, label='Плотность', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])

            fig, fx = plt.subplots()
            fx.plot(karms, fotx, label="F(x)")
            print("MO= ",np.mean(num),"\n","CKO= ",np.std(num, ddof=1),"\n",
                  "Disp= ",np.var(num, ddof=1),"\n","Assim= ",stats.skew(num),"\n",
                  "Excess= ",stats.kurtosis(num),"\n",)
            plt.show()
        case "4","2":
            a = input("Введите a:\n")
            b = input("Введите b:\n")
            k = input("Введите объем выборки k:\n")
            for i in range(0,int(k)):
               ind.append(i)
            random_beta = stats.uniform.rvs(loc = 0,scale=1,size=int(k),random_state=2276)
            rand_p = random_beta.tolist()
            
            num = [0] * len(ind)
            for i in range(len(rand_p)):
                num[i] = float(stats.beta.ppf(rand_p[i], a=int(a), b=int(b)))
            fig, ax = plt.subplots()
            ax.plot(ind, num, label="Гамма")
            ax.legend()
            
            minimum = min(num)
            maximum = max(num)
            karman_count = input("Введите число карманов:\n")
            karman = (maximum-minimum)/int(karman_count)
            karm.append(round(float(minimum), 1))
            karms.append(1)
            for i in range(1,int(karman_count)):
                karm.append(round(karm[i-1] + float(karman), 1))
                karms.append(i+1)
            chast = [0] * len(karm)
            for value in num:
                closest_idx = min(range(len(karm)), key=lambda i: abs(karm[i]-value))
                chast[closest_idx] += 1
            print("Карман|Частота\n")
            for i in range(len(karm)):
               print(str(karm[i])+"|"+str(chast[i])+ "\n")
            fig, bx = plt.subplots()
            bx.bar(karm, chast, label="Частота")
            bx.legend()

            otn = [0] * len(karm)
            fotx = [0] * len(karm)
            teor = [0] * len(karm)
            for i in range(0,len(karm)):
                otn[i] = chast[i]/int(k)
                fotx[i] = otn[i]
                teor[i] = stats.beta.pdf(karm[i], a=int(a), b=int(b))
            total_teor = sum(teor)
            ro = [0] * len(karm)
            for i in range(0,len(karm)):
                ro[i] = teor[i]/total_teor
            print("Отн.частота|Теор.|F(x)|Плотность\n")
            for i in range(len(otn)):
               print(str(otn[i])+"|"+str(teor[i])+"|"+str(fotx[i])+
                     "|"+str(ro[i])+"\n")
            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x, otn, label='Теор.', color='red')
            plt.plot(x, ro, label='Плотность', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])

            fig, fx = plt.subplots()
            fx.plot(karms, fotx, label="F(x)")
            print("MO= ",np.mean(num),"\n","CKO= ",np.std(num, ddof=1),"\n",
                  "Disp= ",np.var(num, ddof=1),"\n","Assim= ",stats.skew(num),"\n",
                  "Excess= ",stats.kurtosis(num),"\n",)
            plt.show()

cont = True
while cont == True:
    choose1 = input("Выберите распределение\n1.Равномерное\n2.Нормальное\n3.Гамма\n4.Бета\n" )
    choose2 = input("Выберите режим\n1.Тестовый\n2.Рабочий\n") 
    handle_command(choose1, choose2)
    ans = input("Продолжить?[Y|n]\n")
    if ans == 'n':
        cont = False
    