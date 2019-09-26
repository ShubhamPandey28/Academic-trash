cmake_minimum_required(VERSION 3.0)

set(CMAKE_BUILD_TYPE Debug)

project(cs202assignment1)


add_library(
    seqLinearList.hpp
    sorting.hpp
)
target_link_libraries(
    cs202assignment1
    seqLinearList.hpp
    sorting.hpp
)

add_executable(
    cs202assignment1
    problem1.cpp
    problem5.cpp
    problem3.cpp
    sortingImp.cpp
    
)

