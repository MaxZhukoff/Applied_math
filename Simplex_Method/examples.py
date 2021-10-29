from main import simplex_method
import numpy as np

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

simplex_method(maximize_func, limitation_left_part, limitation_right_part,
                    num_of_x, limitation_symbol)







# F = x1 + 2x2 -> max
maximize_func = [1, 2]

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
                    num_of_x, limitation_symbol)







# F = x1 + 2x2 -> max
maximize_func = [1, 2]

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
                    num_of_x, limitation_symbol)







# F = -6x1 + -1x2 - 4x3 + 5x4 -> min
maximize_func = [-6, -1, -4, 5]

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
                    num_of_x, limitation_symbol)





# F = x1 + 2x2 -> max
maximize_func = [1, 2]

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
                    num_of_x, limitation_symbol)

