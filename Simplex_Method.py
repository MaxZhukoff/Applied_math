# SIMPLEX_METHOD


# F = 3x1 + 4x2 -> max
maximize_func = [3, 4]

# 4x1 + x2
# x1 - x2
limitation_left_part = [[4, 1],
                        [1, -1]]

# Правая часть уравнения
limitation_right_part = [8, -3]

# Номер икса каждой перемнной
num_of_x = [[1, 2],
            [1, 2]]

# "-1" == "<="
# "0" == "="
# "1" == ">="
limitation_symbol = [-1, 1]

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
print(" -> max\n")

print("Limitations:")
for i in range(len(limitation_left_part)):
    for j in range(len(limitation_left_part[i])):
        print(f'{limitation_left_part[i][j]}x{num_of_x[i][j]}', end='')
        if j != len(limitation_left_part) - 1:
            print(" + ", end='')
    if limitation_symbol[i] == -1:
        print(f" <= {limitation_right_part[i]}")
    elif limitation_symbol[i] == 1:
        print(f" >= {limitation_right_part[i]}")

print()

# Поменять значения числе после "=" с "-" на "+", если такие имеются
for i in range(len(limitation_right_part)):
    if limitation_right_part[i] < 0:
        for j in range(len(limitation_left_part[i])):
            limitation_left_part[i][j] = -limitation_left_part[i][j]
        limitation_right_part[i] = -limitation_right_part[i]
        limitation_symbol[i] = -limitation_symbol[i]
print()

print("Limitations with inverted right part:")
for i in range(len(limitation_left_part)):
    for j in range(len(limitation_left_part[i])):
        print(f'{limitation_left_part[i][j]}x{num_of_x[i][j]}', end='')
        if j != len(limitation_left_part) - 1:
            print(" + ", end='')
    if limitation_symbol[i] == -1:
        print(f" <= {limitation_right_part[i]}")
    elif limitation_symbol[i] == 1:
        print(f" >= {limitation_right_part[i]}")
print()

# Для определения знака нового x
mark_of_x = {}
# Вывести задание в каноническом виде
print("Canonical View:")
for i in range(len(limitation_left_part)):
    for j in range(len(limitation_left_part[i])):
        print(f'{limitation_left_part[i][j]}x{num_of_x[i][j]}', end='')
        if j != len(limitation_left_part) - 1:
            print(" + ", end='')
    if limitation_symbol[i] == -1:
        limitation_left_part[i].append(0)
        additional_x += 1
        print(f" + x{additional_x}", end='')
        mark_of_x[i] = "+"
        num_of_x[i].append(additional_x)
    if limitation_symbol[i] == 1:
        limitation_left_part[i].append(0)
        additional_x += 1
        print(f" - x{additional_x}", end='')
        mark_of_x[i] = "-"
        num_of_x[i].append(additional_x)
    print(f" = {limitation_right_part[i]}")

print(num_of_x[i])
print(mark_of_x)

print()

print("limitation_left_part:", limitation_left_part)
print("num_of_x:", num_of_x)
print("limitation_symbol:", limitation_symbol)

# Выразим базисные переменные и составим таблицу
basis_inequality = []
for i in range(len(limitation_right_part)):
    basis_inequality.append([])
    basis_inequality[i].append(limitation_right_part[i])
    for j in range(len(limitation_left_part[i])):
        if j == len(limitation_left_part):
            break
        basis_inequality[i].append(-limitation_left_part[i][j])
    if mark_of_x[i] == '-':
        for k in range(len(limitation_left_part[i])):
            basis_inequality[i][k] = -basis_inequality[i][k]
print("\nbasis_inequality:", basis_inequality)

#       свободные коэффициенты   x1   x2
# x3              8              -4   -1
# x4              3              +1   -1

