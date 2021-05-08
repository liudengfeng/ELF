cmake_minimum_required(VERSION 3.19)

project(zmq_server)
project(zmq_client)

set(CMAKE_CXX_STANDARD 17)
set(PYBIND11_CPP_STANDARD -std=c++17)

find_package(ZeroMQ CONFIG REQUIRED)

add_executable(zmq_server server.cpp)
add_executable(zmq_client client.cpp)

target_link_libraries(zmq_server PRIVATE libzmq libzmq-static)
target_link_libraries(zmq_client PRIVATE libzmq libzmq-static)
