cmake_minimum_required(VERSION 3.5)
project(TheOne CXX)

set(main_src
  main.cpp
  player.cpp player.hpp
  application.cpp application.hpp
  )

add_executable(theone ${main_src})
set_property(TARGET theone PROPERTY CXX_STANDARD 11)
