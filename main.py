import numpy as np
import random

t = 0


# x = prawdopodobienstwo wylosowania 1, y,z=wymiary tablicy, p= ile elementow ma byc 1(faktyczne prawdopodobienstwo)
def assess_array(x, y, z, p):
    array_1 = np.array([])
    while np.count_nonzero(array_1 == 1) != p:
        array_1 = np.random.binomial(1, x, (y, z))
    return array_1


# Losowanie dowolnej pary z tablicy
def draw_a_pair(used_array):
    x = random.randint(0, len(used_array)-1)
    y = random.randint(0, len(used_array)-1)
    random_element = [x, y]
    if random.choice(random_element) == x:
        x1 = x
        random_element = [y - 1, y + 1]
        y1 = random.choice(random_element)
    else:
        y1 = y
        random_element = [x - 1, x + 1]
        x1 = random.choice(random_element)
    return x, y, x1, y1


# Sprawdzenie czy któraś z par nie wychodzi poza tablicę poziomo
def check_index_x(x, x1, used_array):
    if x1 < 0:
        x1 = x + 1
    elif x1 > len(used_array)-1:
        x1 = x - 1
    return x, x1


# Sprawdzenie czy któraś z par nie wychodzi poza tablicę pionowo
def check_index_y(y, y1, used_array):
    if y1 < 0:
        y1 = y + 1
    elif y1 > len(used_array)-1:
        y1 = y - 1
    return y, y1


# Model sznajda dla pary poziomej
def sznajd_horizontal(x, y, y1, used_array, v):
    if x - 1 < 0:
        if y + 1 > len(used_array)-1:
            used_array[x + 1, y - 1] = v
            used_array[x + 1, y] = v
            used_array[x, y - 2] = v
        elif y - 2 < 0:
            used_array[x + 1, y - 1] = v
            used_array[x + 1, y] = v
            used_array[x, y + 1] = v
        else:
            used_array[x, y - 2] = v
            used_array[x, y + 1] = v
            used_array[x + 1, y - 1] = v
            used_array[x + 1, y] = v
    elif x + 1 > len(used_array)-1:
        if y + 1 > len(used_array)-1:
            used_array[x - 1, y - 1] = v
            used_array[x - 1, y] = v
            used_array[x, y - 2] = v
        elif y - 2 < 0:
            used_array[x - 1, y - 1] = v
            used_array[x - 1, y] = v
            used_array[x, y + 1] = v
        else:
            used_array[x, y - 2] = v
            used_array[x, y + 1] = v
            used_array[x - 1, y - 1] = v
            used_array[x - 1, y] = v
    else:
        used_array[x - 1, y - 1] = v
        used_array[x - 1, y] = v
        used_array[x, y1 - 1] = v
        used_array[x, y1 + 1] = v
        used_array[x + 1, y - 1] = v
        used_array[x + 1, y] = v


# Model sznajda dla pary pionowej
def sznajd_vertical(x, y, x1, used_array, v):
    if y - 1 < 0:
        if x + 1 > len(used_array)-1:
            used_array[x - 1, y + 1] = v
            used_array[x, y + 1] = v
            used_array[x - 2, y] = v
        elif x - 2 < 0:
            used_array[x - 1, y + 1] = v
            used_array[x, y + 1] = v
            used_array[x + 1, y] = v
        else:
            used_array[x - 1, y + 1] = v
            used_array[x, y + 1] = v
            used_array[x - 2, y] = v
            used_array[x + 1, y] = v

    elif y + 1 > len(used_array)-1:
        if x + 1 > len(used_array)-1:
            used_array[x - 1, y - 1] = v
            used_array[x, y - 1] = v
            used_array[x - 2, y] = v
        elif x - 2 < 0:
            used_array[x - 1, y - 1] = v
            used_array[x, y - 1] = v
            used_array[x + 1, y] = v
        else:
            used_array[x - 1, y - 1] = v
            used_array[x, y - 1] = v
            used_array[x - 2, y] = v
            used_array[x + 1, y] = v
    else:
        used_array[x - 1, y - 1] = v
        used_array[x, y + 1] = v
        used_array[x1 - 1, y] = v
        used_array[x1 + 1, y] = v
        used_array[x - 1, y + 1] = v
        used_array[x, y + 1] = v


# Właściwy model Sznajda
def sznajd_model(x, y, x1, y1, used_array):
    element1 = used_array[x, y]
    element2 = used_array[x1, y1]
    value = element1
    if element1 == element2 and x == x1:
        if y > y1:
            sznajd_horizontal(x, y, x1, used_array, value)
        elif y1 > y:
            y = y + 1
            sznajd_horizontal(x, y, x1, used_array, value)
    elif element1 == element2 and y == y1:
        if x > x1:
            sznajd_vertical(x, y, y1, used_array, value)
        elif x1 > x:
            x = x + 1
            sznajd_vertical(x, y, y1, used_array, value)
    return 0


# Wypisywanie wyników do konsoli
def print_results(x, y, x1, y1, used_array):
    first_cord = (x, y)
    second_cord = (x1, y1)
    print("\nResult of " + str(t+1) + " draw:")
    print("Pair's cords:", first_cord, second_cord)
    print("Pair's values:", used_array[x, y], used_array[x1, y1])
    print("'Yes' answers:", np.count_nonzero(used_array == 1))
    print("\n", used_array)


# Zapisywanie wyników do pliku zewnętrznego
def write_results(x, y, x1, y1, used_array):
    with open("Pierwsze zadanie.txt", "a") as f:
        first_cord = (x+1, y+1)
        second_cord = (x1+1, y1+1)
        f.write("\nResult of " + str(t + 1) + " draw:")
        f.write("\nPair's cords:({0},{1})".format(first_cord, second_cord))
        f.write("\nPair's values:({0},{1})".format(used_array[x, y], used_array[x1, y1]))
        f.write("\n'Yes' answers:{0}".format(np.count_nonzero(used_array == 1)))
        f.write("\n{0}".format(used_array))


# Main
if __name__ == "__main__":
    #Tablica 10x10 z p0 = 50
    initial_array = assess_array(0.5, 10, 10, 50)
    print(initial_array)
    for t in range(10):
        index_x, index_y, index_x1, index_y1 = draw_a_pair(initial_array)
        index_y, index_y1 = check_index_y(index_y, index_y1, initial_array)
        index_x, index_x1 = check_index_x(index_x, index_x1, initial_array)
        sznajd_model(index_x, index_y, index_x1, index_y1, initial_array)
        print_results(index_x, index_y, index_x1, index_y1, initial_array)
        write_results(index_x, index_y, index_x1, index_y1, initial_array)

