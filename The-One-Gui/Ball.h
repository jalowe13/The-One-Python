#include "Graphics.h"


class Ball
{
public:
	Ball();
	~Ball();

	void drawBall(Graphics* graphics);
	void incX();
	void incY();
	void decX();
	void decY();
private:
	float x;
	float y;
	int movementMod;
};