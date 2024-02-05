from math import pi
import matplotlib.pyplot as plt

average = 0
sigma = 0
mas = []
N = 50 #кол-во измерений

with open("lab1.txt") as f:
    for line in f:
        mas.append(float(line)) #добавляем значения измерений в массив
f.close()

mas.sort()
average = sum(mas) / N #среднее арифметическое

cur_num = 0
for i in mas:
    cur_num += (i - average) ** 2
sigma = (cur_num / (N-1))**(1/2) #выборочное среднеквадратичное отклонение

k_st = 2.009575234489209 #коэффициент стьюдента для доверительной вероятности 0.95
delta = sigma * k_st

max_density = 1 / (sigma * (2 * pi)**(1/2)) #максимальная плотность распределения

# print("среднее " + str(average))
# print("сигма (среднеквадратичное) " + str(sigma))
# print("дельта (t) " + str(delta))


# ГИСТОГРАММА

# Ваш массив данныхdata = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
# Построение гистограммы
plt.hist(data, bins=range(min(data), max(data) + 1), edgecolor='black', alpha=0.7)
# Добавление заголовка и меток осейplt.title('Гистограмма данных')
plt.xlabel('Значение')plt.ylabel('Частота')
# Отображение гистограммы
plt.show()
