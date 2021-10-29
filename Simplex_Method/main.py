# SIMPLEX_METHOD
import numpy as np
import examples

# Исходное допустимое базисное решение!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def simplex_method(maximize_func, limitation_left_part, limitation_right_part,
                   num_of_x, limitation_symbol):
    # Добавляемый x
    additional_x = 0
    for i in range(len((num_of_x))):
        for j in range(len((num_of_x[i]))):
            if additional_x < num_of_x[i][j]:
                additional_x = num_of_x[i][j]

    # Вывести задание
    print("Function:")
    print("F = ", end='')
    for i in range(len(maximize_func)):
        print(f"{maximize_func[i]}x{i + 1}", end='')
        if i != len(maximize_func) - 1:
            print(" + ", end='')
    print(" -> min\n")

    print("Limitations:")
    for i in range(len(limitation_left_part)):
        for j in range(len(limitation_left_part[i])):
            print(f'{limitation_left_part[i][j]}x{num_of_x[i][j]}', end='')
            if j != len(limitation_left_part[i]) - 1:
                print(" + ", end='')
        if limitation_symbol[i] == -1:
            print(f" <= {limitation_right_part[i]}")
        elif limitation_symbol[i] == 1:
            print(f" >= {limitation_right_part[i]}")
        elif limitation_symbol[i] == 0:
            print(f" = {limitation_right_part[i]}")

    # Поменять значения числе после "=" с "-" на "+", если такие имеются
    # for i in range(len(limitation_right_part)):
    #     if limitation_right_part[i] < 0:
    #         for j in range(len(limitation_left_part[i])):
    #             limitation_left_part[i][j] = -limitation_left_part[i][j]
    #         limitation_right_part[i] = -limitation_right_part[i]
    #         limitation_symbol[i] = -limitation_symbol[i]
    # print()

    # Поменять значения ">=" на "<="
    for i in range(len(limitation_right_part)):
        if limitation_symbol[i] == 1:
            for j in range(len(limitation_left_part[i])):
                limitation_left_part[i][j] = -limitation_left_part[i][j]
            limitation_right_part[i] = -limitation_right_part[i]
            limitation_symbol[i] = -limitation_symbol[i]
    print()

    print("Limitations with inverted right part:")
    for i in range(len(limitation_left_part)):
        for j in range(len(limitation_left_part[i])):
            print(f'{limitation_left_part[i][j]}x{num_of_x[i][j]}', end='')
            if j != len(limitation_left_part[i]) - 1:
                print(" + ", end='')
        if limitation_symbol[i] == -1:
            print(f" <= {limitation_right_part[i]}")
        elif limitation_symbol[i] == 1:
            print(f" >= {limitation_right_part[i]}")
        elif limitation_symbol[i] == 0:
            print(f" = {limitation_right_part[i]}")
    print()


    # Для определения знака нового x
    mark_of_x = {}
    # Вывести задание в каноническом виде (по необходимости, добавляем базисные x-ы)
    print("Canonical View:")
    for i in range(len(limitation_left_part)):
        for j in range(len(limitation_left_part[i])):
            print(f'{limitation_left_part[i][j]}x{num_of_x[i][j]}', end='')
            if j != len(limitation_left_part[i]) - 1:
                print(" + ", end='')
        if limitation_symbol[i] == -1:
            limitation_left_part[i].append(1)
            additional_x += 1
            print(f" + x{additional_x}", end='')
            mark_of_x[i] = "+"
            num_of_x[i].append(additional_x)
        if limitation_symbol[i] == 1:
            limitation_left_part[i].append(1)
            additional_x += 1
            print(f" - x{additional_x}", end='')
            mark_of_x[i] = "-"
            num_of_x[i].append(additional_x)
        print(f" = {limitation_right_part[i]}")

    print()

    print("limitation_left_part:", limitation_left_part)
    print("num_of_x:", num_of_x)
    print("limitation_symbol:", limitation_symbol)
    print("mark_of_x:", mark_of_x)

    # Выразим базисные переменные и составим таблицу
    # basis_inequality = []
    # for i in range(len(limitation_right_part)):
    #     basis_inequality.append([])
    #     basis_inequality[i].append(limitation_right_part[i])
    #     for j in range(len(limitation_left_part[i])):
    #         if j == len(limitation_left_part[i]) - 1:
    #             break
    #         basis_inequality[i].append(-limitation_left_part[i][j])
    #     if mark_of_x[i] == '-':
    #         for k in range(len(limitation_left_part[i])):
    #             basis_inequality[i][k] = -basis_inequality[i][k]
    # print("\nbasis_inequality:", basis_inequality, "\nNEXT\n")


    # Симплекс таблица (отдельная функция)
    print("\nFirts-Simplex-Table:")
    print("   ", end='')
    for i in range(additional_x + 1):
        if (i < len(maximize_func)):
            print(maximize_func[i], end='  ')
        else:
            print(0, end='  ')
    print("  C")
    print("   ", end='')
    for i in range(1, additional_x + 2):
        if i < additional_x + 1:
            print(f"x{i}", end='  ')
        else:
            print("b", end=' ')
    print("  basis")

    simplex_table = np.zeros((len(limitation_left_part), additional_x + 1), dtype=float)

    for i in range(len(num_of_x)):
        for j in range(len(num_of_x[i])):
            simplex_table[i][num_of_x[i][j] - 1] = limitation_left_part[i][j]
        simplex_table[i][additional_x] = limitation_right_part[i]

    # def find_bases():
    # Базисные x-ы
    bases = []
    if 0 in limitation_symbol:
        for i in range(len(simplex_table)):
            if limitation_symbol[i] == -1 or limitation_symbol[i] == 1:
                bases.append(f"x{i + 1 + len(maximize_func)}")
            else:
                for j in range(len(simplex_table[i])):
                    # Ищем базисную переменную, как часть, которая участвует в формировании единичной матрицы в заданной строке
                    if simplex_table[i][j] == 1 and sum([r[j] for r in simplex_table]) == 1 and False not in ([r[j] > 0 for r in simplex_table]):
                        bases.append(f"x{j + 1}")
                        break
                    # Если у нас нет части единичной матрицы, но сверху и снизу всё ещё 0, то приведём к ней делением всей строки на данный коэффициент
                    elif simplex_table[i][j] != 1 and simplex_table[i][j] != 0 and sum([r[j] for r in simplex_table]) == 1 and False not in ([r[j] > 0 for r in simplex_table]):
                        simplex_table[i] = simplex_table[i] / simplex_table[i][j]
                        bases.append(f"x{j + 1}")
                        break
                    elif simplex_table[i][j] != 0 and f"x{j + 1}" not in bases:
                        # Поиск базисных переменных через метод исключающего Гаусса (если все предыдущие не сработали)
                        coef = simplex_table[i][j]
                        simplex_table[i] /= coef
                        for k in range(len(simplex_table)):
                            if k == i:
                                continue
                            simplex_table[k] = simplex_table[k] - simplex_table[i] * simplex_table[k][j]
                        bases.append(f"x{j + 1}")
                        break
                    # flag = 0
                    # for p in range(len(simplex_table)):
                    #     for o in range(len(simplex_table[i]) - 1):
                    #         if simplex_table[p][o] != 1 and simplex_table[p][o] != 0:
                    #             flag += 1
                    # if flag == 0:
                    #   print(simplex_table)
                    #   return "No Solution"
    else:
        # Если у нас нет "=" и все базисные переменные уже установлены
        for i in range(len(maximize_func) + 1, additional_x + 1):
            bases.append(f"x{i}")
    flag = 0
    for i in range(len(simplex_table)):
        for j in range(len(simplex_table[i]) - 1):
            if simplex_table[i][j] != 1 and simplex_table[i][j] != 0:
                flag += 1
    print(simplex_table)
    if flag == 0 or len(bases) == 0:
        print("No Solution\n\n\n")
        # return "No Solution"
    else:
        print("bases:", bases)
        # for i in range(len(bases)):
        #     print(bases[i], end=' ')
        #     print(simplex_table[i])
        print("END\n\n\n")
        # return bases, simplex_table

    # Правая часть не может быть отрицательной!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # Поиск ответа в таблице при помощи исключающего метода Гаусса!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


