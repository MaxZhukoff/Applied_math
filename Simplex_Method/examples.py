from main import simplex_method
import numpy as np

# F = 3x1 + 4x2 -> min
maximize_func = [3, 4]

max_or_min = "min"

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

simplex_method(maximize_func, limitation_left_part, limitation_right_part,
                    num_of_x, limitation_symbol, max_or_min)








# F = x1 + 2x2 -> min
maximize_func = [1, 2]

max_or_min = "min"

# -x1 + 2x2
# x1 + x2
# x1 - x2
# x2
limitation_left_part = [[-1, 2],
                        [1, 1],
                        [1, -1],
                        [1]]

# Правая часть уравнения
limitation_right_part = [2, 4, 2, 6]

# Номер икса каждой перемнной
num_of_x = [[1, 2],
            [1, 2],
            [1, 2],
            [2]]

# "-1" == "<="
# "0" == "="
# "1" == ">="
limitation_symbol = [0, 0, 0, 0]

# Нет решения
simplex_method(maximize_func, limitation_left_part, limitation_right_part,
                    num_of_x, limitation_symbol, max_or_min)







# F = -6x1 + -1x2 - 4x3 + 5x4 -> min
maximize_func = [-6, -1, -4, 5]

max_or_min = "min"

# 3x1 + 1x2 - 1x3 + x4
# 5x1 + x2 + x3 - x4

limitation_left_part = [[3, 1, -1, 1],
                        [5, 1, 1, -1]]

# Правая часть уравнения
limitation_right_part = [4, 4]

# Номер икса каждой перемнной
num_of_x = [[1, 2, 3, 4],
            [1, 2, 3, 4]]

# "-1" == "<="
# "0" == "="
# "1" == ">="
limitation_symbol = [0, 0]

simplex_method(maximize_func, limitation_left_part, limitation_right_part,
                    num_of_x, limitation_symbol, max_or_min)







# F = x1 + 2x2 -> min
maximize_func = [1, 2]

max_or_min = "min"

# -x1 + 2x2
# x1 + x2
# x1 - x2
# x2
limitation_left_part = [[-1, 2],
                        [1, 1],
                        [1, -1],
                        [1]]

# Правая часть уравнения
limitation_right_part = [2, 4, 2, 6]

# Номер икса каждой перемнной
num_of_x = [[1, 2],
            [1, 2],
            [1, 2],
            [2]]

# "-1" == "<="
# "0" == "="
# "1" == ">="
limitation_symbol = [1, 1, -1, 0]
simplex_method(maximize_func, limitation_left_part, limitation_right_part,
                    num_of_x, limitation_symbol, max_or_min)









# F = x1 + 2x2 -> min
maximize_func = [1, 2]

max_or_min = "min"

# -x1 + 2x2
# x1 + x2
# x1 - x2
# x2
limitation_left_part = [[-1, 2],
                        [1, 1],
                        [1, -1],
                        [1]]

# Правая часть уравнения
limitation_right_part = [2, 4, 2, 6]

# Номер икса каждой перемнной
num_of_x = [[1, 2],
            [1, 2],
            [1, 2],
            [2]]

# "-1" == "<="
# "0" == "="
# "1" == ">="
limitation_symbol = [1, 1, -1, -1]
simplex_method(maximize_func, limitation_left_part, limitation_right_part,
                    num_of_x, limitation_symbol, max_or_min)



# Плохие примеры...
# F = 1x1 + 1x2 -> min
maximize_func = [1, 1]

max_or_min = "min"

# 3x1 + 5x2
# 4x1 + -3x2
# 1x1 + -3x2
limitation_left_part = [[3, 5],
                        [4, -3],
                        [1, -3]]

# Правая часть уравнения
limitation_right_part = [30, 12, 6]

# Номер икса каждой перемнной
num_of_x = [[1, 2],
            [1, 2],
            [1, 2]]

# "-1" == "<="
# "0" == "="
# "1" == ">="
limitation_symbol = [-1, -1, 1]
simplex_method(maximize_func, limitation_left_part, limitation_right_part,
                    num_of_x, limitation_symbol, max_or_min)


# F = 1x1 + 1x2 -> min
maximize_func = [1, 2]

max_or_min = "min"

# 3x1 + 5x2
# 4x1 + -3x2
# 1x1 + -3x2
limitation_left_part = [[3, 5],
                        [4, -3],
                        [1, -3]]

# Правая часть уравнения
limitation_right_part = [6, 8, 2]

# Номер икса каждой перемнной
num_of_x = [[1, 2],
            [1, 2],
            [1, 2]]

# "-1" == "<="
# "0" == "="
# "1" == ">="
limitation_symbol = [-1, 1, -1]
simplex_method(maximize_func, limitation_left_part, limitation_right_part,
                    num_of_x, limitation_symbol, max_or_min)


#
# def aboba(ab, bo):
#     return ab, bo
#
# a = 5
# b = 10
# # aboba(a, b)
# print(aboba(a, b))
