#include "Ball.h"

Ball::Ball()
{
	x = (rand() % 1000);
	y = (rand() % 600);
	movementMod = 10;
}

Ball::~Ball()
{
}

void Ball::drawBall(Graphics* graphics)
{
	graphics->DrawCircle(x, y, 10, 100.0, 100.0, 100.0, 1.0);
}

void Ball::incX()
{
	x = x + movementMod;
}

void Ball::incY()
{
	y = y + movementMod;
}

void Ball::decX()
{
	x = x - movementMod;
}

void Ball::decY()
{
	y = y - movementMod;
}


