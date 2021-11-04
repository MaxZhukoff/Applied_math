# SIMPLEX_METHOD
import numpy as np
import examples


# Исходное допустимое базисное решение

def simplex_method(maximize_func, limitation_left_part, limitation_right_part,
                   num_of_x, limitation_symbol, max_or_min):
    # Добавляемый x
    additional_x = 0
    for i in range(len((num_of_x))):
        for j in range(len((num_of_x[i]))):
            if additional_x < num_of_x[i][j]:
                additional_x = num_of_x[i][j]

    # Вывести задание
    print("FUNCTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:")
    print("F = ", end='')
    for i in range(len(maximize_func)):
        print(f"{maximize_func[i]}x{i + 1}", end='')
        if i != len(maximize_func) - 1:
            print(" + ", end='')
    print(f" -> {max_or_min}\n")

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
    build_first_simplex_table(limitation_symbol, limitation_left_part, limitation_right_part, mark_of_x,
                              additional_x, num_of_x, maximize_func, max_or_min)


def build_first_simplex_table(limitation_symbol, limitation_left_part, limitation_right_part, mark_of_x,
                              additional_x, num_of_x, maximize_func, max_or_min):
    len_of_maximize_func = len(maximize_func)
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
                # bases.append(f"x{i + 1 + len(maximize_func)}")
                bases.append(i + 1 + len(maximize_func))
            else:
                for j in range(len(simplex_table[i])):
                    # Ищем базисную переменную, как часть, которая участвует в формировании единичной матрицы в заданной строке
                    if simplex_table[i][j] == 1 and sum([r[j] for r in simplex_table]) == 1 and False not in (
                            [r[j] > 0 for r in simplex_table]):
                        # bases[j + 1] = f"x{j + 1}"
                        bases.append(f"x{j + 1}")
                        break
                    # Если у нас нет части единичной матрицы, но сверху и снизу всё ещё 0, то приведём к ней делением всей строки на данный коэффициент
                    elif simplex_table[i][j] != 1 and simplex_table[i][j] != 0 and sum(
                            [r[j] for r in simplex_table]) == 1 and False not in (
                            [r[j] > 0 for r in simplex_table]):
                        simplex_table[i] = simplex_table[i] / simplex_table[i][j]
                        # bases.append(f"x{j + 1}")
                        bases.append(j + 1)
                        break
                    elif simplex_table[i][j] != 0 and j + 1 not in bases:
                        # ???
                        # Поиск базисных переменных через метод исключающего Гаусса (если все предыдущие не сработали)
                        coef = simplex_table[i][j]
                        simplex_table[i] /= coef
                        for k in range(len(simplex_table)):
                            if k == i:
                                continue
                            simplex_table[k] = simplex_table[k] - simplex_table[i] * simplex_table[k][j]
                        # bases.append(f"x{j + 1}")
                        bases.append(j + 1)
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
            # bases.append(f"x{i}")
            bases.append(i)
    flag = 0
    for i in range(len(simplex_table)):
        for j in range(len(simplex_table[i]) - 1):
            if simplex_table[i][j] != 1 and simplex_table[i][j] != 0:
                flag += 1
    print(simplex_table)
    print("\n\n\n")
    if flag == 0 or len(bases) == 0:
        print("No Solution\n\n\n")
        # return "No Solution"
    else:
        # for i in range(len(bases)):
        #     print(bases[i], end=' ')
        #     print(simplex_table[i])
        # return bases, simplex_table

        # Избавляемся от отрицательности в правой части
        min_num_line = 0
        min_num_line_i = 0
        min_num_column = 0
        min_num_column_j = 0
        arr_of_b = np.array([])

        for i in range(len(simplex_table)):
            arr_of_b = np.append(arr_of_b, simplex_table[i][len(simplex_table[i]) - 1])

        if sum(arr_of_b) != sum(abs(-arr_of_b)):
            while sum(arr_of_b) != sum(abs(-arr_of_b)):
                for i in range(len(simplex_table)):
                    if simplex_table[i][len(simplex_table[i]) - 1] < min_num_line:
                        min_num_line = simplex_table[i][len(simplex_table[i]) - 1]
                        min_num_line_i = i
                        continue
                for j in range(len(simplex_table[min_num_line_i]) - 1):
                    if simplex_table[min_num_line_i][j] < min_num_column:
                        min_num_column = simplex_table[min_num_line_i][j]
                        min_num_column_j = j

                arr_of_b[min_num_line_i] /= simplex_table[min_num_line_i][min_num_column_j]
                simplex_table[min_num_line_i] /= simplex_table[min_num_line_i][min_num_column_j]
                bases[min_num_line_i] = min_num_column_j + 1

                for i in range(len(simplex_table)):
                    if i == min_num_line_i:
                        continue
                    simplex_table[i] = simplex_table[i] - simplex_table[min_num_line_i] * simplex_table[i][
                        min_num_column_j]

            last_check = False
            no_solution = False
            for i in range(len(simplex_table)):
                if simplex_table[i][len(simplex_table[i]) - 1] < 0:
                    for j in range(len(simplex_table[i]) - 2):
                        if simplex_table[i][j] < 0:
                            last_check = True
                            break
                    if last_check:
                        print("There is Solution")
                        break
                    else:
                        print(simplex_table)
                        print("No Solution\n\n\n")
                        no_solution = True
                        break

            if not no_solution:
                print("\nSimplex Table with Fixed Right Part: ")
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
                print(simplex_table)
                print(bases)
                print("END\n\n\n")

    # if flag != 0 and len(bases) != 0:
        for i in range(len(simplex_table)):
            for j in range(len(simplex_table[i])):
                if simplex_table[i][j] == -0:
                    simplex_table[i][j] = 0

        # Рассчёт Дельта
        deltas = np.zeros((len(simplex_table[0])), dtype=float)
        for i in (range(len(simplex_table[0]) - len(maximize_func))):
            maximize_func.append(0)
        print("maximize_func: ", maximize_func)
        print("bases: ", bases)

        # maximize_func_minus_one = np.array(maximize_func) - 1
        # for i in range(len(maximize_func_minus_one)):
        #     if maximize_func_minus_one[i] < 0:
        #         maximize_func_minus_one[i] = 0
        # print("maximize_func_minus_one: ", maximize_func_minus_one)

        i = 0
        for b in bases:
            for j in range(len(simplex_table[0])):
                deltas[j] += maximize_func[b - 1] * simplex_table[i][j]
            i += 1
        for i in range(len(maximize_func)):
            deltas[i] -= maximize_func[i]
        print("deltas:", deltas)

        # answers = np.array([[]])
        # for i in range(len(simplex_table) - 1):
        #     print(len(simplex_table) - 1)
        #     answers = np.append(answers, simplex_table[i][len(simplex_table[0]) - 1])
        # answers_dict = np.array([bases, answers])
        #     print(answers)
        #     print(bases)
        plan = False
        while plan != True:
            if max_or_min == "min":
                optimality = "-"
                for i in range(len(deltas) - 1):
                    if deltas[i] > 0:
                        optimality = "+"
                if optimality == "+":
                    print("Plan is not optimal")
                    flag = 0
                    Q = np.array([])
                    max_point = np.max(deltas)
                    index_column, = np.where(deltas == max_point)
                    for i in range(len(simplex_table)):
                        # print(i)
                        # print(simplex_table[i][index])
                        if simplex_table[i][index_column] < 0:
                            flag += 1
                            Q = np.append(Q, "null")
                        else:
                            Q = np.append(Q, simplex_table[i][len(simplex_table[0]) - 1] / simplex_table[i][index_column])
                    if flag == len(simplex_table):
                        print("No Solution")
                    else:
                        min_point = min(Q)
                        index_line, = np.where(Q == min_point)
                        coef = simplex_table[index_line[0]][index_column[0]]
                        simplex_table[index_line[index_line]] /= coef
                        print(simplex_table)
                        for i in range(len(simplex_table)):
                            if i == index_line:
                                continue
                            simplex_table[i] = simplex_table[i] - simplex_table[index_line[0]] * simplex_table[i][index_column]
                        bases[index_line[0]] = index_column[0] + 1

                        deltas.fill(0)
                        print(deltas)
                        # new Deltas
                        i = 0
                        for b in bases:
                            for j in range(len(simplex_table[0])):
                                deltas[j] += maximize_func[b - 1] * simplex_table[i][j]
                            i += 1
                        for i in range(len(maximize_func)):
                            deltas[i] -= maximize_func[i]
                        print("deltas:", deltas)


                        # find_the_answer(simplex_table, bases, maximize_func, max_or_min, deltas)
                else:
                    print("Plan is optimal")
                    plan = True
                    for i in range(1, len_of_maximize_func + 1):
                        if i in bases:
                            print(f"x{i}: {simplex_table[bases.index(i)][len(simplex_table[0]) - 1]}")
                        else:
                            print(f"x{i}: {0}")
                    print("F:", deltas[len(deltas) - 1])

            # while():
            elif max_or_min == "max":
                optimality = "+"
                for i in range(len(deltas) - 1):
                    if deltas[i] < 0:
                        optimality = "-"
                if optimality == "-":
                    print("Plan is not optimal")
                    flag = 0
                    Q = np.array([])
                    min_point = np.min(deltas)
                    index_column, = np.where(deltas == min_point)
                    for i in range(len(simplex_table)):
                        # print(i)
                        # print(simplex_table[i][index])
                        if simplex_table[i][index_column] < 0:
                            flag += 1
                            Q = np.append(Q, "null")
                        else:
                            Q = np.append(Q,
                                          simplex_table[i][len(simplex_table[0]) - 1] / simplex_table[i][index_column])
                    if flag == len(simplex_table):
                        print("No Solution")
                    else:
                        min_point_Q = min(Q)
                        index_line, = np.where(Q == min_point_Q)
                        coef = simplex_table[index_line[0]][index_column[0]]
                        simplex_table[index_line[index_line]] /= coef
                        print(simplex_table)
                        for i in range(len(simplex_table)):
                            if i == index_line:
                                continue
                            simplex_table[i] = simplex_table[i] - simplex_table[index_line[0]] * simplex_table[i][
                                index_column]
                        bases[index_line[0]] = index_column[0] + 1

                        deltas.fill(0)
                        print(deltas)
                        i = 0
                        for b in bases:
                            for j in range(len(simplex_table[0])):
                                deltas[j] += maximize_func[b - 1] * simplex_table[i][j]
                            i += 1
                        for i in range(len(maximize_func)):
                            deltas[i] -= maximize_func[i]
                        print("deltas:", deltas)
                    # find_the_answer(simplex_table, bases, maximize_func, max_or_min, deltas)
                else:
                    print("Plan is optimal")
                    plan = True
                    for i in range(1, len_of_maximize_func + 1):
                        if i in bases:
                            print(f"x{i}: {simplex_table[bases.index(i)][len(simplex_table[0]) - 1]}")
                        else:
                            print(f"x{i}: {0}")
                    print("F:", deltas[len(deltas) - 1])

def find_the_answer(simplex_table, bases, maximize_func, max_or_min, deltas):
    pass

    # print("\nSimplex Table with Fixed Right Part: ")
    # print("   ", end='')
    # for i in range(additional_x + 1):
    #     if (i < len(maximize_func)):
    #         print(maximize_func[i], end='  ')
    #     else:
    #         print(0, end='  ')
    # print("  C")
    # print("   ", end='')
    # for i in range(1, additional_x + 2):
    #     if i < additional_x + 1:
    #         print(f"x{i}", end='  ')
    #     else:
    #         print("b", end=' ')
    # print("  basis")
    # print(simplex_table)
    # print(bases)
    # print("END\n\n\n")


