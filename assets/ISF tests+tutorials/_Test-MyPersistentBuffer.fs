/*{
	"DESCRIPTION": "demonstrates the use of a persistent buffer to create a motion-blur type effect. also demonstrates the simplest use of steps: a one-step rendering pass",
	"CREDIT": "by zoidberg",
	"CATEGORIES": [
		"TEST-GLSL FX"
	],
	"INPUTS": [
		{
			"NAME": "inputImage",
			"TYPE": "image"
		},
		{
			"NAME": "blurAmount",
			"TYPE": "float"
		}
	],
	"PERSISTENT_BUFFERS": [
		"bufferVariableNameA", "bufferVariableNameB"
	]
	
	
}*/

void main()
{
	vec4		freshPixel = IMG_THIS_PIXEL(inputImage);
	//vec4		stalePixel = IMG_THIS_PIXEL(bufferVariableNameA);
	vec4 red = vec4(1.0, 0.0, 0.0, 1.0);
	vec4 green = vec4(0.0, 1.0, 0.0, 1.0);
	bufferVariableNameA = red;
	bufferVariableNameB = green;
	gl_FragColor = freshPixel;
}
