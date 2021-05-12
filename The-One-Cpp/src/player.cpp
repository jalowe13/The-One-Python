#include "player.hpp"
#include <iostream>



Player::Player()
{
  std::cout << "New Player Created\n";
  something = 0;
}

Player::~Player()
{
  std::cout << "Player Destroyed\n";
}
