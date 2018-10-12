import os
import sys

sys.path.append(os.getenv('OMPYBIND11_MODULE_PATH'))
import ompybind11  # isort:skip

done = ompybind11.do(function=(lambda x: x + 40.0), x=2.0)
print('ompybind11.do(function=(lambda x: x + 40.0), x=2.0) returned {}'.format(
    done))

# This reproduces 1525
#from concurrent.futures import ThreadPoolExecutor # isort:skip
#with ThreadPoolExecutor(max_workers=2) as e:
#    e.submit(ompybind11.do, lambda x: x + 40.0, 2.0)
#    e.submit(ompybind11.do, lambda x: x + 40.0, 2.0)


def f(x):
    return x * x


x = 2.0

pi = ompybind11.calc_pi(100)
print('pi is {}'.format(pi))

foo = ompybind11.eval_func(rank=0, function=f, x=x)
print('Output of eval_func {}\n'.format(foo))

bar = ompybind11.eval_func(rank=1, function=f, x=x)
print('Output of eval_func {}\n'.format(bar))
