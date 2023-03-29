import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 2
y_ = np.exp(1) - 2


def function(x, y, delta):
    return 2 * x * (x ** 2 + y * (1 - delta))


def function_2(x):
    return np.exp(x ** 2) - x ** 2 - 1


def method(left, right, y_0, func, d, epsilon):
    def solve(section):
        mas_x = []
        mas_y = []
        value_x = left
        value_y = y_0
        mas_y.insert(0, value_y)
        mas_x.insert(0, value_x)
        step = abs(right - left) / section
        while value_x < right:
            f = func(value_x, value_y, d)
            value_y = value_y + step * (
                    f + func(value_x + step, value_y + step * f,
                                                     d)) / 2
            value_x += step
            mas_y.insert(0, value_y)
            mas_x.insert(0, value_x)
        mas_y.insert(0, value_y)
        mas_x.insert(0, value_x)
        return mas_x, mas_y

    result_solve_2 = solve(2)
    error_summa = 10
    section_1 = 4
    mas_error = []
    mas_section = [2]
    while error_summa > epsilon:
        mas_y_1 = result_solve_2[1]
        result_solve_2 = solve(section_1)
        mas_y_2 = result_solve_2[1]
        error_summa = 0
        for j in range(1, int((section_1 / 2)) + 1):
            error_summa_m = abs((mas_y_2[2 * j] - mas_y_1[j])/3)
            if error_summa_m > error_summa:
                error_summa = error_summa_m
        mas_error.insert(0, error_summa)
        mas_section.insert(0, section_1)
        section_1 *= 2
    mas_x_final = result_solve_2[0]
    mas_y_final = result_solve_2[1]
    mas_error.reverse()
    mas_section.reverse()
    return mas_x_final, mas_y_final, error_summa, section_1 / 2, mas_error, mas_section


check_1_1 = method(a, b, y_, function, 0, 1)
check_1_2 = method(a, b, y_, function, 0, 0.5)
check_1_3 = method(a, b, y_, function, 0, 1e-1)


plt.figure(1)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('График №1')
x_real = np.linspace(a, b, 1000)
y_real = function_2(x_real)
plt.plot(x_real, y_real, label='real')
plt.plot(check_1_3[0], check_1_3[1], '--', label='tol = 1e-3')
plt.legend()



plt.figure(2)
plt.grid()
plt.xlabel('section')
plt.ylabel('error')
plt.title('График №2')
plt.plot(check_1_3[5][1:], check_1_3[4], '--', label='tol = 1e-3')
plt.legend()

def graph_3_4():
    tol = 1e-1
    mas_tol = []
    mas_error = []
    mas_sec = []
    for j in range(4):
        mas_tol.insert(0, tol)
        result = method(a, b, y_, function, 0, tol)
        mas_error.insert(0, result[2])
        mas_sec.insert(0, result[3])
        tol = round(0.1*tol, 4)
    mas_tol.reverse()
    mas_error.reverse()
    mas_sec.reverse()
    return mas_tol, mas_error, mas_sec

check_2 = graph_3_4()

plt.figure(3)
plt.grid()
plt.yscale('log')
plt.xscale('log')
plt.xlabel('tolerance')
plt.ylabel('error')
plt.title('Graph №3')
plt.plot(check_2[0], check_2[0], label='exact error')
plt.plot(check_2[0], check_2[1], label='experimental error')
plt.legend()

plt.figure(4)
plt.yscale('log')
plt.grid()
plt.xscale('log')
plt.xlabel('tolerance')
plt.ylabel('section')
plt.title('Graph №4')
plt.plot(check_2[0], check_2[2])
plt.legend()

def graph_5(tol):
    delta = 0.0
    mas_delta = []
    mas_error = []
    for j in range(5):
        mas_delta.insert(0, delta * 100)
        result = method(a, b, y_ * (1 - delta), function, 0, tol)
        mas_error.insert(0, result[2])
        delta += 0.1
    mas_delta.reverse()
    mas_error.reverse()
    return mas_delta, mas_error


check_3_1 = graph_5(1e-1)
check_3_2 = graph_5(1e-3)

plt.figure(5)
plt.suptitle('График №5')
plt.subplot(1, 2, 1)
plt.grid()
plt.plot(check_3_1[0], check_3_1[1], label='tol = 1e-1')
plt.xlabel('start error, %')
plt.ylabel('absolute error')
plt.legend()
plt.subplot(1, 2, 2)
plt.grid()
plt.plot(check_3_2[0], check_3_2[1], 'r', label='tol = 1e-3')
plt.xlabel('start error, %')
plt.legend()


