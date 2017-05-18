#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <string>
//~ #include <TCanvas.h>
//~ #include <TH2F.h>
//~ #include <TF1.h>
//~ #include <TGraph.h>

using namespace std;


int width, height;

unsigned char* readBMP(char* filename, int & width, int & height)
{
	// thanks to stackoverflow user 0605002 (http://stackoverflow.com/questions/9296059/read-pixel-value-in-bmp-file)
	// reads the (R, G, B) values of the pixels.
	// The color of pixel (i, j) is stored at data[j * width + i], data[j * width + i + 1] and data[j * width + i + 2].

    FILE* f = fopen(filename, "rb");
    unsigned char info[54];
    fread(info, sizeof(unsigned char), 54, f); // read the 54-byte header


    // extract image height and width from header
    width = *(int*)&info[18];
    height = *(int*)&info[22];


    int size = 3 * (*width) * (*height);
    unsigned char* data = new unsigned char[size]; // allocate 3 bytes (one per color channel) per pixel
    fread(data, sizeof(unsigned char), size, f); // read the rest (only RGB values) of the data at once
    fclose(f);


    return data;
}



int main(){

	width = 0;
	height = 0;
	string filename = "elephant.bmp"
	unsigned char* pixels = readBMP(filename.c_str(), width, height);
	cout << "image dimensions: " << width << "x" << height << endl << endl;

	// Your code goes here

}
