cmake_minimum_required(VERSION 2.8)

project(vehicle_detection_haarcascades)

find_package(OpenCV REQUIRED)

set(vehicle_detection_src vehicle_detection.cpp)

include_directories(${CMAKE_SOURCE_DIR})

add_executable(vehicle_detection_haarcascades ${vehicle_detection_src})

target_link_libraries(vehicle_detection_haarcascades ${OpenCV_LIBS})

