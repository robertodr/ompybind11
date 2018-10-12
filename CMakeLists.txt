# define minimum cmake version
cmake_minimum_required(VERSION 3.11 FATAL_ERROR)

# project name and supported language
project(ompybind11 LANGUAGES CXX)

# require C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

option(ENABLE_OPENMP "Use OpenMP parallelization" OFF)

# for testing we will need the python interpreter
find_package(PythonInterp REQUIRED)

add_subdirectory(ompybind11)

# turn on testing
enable_testing()

# define test
add_test(
  NAME
    python_test
  COMMAND
    ${CMAKE_COMMAND} -E env OMPYBIND11_MODULE_PATH=$<TARGET_FILE_DIR:ompybind11>
    ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/ompybind11/test.py
  )
