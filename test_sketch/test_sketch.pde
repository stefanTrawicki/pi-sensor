int ARRAYLENGTH = 7;
int TIMEMAX = 3600;
int[] buffer = new int[ARRAYLENGTH];

color[] colorChart = {
		color(255, 0, 0),
		color(255, 60, 0),
		color(255, 120, 0)
		};

void setup()
{
	size(800, 450);
}

void draw()
{
	background(colorChart[0]);
}
