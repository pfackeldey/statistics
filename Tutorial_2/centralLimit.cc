#include <iostream>                       ///centralLimit.cc
#include <cmath>      
#include <iomanip>
#include <stdio.h>
#include <stdlib.h>
#include <TCanvas.h>
#include <TF1.h>
#include <TH1F.h>
#include <TRandom3.h>
#include <TROOT.h>
#include <TStyle.h>
           


int main(void)
{
	
	// Set up a random number generator from ROOT
	TRandom3 *rand = new TRandom3(0);
	
	//histogram to store the values, last three arguments specify number of bins and the range of the histogram
	TH1F *hist = new TH1F("hist","hist",30,0,30);
  
	//fill 1000 random numbers into the histogram, drawn from a Gaussian distribution with mean 10 and width 2.5
	for (int i = 0; i < 1000; i++){
		
		hist->Fill(rand->Gaus(10,2.5));
		
	}
	
	// create TF1 objection for a Gaussian function
	TF1 *f1 = new TF1("f1","[0]*TMath::Gaus(x,[1],[2])",0,30);
	// set parameters to the values of the generated function
	f1->SetParameter(0,160); //maximum y-Value
	f1->SetParameter(1,10); // mean
	f1->SetParameter(2,2.5); // width	
	
	//create TCanvas object on which we will draw the histogram, the constructor has as arguments the name, 
	//title, and size of canvas in x and y in number of pixels
	TCanvas *c1 = new TCanvas("c1","c1",800,800);
	//Draw histogram
	hist->Draw();
	//use "same" Draw-Option to draw onto the same canvas without overwriting the histogram
	f1->Draw("same");	
	//Save result as .pdf file
	c1->Print("c1.pdf");
	
	// for more potential functions you can get generated with TRandom and can implement using TMath, 
	//  see http://root.cern.ch/root/html/TMath.html and http://root.cern.ch/root/html/TRandom.html
	
	//~ gStyle->SetOptFit(1111);
	c1->Clear();
	TH1F *hist2 = new TH1F("hist2","hist2",30,0,30);
	for (int i = 0; i < 100; i++){


		hist2->Fill(rand->Binomial(20,0.5));
		hist2->Fill(rand->Poisson(10));
		hist2->Fill(rand->Uniform(5,15));

	}
	hist2->Fit("f1");
	hist2->Draw();
	
	c1->Print("c2.pdf");
	
  

}
