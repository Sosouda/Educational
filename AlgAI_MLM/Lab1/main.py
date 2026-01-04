from openpyxl import load_workbook
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def handle_command(command1, command2):
    book = load_workbook(filename= "задание1.xlsx", data_only=True)
    num = []
    ind = []
    karm = []
    chast = []
    otn = []
    teor = []
    fotx = []
    match (command1, command2):
        case "1","1":
            Bernul = book['1.1.1 Бернулли']

            print("Вероятность события(1), p =",Bernul['C6'].value,"\n","Объем выборки K =",Bernul['C7'].value)
            for i in range(12,196):
                num.append(Bernul['A' + str(i)].value)
                ind.append(Bernul['B' + str(i)].value)
            
            chast = [Bernul['H29'].value,Bernul['H30'].value]
            karm = [Bernul['G29'].value, Bernul['G30'].value]
            print("Карман|Частота\n"+str(karm[0])+"|"+str(chast[0])+ "\n"+ str(karm[1])+"|"+str(chast[1])+"\n")

            otn = [Bernul['J29'].value, Bernul['J30'].value]
            teor = [Bernul['K29'].value, Bernul['K30'].value]
            fotx = [Bernul['L29'].value, Bernul['L30'].value]
            print("Отн.частота|Теор.|F(x)\n"+str(otn[0])+"|"+str(teor[0])+"|"+str(fotx[0])+ "\n"+ str(otn[1])+"|"+str(teor[1])+"|"+str(fotx[1]))
            fig, ax = plt.subplots()
            ax.plot(num, ind, label="Бернулли")
            ax.legend()

            fig, bx = plt.subplots()
            bx.bar(karm, chast, label="Частота")
            bx.legend()

            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x+0.15, teor,width = 0.15, label='Теор.', color='red')
            plt.bar(x, otn,width = 0.15, label='Отн.частота', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])

            fig, fx = plt.subplots()
            fx.plot(karm, fotx, label="F(x)")

            plt.show()
        case "2","1":
            Binom = book['1.1.2 Биномиальное']

            print("Вероятность (Бернулли)=",Binom['D6'].value,"\n","Число испытаний =",Binom['D7'].value,"\n","Объем выборки K =",Binom['D8'].value)
            
            for i in range(12,120):
                num.append(Binom['A' + str(i)].value)
                ind.append(Binom['B' + str(i)].value)
            for i in range(29,35):
                karm.append(Binom['G' + str(i)].value)
                chast.append(Binom['H' + str(i)].value)
                otn.append(Binom['J' + str(i)].value)
                teor.append(Binom['K' + str(i)].value)
                fotx.append(Binom['L' + str(i)].value)
            
            print("Карман|Частота\n")
            for i in range(len(karm)):
               print(str(karm[i])+"|"+str(chast[i])+ "\n") 
            print("Отн.частота|Теор.|F(x)\n")
            for i in range(len(otn)):
               print(str(otn[i])+"|"+str(teor[i])+"|"+str(fotx[i])+ "\n")

            fig, ax = plt.subplots()
            ax.plot(num, ind, label="Бернулли")
            ax.legend()

            fig, bx = plt.subplots()
            bx.bar(karm, chast, label="Частота")
            bx.legend()

            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x+0.15, teor,width = 0.15, label='Теор.', color='red')
            plt.bar(x, otn,width = 0.15, label='Отн.частота', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])

            fig, fx = plt.subplots()
            fx.plot(karm, fotx, label="F(x)")

            plt.show()
        case "3","1":
            Puass = book['1.1.3 Пуассона']
            print("λ=",Puass['B6'].value,"\n","Объем выборки K =",Puass['D7'].value)
            
            for i in range(12,179):
                num.append(Puass['A' + str(i)].value)
                ind.append(Puass['B' + str(i)].value)
            for i in range(29,39):
                karm.append(Puass['G' + str(i)].value)
                chast.append(Puass['H' + str(i)].value)
                otn.append(Puass['J' + str(i)].value)
                teor.append(Puass['K' + str(i)].value)
                fotx.append(Puass['L' + str(i)].value)

            print("Карман|Частота\n")
            for i in range(len(karm)):
               print(str(karm[i])+"|"+str(chast[i])+ "\n") 
            print("Отн.частота|Теор.|F(x)\n")
            for i in range(len(otn)):
               print(str(otn[i])+"|"+str(teor[i])+"|"+str(fotx[i])+ "\n")
           
            fig, ax = plt.subplots()
            ax.plot(num, ind, label="Бернулли")
            ax.legend() 
           
            fig, bx = plt.subplots()
            bx.bar(karm, chast, label="Частота")
            bx.legend() 
           
            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x+0.15, teor,width = 0.15, label='Теор.', color='red')
            plt.bar(x, otn,width = 0.15, label='Отн.частота', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])   
           
            fig, fx = plt.subplots()
            fx.plot(karm, fotx, label="F(x)")   
            plt.show()
        case "4","1":
            Discr = book['1.1.4 Дискретное']
            print("Объем выборки K =",Discr['C18'].value,"\n")
            IG = []
            print("Xi|Вероятн. P(xi)|Исх.ген.\n")
            for i in range(7,16):
                karm.append(Discr['A' + str(i)].value)
                teor.append(Discr['B' + str(i)].value)
                IG.append(Discr['C' + str(i)].value)
            for i in range(len(IG)):
               print(str(karm[i])+"|"+str(teor[i])+"|"+str(IG[i])+ "\n")  

            for i in range(29,122):
                num.append(Discr['A' + str(i)].value)
                ind.append(Discr['B' + str(i)].value)
            for i in range(29,38):
                chast.append(Discr['H' + str(i)].value)
                otn.append(Discr['J' + str(i)].value)
                fotx.append(Discr['L' + str(i)].value)

            print("Карман|Частота\n")
            for i in range(len(karm)):
               print(str(karm[i])+"|"+str(chast[i])+ "\n") 
            print("Отн.частота|Теор.|F(x)\n")
            for i in range(len(otn)):
               print(str(otn[i])+"|"+str(teor[i])+"|"+str(fotx[i])+ "\n") 

            fig, ax = plt.subplots()
            ax.plot(num, ind, label="Бернулли")
            ax.legend() 
           
            fig, bx = plt.subplots()
            bx.bar(karm, chast, label="Частота")
            bx.legend() 
           
            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x+0.15, teor,width = 0.15, label='Теор.', color='red')
            plt.bar(x, otn,width = 0.15, label='Отн.частота', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])   
           
            fig, fx = plt.subplots()
            fx.plot(karm, fotx, label="F(x)")   
            plt.show()
        case "1","2":
            p = input("Введите вероятность события(0,2 - 0,8)\n")
            k = input("Введите вероятность события(100 - 200)\n")
            for i in range(0,int(k)):
               ind.append(i)
            random_bernoulli = stats.bernoulli.rvs(p=float(p),size=int(k),random_state=2176)
            num = random_bernoulli.tolist()
            fig, ax = plt.subplots()
            ax.plot(ind, num, label="Бернулли")
            ax.legend()

            zeroes = 0
            ones = 0
            karm=[0,1]
            for i in range(len(num)):
                if num[i] == 0:
                  zeroes += 1
                else:
                    ones += 1
            chast.append(zeroes)
            chast.append(ones)
            print("Карман|Частота\n"+str(karm[0])+"|"+str(chast[0])+ "\n"+ str(karm[1])+"|"+str(chast[1])+"\n")
            fig, bx = plt.subplots()
            bx.bar(karm, chast, label="Частота")
            bx.legend()
            otn = [0] * len(karm)
            fotx = [0] * len(karm)
            for i in range(0,len(karm)):
               otn[i] = chast[i]/int(k)
               fotx[i] = otn[i] + fotx[i-1]
            teor.append(float(p))
            teor.append(1-teor[0])
            print("Отн.частота|Теор.|F(x)\n"+str(otn[0])+"|"+str(teor[0])+"|"+str(fotx[0])+ "\n"+ str(otn[1])+"|"+str(teor[1])+"|"+str(fotx[1]))
            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x+0.15, teor,width = 0.15, label='Теор.', color='red')
            plt.bar(x, otn,width = 0.15, label='Отн.частота', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])

            fig, fx = plt.subplots()
            fx.plot(karm, fotx, label="F(x)")
            plt.show()
        case "2","2":
            Binom = book['1.1.2 Биномиальное']
            p = input("Введите вероятность события(0,2 - 0,8)\n")
            k = input("Введите вероятность события(100 - 200)\n")
            n = input("Введите число испытаний (3-8)\n")
            for i in range(0,int(k)):
                ind.append(i)
            random_binom = stats.binom.rvs(n= int(n),p=float(p),size=int(k),random_state=2176)
            num = random_binom.tolist()
            fig, ax = plt.subplots()
            ax.plot(ind, num, label="Биномиальное")
            ax.legend()

            karm, chast = np.unique(num, return_counts=True)
            karm = karm.tolist()
            chast = chast.tolist()
            print("Карман|Частота\n")
            for i in range(len(karm)):
               print(str(karm[i])+"|"+str(chast[i])+ "\n")
            fig, bx = plt.subplots()
            bx.bar(karm, chast, label="Частота")
            bx.legend()

            otn = [0] * len(karm)
            fotx = [0] * len(karm)
            teor = [0] * len(karm)
            for i in range(len(karm)):
               otn[i] = chast[i]/int(k)
               fotx[i] = otn[i] + fotx[i-1]
               teor[i] = stats.binom.pmf(int(karm[i]), int(n), float(p))
            print("Отн.частота|Теор.|F(x)\n")
            for i in range(len(otn)):
               print(str(otn[i])+"|"+str(teor[i])+"|"+str(fotx[i])+ "\n")
            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x+0.15, teor,width = 0.15, label='Теор.', color='red')
            plt.bar(x, otn,width = 0.15, label='Отн.частота', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])

            fig, fx = plt.subplots()
            fx.plot(karm, fotx, label="F(x)")
            plt.show()
        case "3","2":
            Puass = book['1.1.3 Пуассона']
            lmbd = input("Введите λ(2 - 10)\n")
            k = input("Введите вероятность события(100 - 200)\n")
            for i in range(0,int(k)):
                ind.append(i)
            random_pois = stats.poisson.rvs(mu=float(lmbd), size=int(k), random_state=2176)
            num = random_pois.tolist()
            fig, ax = plt.subplots()
            ax.plot(ind, num, label="Пуассона")
            ax.legend()

            karm, chast = np.unique(num, return_counts=True)
            karm = karm.tolist()
            chast = chast.tolist()
            print("Карман|Частота\n")
            for i in range(len(karm)):
               print(str(karm[i])+"|"+str(chast[i])+ "\n")
            fig, bx = plt.subplots()
            bx.bar(karm, chast, label="Частота")
            bx.legend()

            otn = [0] * len(karm)
            fotx = [0] * len(karm)
            teor = [0] * len(karm)
            for i in range(len(karm)):
               otn[i] = chast[i]/int(k)
               fotx[i] = otn[i] + fotx[i-1]
               teor[i] = stats.poisson.pmf(int(karm[i]), int(lmbd))
            print("Отн.частота|Теор.|F(x)\n")
            for i in range(len(otn)):
               print(str(otn[i])+"|"+str(teor[i])+"|"+str(fotx[i])+ "\n")
            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x+0.15, teor,width = 0.15, label='Теор.', color='red')
            plt.bar(x, otn,width = 0.15, label='Отн.частота', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])

            fig, fx = plt.subplots()
            fx.plot(karm, fotx, label="F(x)")
            plt.show()   
        case "4","2":
            Discr = book['1.1.4 Дискретное']
            Xi = input("Введите Xi значения через пробел\n")
            p = input("Введите вероятности для Xi событий через пробел\n")
            k = input("Введите вероятность события(100 - 200)\n")
            karm = [int(x) for x in Xi.split()] 
            teor = [float(x) for x in p.split()]
            stats.discrete_dist = stats.rv_discrete(name='custom', values=(karm, teor))
            for i in range(0,int(k)):
                ind.append(i)
            random_binom = stats.discrete_dist.rvs(size=int(k), random_state=2176)
            num = random_binom.tolist()
            fig, ax = plt.subplots()
            ax.plot(ind, num, label="Дискретное")
            ax.legend()

            karm,chast = np.unique(num, return_counts=True)
            chast = chast.tolist()
            print("Карман|Частота\n")
            for i in range(len(karm)):
               print(str(karm[i])+"|"+str(chast[i])+ "\n")
            fig, bx = plt.subplots()
            bx.bar(karm, chast, label="Частота")
            bx.legend()

            otn = [0] * len(karm)
            fotx = [0] * len(karm)
            for i in range(len(karm)):
               otn[i] = chast[i]/int(k)
               fotx[i] = otn[i] + fotx[i-1]
            print("Отн.частота|Теор.|F(x)\n")
            for i in range(len(otn)):
               print(str(otn[i])+"|"+str(teor[i])+"|"+str(fotx[i])+ "\n")
            fig, cx = plt.subplots()
            x = np.arange(len(karm))
            plt.bar(x+0.15, teor,width = 0.15, label='Теор.', color='red')
            plt.bar(x, otn,width = 0.15, label='Отн.частота', color='blue')
            plt.xlabel('Карман')
            plt.ylabel('Частота')
            plt.xticks(x, [f'{k:.3f}' for k in karm])

            fig, fx = plt.subplots()
            fx.plot(karm, fotx, label="F(x)")
            plt.show()

cont = True
while cont == True:
    choose1 = input("Выберите распределение\n1.Бернулли\n2.Биномиальное\n3.Пуассона\n4.Дискретное\n" )
    choose2 = input("Выберите режим\n1.Тестовый\n2.Рабочий\n") 
    handle_command(choose1, choose2)
    ans = input("Продолжить?[Y|n]\n")
    if ans == 'n':
        cont = False
    