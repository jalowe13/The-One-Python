cmake_minimum_required(VERSION 3.5)
project(TheOne CXX)

set(main_src
  WinMain.cpp
  Graphics.cpp Graphics.h
  Ball.cpp	Ball.h
)

add_executable(WinMain ${main_src})
set_property(TARGET WinMain PROPERTY CXX_STANDARD 11)
