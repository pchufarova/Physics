from math import pi

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
sigma = (cur_num / 49*50)**(1/2) #выборочное среднеквадратичное отклонение

k_st = 2.009575234489209 #коэффициент стьюдента для доверительной вероятности 0.95
delta = sigma * k_st

max_density = 1 / (sigma * (2 * pi)**(1/2)) #максимальная плотность распределения

print("среднее " + str(average))
print("сигма (среднеквадратичное) " + str(sigma))
print("дельта (t) " + str(delta))
