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
	double variance=0.;
	double mean_= mean(numbers);
	for (int i=0; i<numbers.size();i++){
		numbers[i]=pow((numbers[i]-mean_),2.);
	}
	variance=mean(numbers);
	return variance;
	
}


double median(std::vector<double> numbers){
	
	double median =0.;
	sort(numbers.begin(),numbers.end());
	int length = numbers.size();
	int middle = length/2.;
	if ( length % 2 == 0 ){ 
			median = (numbers.at(middle)+numbers.at(middle-1))/2.;
		}
	else 
		{
			median = numbers.at(middle);
		}
	
	return median;
	
}


double mode(std::vector<double> numbers){
	
	// treat all numbers as ints to allow for mode calculation
	// test all numbers between -10 and 100
	sort(numbers.begin(),numbers.end());
	int mode=0;
	int count=0;
	int count_old=0;
	int value=0;
	int rounded=0;
	int rounded_1=0;
	int beginner=numbers[0];
	for(int i=0;i<numbers.size();i++){
		rounded=numbers[i];
		if(i==0){rounded_1=beginner;}else{rounded_1=numbers[i-1];}
		if(rounded==rounded_1){
			count++;
		}else{
			if(count>count_old){
			value=numbers[i-1];
			count_old=count;}
			count=0;
		}
	}
	mode=value;
	return mode;
}



double skew(std::vector<double> numbers){
	double mean_= mean(numbers);
	double variance_= variance(numbers);
	double sigma = pow(variance_,1./2.);
	double skew=0.;
	for (int i=0; i<numbers.size();i++){
		numbers[i]=pow(((numbers[i]-mean_)/sigma),3.);
	}
	skew=mean(numbers);
	return skew;
}

double kurtosis(std::vector<double> numbers){
	double kurtosis=0.;
	double mean_=mean(numbers);
	double variance_=variance(numbers);
	double sigma = pow(variance_,1./2.);
	
	for (int i=0; i<numbers.size();i++){
		numbers[i]=pow((numbers[i]-mean_)/sigma,4.);
	}
	kurtosis=mean(numbers);
	return kurtosis;
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
	cout << "variance: " << variance(numbers) << endl;
	cout << "median: " << median(numbers) << endl;
	cout << "mode: " << mode(numbers) << endl;
	cout << "skew: " << skew(numbers) << endl;
	cout << "kurtosis: " << kurtosis(numbers) << endl;

	
	return 0;
}
