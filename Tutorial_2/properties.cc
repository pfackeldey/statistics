#include <iostream>  //std::cout, std::endl
#include <ctime>     //time
#include <cmath>     //sqrt
#include <map>       //std::map
#include <utility>   //std::pair
#include <sstream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm> // for sort
using namespace std;

double mean(std::vector<double> numbers){
	
	
	double mean = 0.;
	double nominator = 0.;
	double denominator =  numbers.size();
	
	for(std::vector<double>::iterator it = numbers.begin(); it != numbers.end(); ++it) {
		
		
		nominator += *it;
		
	
	}
	mean =  nominator/ denominator;
	return mean;
	
}


double variance(std::vector<double> numbers){
	
	
	return -1.;
	
}


double median(std::vector<double> numbers){
	
	
	return -1.;
	
}


double mode(std::vector<double> numbers){
	
	// treat all numbers as ints to allow for mode calculation
	// test all numbers between -10 and 100
	
	
	return -1.;
}


double skew(std::vector<double> numbers){
	
	return -1.;
}

double kurtosis(std::vector<double> numbers){
	
	return -1.;
}


int main(void)
{
	cout.precision(15);
	std::ifstream infile("randNumbers.txt");	
	std::string line;
	std::vector<double> numbers;
	while (std::getline(infile, line))
	{
		
		
		std::istringstream iss(line);
		double number;
		if (!(iss >> number)) { break; } // error
		
		iss >> number;
		numbers.push_back(number);
		

	} 

	cout << "Properties of the data samle" << endl;
	cout << "mean: " << mean(numbers) << endl;
	cout << "median: " << median(numbers) << endl;
	cout << "mode: " << mode(numbers) << endl;
	cout << "skew: " << skew(numbers) << endl;
	cout << "kurtosis: " << kurtosis(numbers) << endl;

	
	return 0;
}
