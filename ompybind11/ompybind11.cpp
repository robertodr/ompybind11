#include <functional>
#include <iostream>

#include <omp.h>

#include <pybind11/functional.h>
#include <pybind11/pybind11.h>

namespace py = pybind11;

double eval_func(int rank, std::function<double(double)> func, double x) {
  double out = 0.0;
#pragma omp parallel shared(out)
  {
    int thread_num = omp_get_thread_num();
    if (thread_num == rank) {
      std::cout << "Thread " << thread_num << " working\n";
      out = func(x);
    }
  }
  return out;
}

double calc_pi(int n) {
  double step = 1.0 / n;
  double s = 0.0;

#pragma omp parallel
  {
    double x;
#pragma omp for reduction(+ : s)
    for (int i = 0; i < n; i++) {
      x = (i + 0.5) * step;
      s += 4.0 / (1 + x * x);
    }
  }
  return step * s;
};

PYBIND11_MODULE(ompybind11, m) {
  m.def("eval_func", &eval_func, py::arg("rank"), py::arg("function"),
        py::arg("x"))
      .def("calc_pi", [](int n) {
        return calc_pi(n);
      });
}
