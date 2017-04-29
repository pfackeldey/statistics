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
		
		hist->Fill(rand->Gaus(20,5));
		
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
	
	
	TH1F *hist1 = new TH1F("hist1","hist1",30,0,30);
	for (int k=0; k < 10; k++){
		TH1F *hist2 = new TH1F("hist2","hist2",30,0,30);		
		for (int i = 0; i < 100; i++){

			hist2->Fill(rand->Binomial(20,0.5));
			//hist2->Fill(rand->Poisson(10));
			//hist2->Fill(rand->Uniform(5,15));

		}
		hist1->Add(hist2);
	}
	hist1->Fit("f1");
	TCanvas *c2 = new TCanvas("c2","c2",800,800);	
	hist1->Draw();
	
	
	c2->Print("CLT_binomial.pdf");

	TH1F *hist3 = new TH1F("hist1","hist1",30,0,30);
	for (int k=0; k < 10; k++){
		TH1F *hist4 = new TH1F("hist2","hist2",30,0,30);		
		for (int i = 0; i < 100; i++){

			//hist4->Fill(rand->Binomial(20,0.5));
			hist4->Fill(rand->Poisson(10));
			//hist2->Fill(rand->Uniform(5,15));

		}
		hist3->Add(hist4);
	}
	hist3->Fit("f1");
	TCanvas *c3 = new TCanvas("c3","c3",800,800);	
	hist3->Draw();
	
	
	c3->Print("CLT_poisson.pdf");


	float a = 10.;
	float b = 0.;
	TH1F *hist5 = new TH1F("hist1","hist1",30,0,30);
	for (int k=0; k < 20; k++){
		float b = rand->Uniform(1,5);
		TH1F *hist6 = new TH1F("hist2","hist2",30,0,30);		
		for (int i = 0; i < 100; i++){
			hist6->Fill(rand->Uniform(a-b,a+b));
		}
		hist5->Add(hist6);
	}
	hist5->Fit("f1");
	TCanvas *c4 = new TCanvas("c4","c4",800,800);	
	hist5->Draw();
	
	
	c4->Print("CLT_uniform.pdf");
	
  

}

/*
Task 3.a):

***************
1st parameter :
	f1->SetParameter(0,160); //maximum y-Value
	f1->SetParameter(1,10); // mean
	f1->SetParameter(2,2.5); // width

output : 
 FCN=22.7877 FROM MIGRAD    STATUS=CONVERGED      84 CALLS          85 TOTAL
                     EDM=2.72952e-09    STRATEGY= 1  ERROR MATRIX UNCERTAINTY   1.9 per cent
  EXT PARAMETER                                   STEP         FIRST   
  NO.   NAME      VALUE            ERROR          SIZE      DERIVATIVE 
   1  p0           4.33194e+01   3.08045e+00   6.58758e-03   7.67891e-06
   2  p1           1.05883e+01   1.74387e-01  -1.00433e-04   5.49574e-04
   3  p2           2.64083e+00   1.16646e-01  -7.37033e-07   1.25510e-04

2nd parameter :
	f1->SetParameter(0,160); //maximum y-Value
	f1->SetParameter(1,20); // mean
	f1->SetParameter(2,2.5); // width

output : 
 FCN=243.463 FROM HESSE     STATUS=OK             16 CALLS         537 TOTAL
                     EDM=1.14502e-07    STRATEGY= 1      ERROR MATRIX ACCURATE 
  EXT PARAMETER                                   STEP         FIRST   
  NO.   NAME      VALUE            ERROR          SIZE      DERIVATIVE 
   1  p0           1.56537e+01   1.44449e+02   3.17867e-03   2.26702e-04
   2  p1           6.15491e+07   1.16019e+08   1.46745e+01  -1.84950e-10
   3  p2           3.43410e+07   6.42077e+07   8.84459e+00   3.31018e-10

3rd parameter : 
	f1->SetParameter(0,160); //maximum y-Value
	f1->SetParameter(1,20); // mean
	f1->SetParameter(2,5); // width

output : 
 FCN=6.29056 FROM MIGRAD    STATUS=CONVERGED     563 CALLS         564 TOTAL
                     EDM=4.25093e-07    STRATEGY= 1      ERROR MATRIX ACCURATE 
  EXT PARAMETER                                   STEP         FIRST   
  NO.   NAME      VALUE            ERROR          SIZE      DERIVATIVE 
   1  p0           4.21723e+01   3.16909e+00   3.24621e-03   3.11608e-04
   2  p1           1.00875e+01   1.75271e-01   2.28092e-04  -2.78085e-03
   3  p2           2.82324e+00   1.48335e-01   1.50345e-04   3.93596e-03
*************

Task 3.b):

*************
TMATH:
Binomial expects n and k as integers: Double_t Binomial(Int_t n, Int_t k)
Poisson expects 2 double floats (x and par): Double_t TMath::Poisson(Double_t x, Double_t par)
Uniform is not implemented in TMATH

TRANDOM:	
Binomial expects 1 integer (n_tot) and 1 double float (probability): Int_t TRandom::Binomial (Int_t ntot,Double_t prob) 
Poisson	expects 1 double float (mean): virtual Int_t Poisson (Double_t mean) #### here: it works with an integer as variable input
Uniform expects 2 double floats (x1 and x2): virtual Double_t Uniform (Double_t x1, Double_t x2) #### here: it works with an integer as variable input

additional: In the plots of Binomial,Poisson and Uniform histograms one can see that some bins have large fluctuations. This is due to small amount of statistics (only 100 generated numbers). Nevertheless one can clearly see that the shape of all three distributions is following the "theory" shapes (shape with way more statistics).
*************

Task 3.c):

*************
The fit to the gaussian distribution shows that the CLT is valid for adding each pdf to itself several times.
*************
*/
