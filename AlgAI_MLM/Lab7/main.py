from openpyxl import load_workbook
import numpy as np
import matplotlib.pyplot as plt

def handle_command(command1, command2):
    book = load_workbook(filename= "задание7.xlsx", data_only=True)
    ishdan=[]
    Nep  = []
    kosh = []
    w0 = []
    w1 = []
    w2 = []
    k1x = []
    k1y = []
    k2x = []
    k2y = []
    match (command1, command2):
        case "1","1":
            Liner = book['2 переменные']
            for i in range(7,17):
                ishdan.append(Liner['C' + str(i)].value)
            print(f"x1(c1)={ishdan[0]},x2(c1)={ishdan[1]},o(c1)={ishdan[2]},x1(c2)={ishdan[3]},x2(c2)={ishdan[4]},o(c2)={ishdan[5]}"\
                  f",d(c1,c2)={ishdan[6]},v={ishdan[7]},N={ishdan[8]},n={ishdan[9]}")
            for i in range(21,31):
                Nep.append(Liner['AM' + str(i)].value)
                kosh.append(Liner['AN' + str(i)].value)
                w0.append(Liner['AO' + str(i)].value)
                w1.append(Liner['AP' + str(i)].value)
                w2.append(Liner['AQ' + str(i)].value)
            fig, ax = plt.subplots()
            plt.scatter(Nep, kosh)
            plt.plot(Nep, kosh)
            plt.scatter(Nep, w0)
            plt.plot(Nep, w0)
            plt.scatter(Nep, w1)
            plt.plot(Nep, w1)
            plt.scatter(Nep, w2)
            plt.plot(Nep, w2)
            plt.grid(True)
            plt.show()
            for i in range(23,223):
                k1x.append(Liner['N' + str(i)].value)
                k1y.append(Liner['O' + str(i)].value)
                k2x.append(Liner['P' + str(i)].value)
                k2y.append(Liner['Q' + str(i)].value)
            fig, ax = plt.subplots()
            ax.set_xlim(-10, 30)  
            ax.set_ylim(-10, 30)
            plt.scatter(k1x, k1y)
            plt.scatter(k2x, k2y)
            ax.plot([float(Liner['AT34'].value), float(Liner['AV34'].value)], [float(Liner['AU34'].value), float(Liner['AW34'].value)] , label=f'P/resh')
            ax.scatter([float(Liner['AT34'].value), float(Liner['AV34'].value)], [float(Liner['AU34'].value), float(Liner['AW34'].value)] , label=f'P/resh')
            ax.plot([float(Liner['AT35'].value), float(Liner['AV35'].value)], [float(Liner['AU35'].value), float(Liner['AW35'].value)] , label=f'NVED')
            ax.scatter([float(Liner['AT35'].value), float(Liner['AV35'].value)], [float(Liner['AU35'].value), float(Liner['AW35'].value)] , label=f'NVED')
            for i in range(21,31):
                ax.plot([float(Liner['AT21'].value), float(Liner['AV' + str(i)].value)], [float(Liner['AU21'].value), float(Liner['AW' + str(i)].value)] , label=f'эпоха {i - 21}')
                ax.scatter([float(Liner['AT21'].value), float(Liner['AV' + str(i)].value)], [float(Liner['AU21'].value), float(Liner['AW' + str(i)].value)] , label=f'эпоха {i - 21}')
            plt.grid(True)
            plt.show()         
        case "2","1":
            Liner = book['5 переменных']
            w3 = []
            w4 = []
            w5 = []
            for i in range(2,18):
                ishdan.append(Liner['C' + str(i)].value)
            print(f"x1(c1)={ishdan[0]},x2(c1)={ishdan[1]},x3(c1)={ishdan[2]},x4(c1)={ishdan[3]},x5(c1)={ishdan[4]},o(c1)={ishdan[5]}"\
                  f"x1(c2)={ishdan[6]},x2(c2)={ishdan[7]},x3(c2)={ishdan[8]},x4(c2)={ishdan[9]},x5(c2)={ishdan[10]},o(c2)={ishdan[11]}"\
                  f",d(c1,c2)={ishdan[12]},v={ishdan[13]},N={ishdan[14]},n={ishdan[15]}")
            for i in range(23,33):
                Nep.append(Liner['AU' + str(i)].value)
                kosh.append(Liner['AV' + str(i)].value)
                w0.append(Liner['AW' + str(i)].value)
                w1.append(Liner['AX' + str(i)].value)
                w2.append(Liner['AY' + str(i)].value)
                w3.append(Liner['AZ' + str(i)].value)
                w4.append(Liner['BA' + str(i)].value)
                w5.append(Liner['BB' + str(i)].value)
            fig, ax = plt.subplots()
            plt.scatter(Nep, kosh)
            plt.plot(Nep, kosh)
            plt.scatter(Nep, w0)
            plt.plot(Nep, w0)
            plt.scatter(Nep, w1)
            plt.plot(Nep, w1)
            plt.scatter(Nep, w2)
            plt.plot(Nep, w2)
            plt.scatter(Nep, w3)
            plt.plot(Nep, w3)   
            plt.scatter(Nep, w4)    
            plt.plot(Nep, w4)
            plt.scatter(Nep, w5)
            plt.plot(Nep, w5)
            plt.grid(True)
            plt.show()
        case "1","2":
            print("--- Ввод Параметров Обучения и Генерации Данных ---")

            try:
                LEARNING_RATE_V = float(input("Введите Скорость обучения v: "))
                N_EPOCHS = int(input("Введите Количество эпох N: "))
                N_BATCH = int(input("Введите Количество наблюдений в партии n: "))
                N_SAMPLES = int(input("Введите Общее количество наблюдений для выборки: "))
                PROPORTION_C1 = float(input("Введите Пропорцию класса C1: "))

                print("\n--- Параметры Класса C1 ---")
                X1_C1 = float(input("Введите мат. ожидание x1 для C1: "))
                X2_C1 = float(input("Введите мат. ожидание x2 для C1: "))
                O_C1 = float(input("Введите стд. откл. для C1: "))

                print("\n--- Параметры Класса C2 ---")
                X1_C2 = float(input("Введите мат. ожидание x1 для C2: "))
                X2_C2 = float(input("Введите мат. ожидание x2 для C2: "))
                O_C2 = float(input("Введите стд. откл. для C2: "))
            except ValueError:
                print("Ошибка ввода. Убедитесь, что вводите числа.")

            weights = np.array([0.1, 0.1, 0.1])
            print(f"\nНачальные веса: {weights}")

            N_C1 = int(N_SAMPLES * PROPORTION_C1)
            N_C2 = N_SAMPLES - N_C1

            
            r1 = np.random.normal(0, 1, N_SAMPLES)
            r2 = np.random.normal(0, 1, N_SAMPLES)
            o = np.random.uniform(0, 1, N_SAMPLES) 

            X_data = np.zeros((N_SAMPLES, 3)) 
            Y_data = np.zeros(N_SAMPLES)

            X_data[:, 0] = 1

            
            for i in range(N_C1): 
                X_data[i, 1] = r1[i] * O_C1 + X1_C1
                X_data[i, 2] = r2[i] * O_C1 + X2_C1
            for i in range(N_C1, N_SAMPLES):
                X_data[i, 1] = r1[i] * O_C2 + X1_C2
                X_data[i, 2] = r2[i] * O_C2 + X2_C2

            Y_data = np.where(o < PROPORTION_C1, 1, -1)

            indices = np.arange(N_SAMPLES)
            np.random.shuffle(indices)
            X_data = X_data[indices]
            Y_data = Y_data[indices]

            X_C1 = X_data[Y_data == 1]  
            X_C2 = X_data[Y_data == -1] 

            X1_C1_plot = X_C1[:, 1]
            X2_C1_plot = X_C1[:, 2]
            X1_C2_plot = X_C2[:, 1]
            X2_C2_plot = X_C2[:, 2]

            print("\n--- Начало Обучения Перцептрона ---")

            error_history = []
            w0_history = [weights[0]]
            w1_history = [weights[1]]
            w2_history = [weights[2]]

            for epoch in range(N_EPOCHS):
                epoch_errors = 0

                for i in range(0, N_SAMPLES, N_BATCH):

                    X_batch = X_data[i:i + N_BATCH]
                    Y_batch = Y_data[i:i + N_BATCH]

                    linear_combination = np.dot(X_batch, weights)
                    predictions = np.where(linear_combination >= 0, 1, -1) 

                    errors = (Y_batch - predictions) / 2

                    misclassified_mask = (errors != 0)
                    epoch_errors += np.sum(misclassified_mask)

                    X_misclassified = X_batch[misclassified_mask]
                    errors_misclassified = errors[misclassified_mask]

                    if X_misclassified.shape[0] > 0:

                        learning_rate_errors = LEARNING_RATE_V * errors_misclassified[:, np.newaxis]

                        total_delta_w = np.sum(learning_rate_errors * X_misclassified, axis=0)

                        weights = weights + total_delta_w

                error_history.append(epoch_errors)
                w0_history.append(weights[0])
                w1_history.append(weights[1])
                w2_history.append(weights[2])

            print(f"\nОбучение завершено. Финальные веса: w0={weights[0]:.4f}, w1={weights[1]:.4f}, w2={weights[2]:.4f}")

            plt.style.use('seaborn-v0_8-darkgrid')
            fig, ax1 = plt.subplots(figsize=(10, 6))
            fig.suptitle('История Обучения Перцептрона (Ошибки и Веса)')


            ax1.plot(range(N_EPOCHS), error_history, marker='o', linestyle='--')
            ax1.tick_params(axis='y',)


            ax2 = ax1.twinx()
            epochs_w = list(range(N_EPOCHS + 1)) 
            ax2.plot(epochs_w, w0_history, color='blue', label='$w_0$ (Смещение)', linestyle='-')
            ax2.plot(epochs_w, w1_history, color='green', label='$w_1$', linestyle='-')
            ax2.plot(epochs_w, w2_history, color='orange', label='$w_2$', linestyle='-')
            ax2.tick_params(axis='y')
            ax2.legend(loc='lower left')

            plt.show()
            


            plt.figure(figsize=(10, 8))
            plt.title('Разделение Классов и Разделительные Линии (Показана каждая эпоха)')
            plt.xlabel('$x_1$')
            plt.ylabel('$x_2$')

            plt.scatter(X1_C1_plot, X2_C1_plot, color='blue', marker='o', label='Класс C1')
            plt.scatter(X1_C2_plot, X2_C2_plot, color='red', marker='x', label='Класс C2')

            x1_line = np.array([-5, 15]) 

            for i in range(1, N_EPOCHS + 1):
                w0, w1, w2 = w0_history[i], w1_history[i], w2_history[i]

                if w2 != 0:
                    x2_line = -w0/w2 - (w1/w2) * x1_line

                    if i == 1:
                        plt.plot(x1_line, x2_line, color='green', linestyle='--', alpha=0.8, 
                                 linewidth=1, label=f'Линия Эпохи 1')
                    else:
                        plt.plot(x1_line, x2_line, color='gray', linestyle='--', alpha=0.2, 
                                 linewidth=1, label=None)

            w0_final, w1_final, w2_final = weights
            if w2_final != 0:
                x2_line_final = -w0_final/w2_final - (w1_final/w2_final) * x1_line
                plt.plot(x1_line, x2_line_final, color='black', linestyle='-', linewidth=3, 
                         label='Финальная Разделительная Линия')

            plt.legend()
            plt.grid(True)
            plt.xlim(-5, 15)
            plt.ylim(0, 15)
            plt.show()         
        case "2","2":
            
            
            N_FEATURES = 5 
            INITIAL_WEIGHTS = np.array([1.0, 0.1, -5.0, 1.0, 0.1, 7.0]) 


            print("--- Ввод Параметров Обучения и Генерации Данных (5D) ---")

            try:
                LEARNING_RATE_V = float(input("Введите Скорость обучения: "))
                N_EPOCHS = int(input("Введите Количество эпох N: "))
                N_BATCH = int(input("Введите Количество наблюдений в партии n: "))
                N_SAMPLES = int(input("Введите Общее количество наблюдений для выборки: "))
                PROPORTION_C1 = float(input("Введите Пропорцию класса C1: "))

                print(f"\n--- Параметры Класса C1 (5 мат. ожиданий) ---")
                MU_C1 = [float(x) for x in input(f"Введите {N_FEATURES} мат. ожиданий для C1 через пробел (например, 2 2 2 2 2): ").split()]
                O_C1 = float(input("Введите стд. откл. для C1 O: "))

                print(f"\n--- Параметры Класса C2 (5 мат. ожиданий) ---")
                MU_C2 = [float(x) for x in input(f"Введите {N_FEATURES} мат. ожиданий для C2 через пробел : ").split()]
                O_C2 = float(input("Введите стд. откл. для C2 O: "))

                if len(MU_C1) != N_FEATURES or len(MU_C2) != N_FEATURES:
                    raise ValueError("Неверное количество мат. ожиданий. Должно быть 5.")

            except ValueError as e:
                print(f"Ошибка ввода: {e}.")

            weights = INITIAL_WEIGHTS.copy()
            print(f"\nНачальные веса: {weights}")

            N_C1 = int(N_SAMPLES * PROPORTION_C1)
            N_C2 = N_SAMPLES - N_C1
            N_TOTAL_SAMPLES = N_SAMPLES * 2 

            R_COMPONENTS = np.random.normal(0, 1, (N_TOTAL_SAMPLES, N_FEATURES)) 
            O_COMPONENTS = np.random.uniform(0, 1, N_TOTAL_SAMPLES) 

            X_data = np.zeros((N_TOTAL_SAMPLES, N_FEATURES + 1)) 
            Y_data = np.zeros(N_TOTAL_SAMPLES)      

            X_data[:, 0] = 1

            for j in range(N_FEATURES):
                X_data[:N_C1, j + 1] = R_COMPONENTS[:N_C1, j] * O_C1 + MU_C1[j]

            for j in range(N_FEATURES):
                X_data[N_C1:, j + 1] = R_COMPONENTS[N_C1:, j] * O_C2 + MU_C2[j]

            Y_data = np.where(O_COMPONENTS < PROPORTION_C1, 1, -1)

            indices = np.arange(N_TOTAL_SAMPLES)
            np.random.shuffle(indices)
            X_data = X_data[indices]
            Y_data = Y_data[indices]

            print("\n--- Начало Обучения Перцептрона (5D) ---")

            error_history = []
            weights_history = np.zeros((N_EPOCHS + 1, N_FEATURES + 1))
            weights_history[0] = weights.copy() 


            for epoch in range(N_EPOCHS):
                epoch_errors = 0

                for i in range(0, N_TOTAL_SAMPLES, N_BATCH):

                    X_batch = X_data[i:i + N_BATCH]
                    Y_batch = Y_data[i:i + N_BATCH]

                    linear_combination = np.dot(X_batch, weights)
                    predictions = np.where(linear_combination >= 0, 1, -1) 

                    errors = (Y_batch - predictions) / 2

                    misclassified_mask = (errors != 0)
                    epoch_errors += np.sum(misclassified_mask)

                    X_misclassified = X_batch[misclassified_mask]
                    errors_misclassified = errors[misclassified_mask]

                    if X_misclassified.shape[0] > 0:

                        learning_rate_errors = LEARNING_RATE_V * errors_misclassified[:, np.newaxis]

                        total_delta_w = np.sum(learning_rate_errors * X_misclassified, axis=0)

                        weights = weights + total_delta_w

                error_history.append(epoch_errors)
                weights_history[epoch + 1] = weights.copy() 

                if epoch_errors == 0 and epoch > 0:
                    print(f"Конвергенция достигнута на Эпохе {epoch + 1}.")
                    N_EPOCHS = epoch + 1 
                    weights_history = weights_history[:N_EPOCHS + 1]
                    break
                
            print(f"\nОбучение завершено. Финальные веса: W = {weights}")

            epochs_range = np.arange(1, N_EPOCHS + 1)
            weights_history_plot = weights_history[1:] 

            plt.style.use('seaborn-v0_8-darkgrid')
            fig, ax1 = plt.subplots(figsize=(10, 6))
            fig.suptitle('История Обучения Перцептрона (Ошибки и Веса)')

            color = 'tab:red'
            ax1.set_xlabel('Номер Эпохи')
            ax1.set_ylabel('Количество Ошибок в Эпохе', color=color)
            ax1.plot(range(N_EPOCHS), error_history, color=color, marker='o', linestyle='--')
            ax1.tick_params(axis='y', labelcolor=color)

            ax2 = ax1.twinx()
            color = 'tab:blue'
            ax2.set_ylabel('Значения Весов', color=color)
            epochs_w = list(range(N_EPOCHS + 1))
            labels = [f'$w_0$'] + [f'$w_{i}$' for i in range(1, N_FEATURES + 1)]

            for j in range(N_FEATURES + 1):
                ax2.plot(epochs_w, weights_history[:, j], label=labels[j])

            ax2.tick_params(axis='y', labelcolor=color)
            ax2.legend(loc='lower left')

            plt.show()
        

        


cont = True
while cont == True:
    choose1 = input("Выберите вид прогноза СП\n1. 2 переменных\n2.5 переменных\n" )
    choose2 = input("Выберите режим\n1.Тестовый\n2.Рабочий\n") 
    handle_command(choose1, choose2)
    ans = input("Продолжить?[Y|n]\n")
    if ans == 'n':
        cont = False
    