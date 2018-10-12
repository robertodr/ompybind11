import os
import sys

sys.path.append(os.getenv('OMPYBIND11_MODULE_PATH'))
import ompybind11 # isort:skip


def f(x):
    return x*x

x = 2.0

pi = ompybind11.calc_pi(100)
print('pi is {}'.format(pi))

foo = ompybind11.eval_func(0, f, x)
print('Output of eval_func {}\n'.format(foo))

bar = ompybind11.eval_func(1, f, x)
print('Output of eval_func {}\n'.format(bar))
