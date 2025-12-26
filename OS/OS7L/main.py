import pandas as pd
import matplotlib.pyplot as plt

files = [
    "fifo_tmax_50.csv",
    "fifo_tmax_500.csv",
    "fifo_tmax_5000.csv",
    "fscan_tmax_50.csv",
    "fscan_tmax_500.csv",
    "fscan_tmax_5000.csv",
]

fig, axes = plt.subplots(3, 2, figsize=(16, 8))
axes = axes.ravel()

for ax, fname in zip(axes, files):
    df = pd.read_csv(fname)
    values = df.iloc[:, 0]           # столбец с временами

    # гистограмма как на примере
    ax.hist(
        values,
        bins=20,                      # можно подобрать под каждый файл
        color="skyblue",
        edgecolor="black"
    )
    ax.set_title(fname)
    ax.set_xlabel("Время обслуживания (мс)")
    ax.set_ylabel("Количество запросов")

plt.tight_layout()
plt.show()