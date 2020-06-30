cmake_minimum_required(VERSION 3.14)
project(OpenVRSDK)

include(conanbuildinfo.cmake)
conan_basic_setup()

add_subdirectory("sources")