def graph_6(tol):
    delta_ = 0.0
    mas_delta = []
    mas_error = []
    for j in range(5):
        mas_delta.insert(0, delta_ * 100)
        result = method(a, b, y_, function, delta_, tol)
        mas_error.insert(0, result[2])
        delta_ += 0.1
    mas_error.reverse()
    return mas_delta, mas_error


check_6_1 = graph_6(1e-1)
check_6_2 = graph_6(1e-2)

plt.figure(6)
plt.suptitle('Graph №6')
plt.subplot(1, 2, 1)
plt.grid()
plt.plot(check_6_1[0], check_6_1[1], label='tol = 1e-1')
plt.xlabel('error in equation, %')
plt.ylabel('absolute error')
plt.legend()
plt.subplot(1, 2, 2)
plt.grid()
plt.plot(check_6_2[0], check_6_2[1], 'r', label='tol = 1e-3')
plt.xlabel('error in equation, %')
plt.legend()


def graph_7(tol):
    delta = 0.0
    mas_delta = []
    mas_error = []
    mas_y_real = method(a, b, y_, function, 0, tol)[1]
    for j in range(5):
        mas_delta.insert(0, delta * 100)
        mas_y_approx = method(a, b, y_ * (1 - delta), function, 0, tol)[1]
        length = len(mas_y_approx)
        result = np.zeros((1, length))[0]
        for k in range(length):
            result[k] = abs((mas_y_real[k] - mas_y_approx[k]) / mas_y_real[k])
        mas_error.insert(0, max(result) * 100)
        delta += 0.1
    mas_delta.reverse()
    mas_error.reverse()
    return mas_delta, mas_error

check_7_1 = graph_7(1e-1)
check_7_2 = graph_7(1e-3)


plt.figure(7)
plt.suptitle('Graph №7')
plt.subplot(1, 2, 1)
plt.grid()
plt.plot(check_7_1[0], check_7_1[1], label='tol = 1e-1')
plt.xlabel('start error, %')
plt.ylabel('relative error, %')
plt.legend()
plt.subplot(1, 2, 2)
plt.grid()
plt.plot(check_7_2[0], check_7_2[1], 'r', label='tol = 1e-3')
plt.xlabel('start error, %')
plt.legend()


def graph_8(tol):
    delta_ = 0.0
    mas_delta = []
    mas_error = []
    mas_y_real = method(a, b, y_, function, 0, tol)[1]
    for j in range(5):
        mas_delta.insert(0, delta_ * 100)
        mas_y_approx = method(a, b, y_, function, delta_, tol)[1]
        length = len(mas_y_approx)
        result = np.zeros((1, length))[0]
        for k in range(length):
            result[k] = abs((mas_y_real[k] - mas_y_approx[k]) / mas_y_real[k])
        mas_error.insert(0, max(result) * 100)
        delta_ += 0.1
    return mas_delta, mas_error


check_8_1 = graph_8(1e-1)
check_8_2 = graph_8(1e-2)

plt.figure(8)
plt.suptitle('Graph №8')
plt.subplot(1, 2, 1)
plt.grid()
plt.plot(check_8_1[0], check_8_1[1], label='tol = 1e-1')
plt.xlabel('error in equation, %')
plt.ylabel('relative error, %')
plt.legend()
plt.subplot(1, 2, 2)
plt.grid()
plt.plot(check_8_2[0], check_8_2[1], 'r', label='tol = 1e-3')
plt.xlabel('error in equation, %')
plt.legend()

def graph_9():
    rel_error = []
    res = method(a, b, y_, function, 0, 1e-2)
    error = res[4]
    length = len(error)
    for j in range(length):
        rel_error.insert(0, error[0] / error[j])
    rel_error.reverse()
    rel_error.pop(1)
    return rel_error


res_graph_9 = graph_9()
plt.figure(9)
plt.grid()
plt.xlabel('x')
plt.ylabel('уменьшение абсолютной погрешности')
plt.title('Graph №9')
x_2 = np.linspace(0, 10, 11)
y_2 = 2 ** x_2
plt.plot(x_2, res_graph_9, label='method')
plt.plot(x_2, y_2, label='2**x')
plt.legend()
plt.show()
