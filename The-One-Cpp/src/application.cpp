#include "application.hpp"
#include <iostream>


Application::Application()
{
  std::cout << "New Application Created\n";
}

Application::~Application()
{
  std::cout << "Application Destroyed\n";
}
