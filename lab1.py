summa = 0
average = 0
sigma = 0
mas = []
with open("lab1.txt") as f:
    for line in f:
        mas.append(float(line))
f.close()
mas.sort()
average = sum(mas) / 50
cur_num = 0
for i in mas:
    cur_num += (i - average) ** 2
sigma = (cur_num / 49*50)**(1/2)
k_st = 2.009575234489209
delta = sigma * k_st
print("среднее " + str(average))
print("сигма " + str(sigma))
print("дельта+ " + str(delta))
