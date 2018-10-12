
Requires at least CMake 3.11

Configure with:
```
cmake -H. -Bbuild -DENABLE_OPENMP=ON
```
Compile with:
```
cmake --build build
```
Test run with:
```
env OMP_NUM_THREADS=2 OMPYBIND11_MODULE_PATH=$PWD/build/ompybind11 python ompybind11/test.py
```
