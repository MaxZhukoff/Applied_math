# # aboba
# from scipy.integrate import solve_ivp
# import matplotlib.pyplot as plt
#
# l = 7.23
# u = 4.9
# x = []
# y = []
#
#
# def rhs(s, v):
#     # while v[0] + v[1] + v[2] + v[3] + v[4] + v[5] != 1:
#         kz = (v[1] + 2 * v[2] + 3 * v[3] + 4 * (v[4] + v[5])) / 4
#         kp = (v[3] + 2 * v[2] + 3 * v[1] + 4 * v[0]) / 4
#         x.append(kz)
#         y.append(kp)
#         # x = []
#         # y = []
#
#         # fig, ax = plt.subplots()
#         # ax.axis([0, 1, 0, 1])
#         #
#         # ax.cla()
#         # x.append(kz)
#         # y.append(kp)
#         # print(x)
#
#         # ax.scatter(x, y)
#
#         # print(kz * 100)
#         # print(kp * 100)
#
#         # print("v[0]:", v[0])
#         return [-l * v[0] + u * v[1],
#                 l * v[0] - (u + l) * v[1] + 2 * u * v[2],
#                 l * v[1] - (2 * u + l) * v[2] + 3 * u * v[3],
#                 l * v[2] - (3 * u + l) * v[3] + 4 * u * v[4],
#                 l * v[3] - (4 * u + l) * v[4] + 4 * u * v[5],
#                 l * v[4] - 4 * u * v[5]]
#
#
# # def FindX(s, v):
# #
# #     kz = (v[1] + 2 * v[2] + 3 * v[3] + 4 * (v[4] + v[5])) / 4
# #
# #     x = []
# #
# #     x.append(kz)
# #
# #     return x
# #
# # def FindY(s, v):
# #     # while v[0] + v[1] + v[2] + v[3] + v[4] + v[5] != 1:
# #     kp = (v[3] + 2 * v[2] + 3 * v[1] + 4 * v[0]) / 4
# #
# #     y = []
# #
# #     y.append(kp)
# #
# #     # ax.scatter(x, y)
# #
# #     return y
#
# res = solve_ivp(rhs, (0, 5), [1, 0, 0, 0, 0, 0])
#
# plt.plot(res.t, res.y.T)
# plt.show()
# print(res.y.T)
#
# # x = solve_ivp(rhs, (0, 5), [1, 0, 0, 0, 0, 0])
# #
# # y = solve_ivp(rhs, (0, 5), [1, 0, 0, 0, 0, 0])
#
# # print(x)
#
# # plt.plot(x, y)
# # plt.show()
#
# plt.plot(x)
# plt.plot(y)
# plt.show()
#
# #
# # p0 = 0.229842422510265 - вероятность того, что все машины не работают.
# # p1 = 0.337659329540657- вероятность того, что одна машина занята рубкой
# # p2 = 0.24911098933120301 - вероятность того, что две машины заняты рубкой
# # p3 = 0.12252139641223 - вероятность того, что три машины заняты рубкой
# # p4 = 0.0451953926561439  - вероятность того, что четыре машины заняты рубкой
# # p5 = 0.0166715657604041 - вероятность того,  что четыре машины заняты рубкой, одно бревно находится в очереди.

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

l = 7.23
u = 4.9

x = []
y = []


def rhs(s, v):
    kz = (v[1] + 2 * v[2] + 3 * v[3] + 4 * (v[4] + v[5])) / 4
    kp = (v[3] + 2 * v[2] + 3 * v[1] + 4 * v[0]) / 4

    x.append(kz)
    y.append(kp)

    return [-l * v[0] + u * v[1],
            l * v[0] - (u + l) * v[1] + 2 * u * v[2],
            l * v[1] - (2 * u + l) * v[2] + 3 * u * v[3],
            l * v[2] - (3 * u + l) * v[3] + 4 * u * v[4],
            l * v[3] - (4 * u + l) * v[4] + 4 * u * v[5],
            l * v[4] - 4 * u * v[5]]


res = solve_ivp(rhs, (0, 2), [1, 0, 0, 0, 0, 0])
print(res)

plt.plot(res.t, res.y.T)
print(res.y.T)
plt.show()

plt.plot(x)
plt.plot(y)
plt.show()
