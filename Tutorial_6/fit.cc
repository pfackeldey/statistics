#include <iostream>                       ///centralLimit.cc
#include <cmath>
#include <iomanip>
#include <stdio.h>
#include <stdlib.h>
#include <TCanvas.h>
#include <TF1.h>
#include <TFile.h>
#include <TH1F.h>
#include <TRandom3.h>
#include <TROOT.h>
#include <TStyle.h>
#include <THStack.h>
#include <TLegend.h>
#include <TString.h>
#include <TGraph.h>
using namespace std;


int fit()
{
	//create TCanvas object on which we will draw the histogram, the constructor has as arguments the name, title, and size of canvas in x and y in number of pixels
	TCanvas *c1 = new TCanvas("c1","c1",800,800);
	// Use DrawFrame function to plot the frame independent from the content
	c1->DrawFrame(0,0,200,10000,"; mass [GeV] ; Events / 2 GeV");


	TF1 *f1 = new TF1("f1","[0]*ROOT::Math::exponential_pdf(x,[1])+gaus(2)",0,200);
	// set parameters to the values of the generated function
	f1->SetParameter(0,50000); // normalization of first exponential part
	f1->SetParameter(1,2); // parameter lambda of first exponential falloff
	f1->SetParameter(2,10000); // normalization of gaussian part
	f1->SetParameter(3,50);// parameter of gaussian mean
	f1->SetParameter(4,1);   // parameter of gaussian sigma
	// constrain parameter limits
	f1->SetParLimits(1,0,10);
	f1->SetParLimits(4,1,10);
	f1->SetParLimits(3,45,55);

	//read histograms by name
	TFile *file =new TFile("histos_ex3.root","READ");
	TH1F *hist = (TH1F*) file->Get("hist");
	hist->Fit("f1");
	hist->Draw("same");
	c1->Print("fit_solution.pdf");
	Double_t chi2_ndof = f1->GetChisquare()/f1->GetNDF();
	Double_t chi2 = f1->GetChisquare();
	std::cout << "chi2: "<< chi2 << std::endl;
	std::cout << "chi2/ndof: "<< chi2_ndof << std::endl;
	return 0;
}

int main(void)
{
	return fit();
}
