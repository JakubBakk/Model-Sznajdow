from main import *
import matplotlib.pyplot as plt

# Tablica 100x100 z p0 = 5000
second_array = assess_array(0.35, 100, 100, 3500)
t_count = []
p_count = []
p_percent = []

# Model sznajda dla 10^5 krokow
for t in range(10**5):
    index_x, index_y, index_x1, index_y1 = draw_a_pair(second_array)
    index_y, index_y1 = check_index_y(index_y, index_y1, second_array)
    index_x, index_x1 = check_index_x(index_x, index_x1, second_array)
    sznajd_model(index_x, index_y, index_x1, index_y1, second_array)
    t = t+1
    t_count.append(t)
    p_count.append(np.count_nonzero(second_array == 1))

for i in range(len(p_count)):
    p_percent.append((p_count[i]/(t-1))*1000)


# print(t_count, p_count, p_percent)


# Wykres funkcji
plt.plot(t_count, p_percent)
plt.xlabel('Krok czasowy')
plt.ylabel("% odpowiedzi na 'Tak' ")
plt.show()
