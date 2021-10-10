from main import *
import plotly.graph_objects as go

first_array = assess_array(0.25, 20, 20, 100)
second_array = assess_array(0.5, 20, 20, 200)
third_array = assess_array(0.75, 20, 20, 300)
p_10_first = []
p_10_second = []
p_10_third = []
p_1000_first = []
p_1000_second = []
p_1000_third = []
p_10000_first = []
p_10000_second = []
p_10000_third = []
p_mean = []
p_std = []


# Model sznajda dla 10^3 kroków oraz R = 10
def ten_simulations(x, y, z, p, first_10):
    for _ in range(10):
        used_array = assess_array(x, y, z, p)
        for _ in range(10 ** 3):
            index_x, index_y, index_x1, index_y1 = draw_a_pair(used_array)
            index_y, index_y1 = check_index_y(index_y, index_y1, used_array)
            index_x, index_x1 = check_index_x(index_x, index_x1, used_array)
            sznajd_model(index_x, index_y, index_x1, index_y1, used_array)
        first_10.append(np.count_nonzero(used_array == 1))
    return first_10, x


# Liczenie sredniej oraz odchylenia standardowego, a nastepnie wyswietlanie wyniku
def ten_simulations_results(first_10, x, mean_list, std_list):
    mean_first_10 = np.nanmean(first_10)/400
    mean_list.append(mean_first_10)
    std_first_10 = np.nanstd(first_10)/20
    std_list.append(std_first_10)
    print("For 10 simulations and p0 being {0} mean equals {1} and standard deviation equals {2}\n".format(x,mean_first_10, std_first_10))


# Model sznajda dla 10^3 kroków oraz R = 1000
def thousand_simulations(x, y, z, p, first_1000):
    for _ in range(1000):
        used_array = assess_array(x, y, z, p)
        for _ in range(10 ** 3):
            index_x, index_y, index_x1, index_y1 = draw_a_pair(used_array)
            index_y, index_y1 = check_index_y(index_y, index_y1, used_array)
            index_x, index_x1 = check_index_x(index_x, index_x1, used_array)
            sznajd_model(index_x, index_y, index_x1, index_y1, used_array)
        first_1000.append(np.count_nonzero(used_array == 1))
    return first_1000, x


# Liczenie sredniej oraz odchylenia standardowego, a nastepnie wyswietlanie wyniku
def thousand_simulations_results(first_1000, x, mean_list, std_list):
    mean_first_1000 = np.nanmean(first_1000)/400
    mean_list.append(mean_first_1000)
    std_first_1000 = np.nanstd(first_1000)/20
    std_list.append(std_first_1000)
    print("For 1000 simulations and p0 being {0} mean equals {1} and standard deviation equals {2}\n".format(x, mean_first_1000, std_first_1000))


# Model sznajda dla 10^3 kroków oraz R = 10000
def ten_thousand_simulations(x, y, z, p, first_10000):
    for _ in range(10000):
        used_array = assess_array(x, y, z, p)
        for _ in range(10 ** 3):
            index_x, index_y, index_x1, index_y1 = draw_a_pair(used_array)
            index_y, index_y1 = check_index_y(index_y, index_y1, used_array)
            index_x, index_x1 = check_index_x(index_x, index_x1, used_array)
            sznajd_model(index_x, index_y, index_x1, index_y1, used_array)
        first_10000.append(np.count_nonzero(used_array == 1))
    return first_10000, x


# Liczenie sredniej oraz odchylenia standardowego, a nastepnie wyswietlanie wyniku
def ten_thousand_simulations_results(first_10000, x, mean_list, std_list):
    mean_first_10000 = np.nanmean(first_10000)/400
    mean_list.append(mean_first_10000)
    std_first_10000 = np.nanstd(first_10000)/20
    std_list.append(std_first_10000)
    print("For 10000 simulations and p0 being {0} mean equals {1} and standard deviation equals {2}\n".format(x, mean_first_10000, std_first_10000))


# Wszystkie symulacje
ten_simulations(0.25, 20, 20, 100, p_10_first)
ten_simulations_results(p_10_first, 0.25, p_mean, p_std)

ten_simulations(0.5, 20, 20, 200, p_10_second)
ten_simulations_results(p_10_second, 0.5, p_mean, p_std)

ten_simulations(0.75, 20, 20, 300, p_10_third)
ten_simulations_results(p_10_third, 0.75, p_mean, p_std)
print(p_mean, p_std)

thousand_simulations(0.25, 20, 20, 100, p_1000_first)
thousand_simulations_results(p_1000_first, 0.25, p_mean, p_std)

thousand_simulations(0.5, 20, 20, 200, p_1000_second)
thousand_simulations_results(p_1000_second, 0.5, p_mean, p_std)

thousand_simulations(0.75, 20, 20, 300, p_1000_third)
thousand_simulations_results(p_1000_third, 0.75, p_mean, p_std)
print(p_mean, p_std)

ten_thousand_simulations(0.25, 20, 20, 100, p_10000_first)
ten_thousand_simulations_results(p_10000_first, 0.25, p_mean, p_std)

ten_thousand_simulations(0.5, 20, 20, 200, p_10000_second)
ten_thousand_simulations_results(p_10000_second, 0.5, p_mean, p_std)

ten_thousand_simulations(0.75, 20, 20, 300, p_10000_third)
ten_thousand_simulations_results(p_10000_third, 0.75, p_mean, p_std)

#Tabela z wszystkimi danymi
fig = go.Figure(data=[go.Table(
    header=dict(values=["sum of elements", "p0", "percentage", "pAvg", "pStd", "R"],
                line_color='darkslategray',
                fill_color='lightgreen',
                align='center'),
    cells=dict(values=[[400, 400, 400, 400, 400, 400, 400, 400, 400],
                       [100, 100, 100, 200, 200, 200, 300, 300, 300],
                       ["25%", "25%", "25%", "50%", "50%", "50%", "75%", "75%", "75%" ],
                       [p_mean[0], p_mean[3], p_mean[6], p_mean[1], p_mean[4], p_mean[7], p_mean[2], p_mean[5], p_mean[8]],
                       [p_std[0], p_std[3], p_std[6], p_std[1], p_std[4], p_std[7], p_std[2], p_std[5], p_std[8]],
                       [10, 1000, 10000, 10, 1000, 10000, 10, 1000, 10000]],
               line_color='darkslategray',
               fill_color='white',
               align='center')
)])

fig.update_layout(width=1600, height=1000)
fig.show()
