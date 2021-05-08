cmake_minimum_required(VERSION 3.20)
project(elf)

find_package(pybind11 CONFIG REQUIRED)
find_package(cppzmq CONFIG REQUIRED)

# Source files

set(ELF_SOURCES
    Pybind.cpp
    concurrency/Counter.cpp
    logging/IndexedLoggerFactory.cpp
    logging/Levels.cpp
    logging/Pybind.cpp
    options/OptionMap.cpp
    options/OptionSpec.cpp
    options/Pybind.cpp
)

set(ELF_TEST_SOURCES
    options/OptionMapTest.cpp
    options/OptionSpecTest.cpp
)

# Main ELF library

add_library(elf ${ELF_SOURCES})
# target_compile_definitions(elf PUBLIC
#     GIT_COMMIT_HASH=${GIT_COMMIT_HASH}
#     GIT_STAGED=${GIT_STAGED_STRING}
# )

target_link_libraries(elf PUBLIC
    #${Boost_LIBRARIES}
    unofficial::concurrentqueue::concurrentqueue
    # nlohmann_json nlohmann_json::nlohmann_json
    nlohmann_json::nlohmann_json
    pybind11::lto pybind11::embed pybind11::module
    $<BUILD_INTERFACE:${PYTHON_LIBRARIES}>
    spdlog::spdlog spdlog::spdlog_header_only
    # ${TBB_IMPORTED_TARGETS}
    TBB::tbb
    fmt::fmt
    cppzmq cppzmq-static
)
# target_link_libraries(elf PUBLIC
#     #${Boost_LIBRARIES}
#     concurrentqueue
#     nlohmann_json
#     pybind11
#     $<BUILD_INTERFACE:${PYTHON_LIBRARIES}>
#     spdlog
#     ${TBB_IMPORTED_TARGETS}
# )

# Tests

enable_testing()
add_cpp_tests(test_cpp_elf_ elf ${ELF_TEST_SOURCES})

# Python bindings

pybind11_add_module(_elf pybind_module.cpp)
target_link_libraries(_elf PRIVATE
    elf
)
# set_target_properties(_elf PROPERTIES
#    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/../../src_py/elf")
