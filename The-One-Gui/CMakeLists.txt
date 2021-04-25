cmake_minimum_required(VERSION 3.5)
project(TheOne CXX)

set(main_src
  main.cpp
)

add_executable(main WIN32 ${main_src})
set_property(TARGET main PROPERTY CXX_STANDARD 11)
