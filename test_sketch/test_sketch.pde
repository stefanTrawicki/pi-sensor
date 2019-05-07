//Array preferences
int ARRAYLENGTH = 7;
int TIMEMAX = 3600;

//Display preferences
int width = 800;
int height = 450;
int border = 25;

//Instantiation
int[] buffer = new int[ARRAYLENGTH];
int startX = border; 
int endX = width-border;
int startY = border;
int endY = height-border;

color[] colorChart = {
		color(255, 0, 0),
		color(255, 60, 0),
		color(255, 120, 0),
		color(255, 255, 255),
		color(0, 0, 0)
		};

void setup()
{
	size(800, 450);
}

void draw()
{
	background(colorChart[3]);
	strokeWeight(1);
	stroke(colorChart[4]);
	line(startX, height-border, endX, height-border);
	line(border, startY, border, endY);
}
