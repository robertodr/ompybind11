include(FetchContent)

FetchContent_Declare(
  pybind11_sources
  GIT_REPOSITORY https://github.com/pybind/pybind11.git
  GIT_TAG        v2.2
)

FetchContent_GetProperties(pybind11_sources)

if(NOT pybind11_sources_POPULATED)
  FetchContent_Populate(pybind11_sources)

  add_subdirectory(
    ${pybind11_sources_SOURCE_DIR}
    ${pybind11_sources_BINARY_DIR}
    )
endif()

if(ENABLE_OPENMP)
  find_package(OpenMP REQUIRED)
endif()

# create python module
add_library(ompybind11
  MODULE
    ompybind11.cpp
  )

target_link_libraries(ompybind11
  PUBLIC
    pybind11::module
    $<$<AND:$<BOOL:ENABLE_OPENMP>,$<BOOL:OpenMP_FOUND>>:OpenMP::OpenMP_CXX>
  )

set_target_properties(ompybind11
  PROPERTIES
    PREFIX "${PYTHON_MODULE_PREFIX}"
    SUFFIX "${PYTHON_MODULE_EXTENSION}"
  )
