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
#include <string>

#include <RooRealVar.h>
#include <RooAddPdf.h>
#include <RooDataSet.h>
#include <RooDataHist.h>
#include <RooGaussian.h>
#include <RooArgusBG.h>
#include <RooArgList.h>
#include <RooPlot.h>
#include "RooConstVar.h"
#include "RooWorkspace.h"
#include <fstream>

using namespace std;

using namespace RooFit;

#include <sstream>
template <typename T>  // for old c++ versions...
  std::string to_string ( T Number )
  {
     std::ostringstream ss;
     ss << Number;
     return ss.str();
}



int main(void)
{
	vector<float> m;
	for (int bin = 25; bin <= 75; bin += 25) {

		for (float sigma = 0.1; sigma <= 0.5; sigma += 0.05) {

			// read histograms from TFile
			TCanvas *c1 = new TCanvas("c1","c1",800,800);

			// Creating the workspace object
			RooWorkspace *w = new RooWorkspace("w");

			//Defining the background pdf. Remember, this line corresponds to three lines when you do not use the workspace:
			/* //first define the observable
			 * RooRealVar *x = new RooRealVar("x","",0,10) ;
			 * //then define the parameter
			 * RooRealVar *a = new RooRealVar("a","",-0.5,-1000,0) ;
			 * // finally define the background pdf
			 * RooExponential *bkg_pdf = new RooExponential("bkg_pdf","",x,a);
			 * */
			w->factory("Exponential:bkg_pdf(x[0,10], a[-0.5,-1000,0])");
			//Similarly now define signal pdf. Note that x has already been initialized in the line above, so we don't have to do it again
			w->factory("Gaussian:sig_pdf(x, mass[2,0,10], sigma[0,1])");
			//Create the combined model as sum of the two pdfs with normalization parameters for both.
			w->factory("SUM:model(nsig[0,1000]*sig_pdf, nbkg[0,1000000]*bkg_pdf)");
			//Set the binning of the variable. This is used only for the plot! The fit is still unbinnend

			w->var("x")->setBins(bin);

			//Set the normalizations to some values and sigma
			w->var("sigma")->setVal(sigma);
			w->var("nsig")->setVal(300);
			w->var("nbkg")->setVal(10000);
			//Now generate events according to the model, the number of events will be nsig+nbkg
			RooDataSet * data = w->pdf("model")->generate( *w->var("x"));
			//Import dataset into workspace
			data->SetName("data");
			w->import(*data);
			//Now fit model to generated data
			w->pdf("model")->fitTo(*w->data("data"));
			//Now create a frame and plot the data and the models
			//Set the binning of the variable. This is used only for the plot! The fit is still unbinnend

			//save peak values
			m.push_back(w->var("mass")->getVal());

			RooPlot* xframe = w->var("x")->frame();
			w->data("data")->plotOn(xframe) ;
			w->pdf("model")->plotOn(xframe) ;
			w->pdf("model")->plotOn(xframe,Components(RooArgSet(*w->pdf("bkg_pdf"))),LineStyle(kDashed)) ;
			w->pdf("model")->plotOn(xframe,Components(RooArgSet(*w->pdf("sig_pdf"))),LineStyle(kDashed)) ;
			xframe->Draw();
			c1->Print(("roofit_bin_"+to_string(bin)+"_sigma_"+to_string(sigma)+".pdf").c_str());
			w->Print();
			//Clear the canvas so we can draw new things
			c1->Clear();
		}
	}
	vector<float> m1;
	for (int bin = 25; bin <= 75; bin += 25) {

		for (float sigma = 0.1; sigma <= 0.5; sigma += 0.05) {

			// read histograms from TFile
			TCanvas *c1 = new TCanvas("c1","c1",800,800);

			// Creating the workspace object
			RooWorkspace *w = new RooWorkspace("w");

			//Defining the background pdf. Remember, this line corresponds to three lines when you do not use the workspace:
			/* //first define the observable
			 * RooRealVar *x = new RooRealVar("x","",0,10) ;
			 * //then define the parameter
			 * RooRealVar *a = new RooRealVar("a","",-0.5,-1000,0) ;
			 * // finally define the background pdf
			 * RooExponential *bkg_pdf = new RooExponential("bkg_pdf","",x,a);
			 * */
			w->factory("Exponential:bkg_pdf(x[0,10], a[-0.5,-1000,0])");
			//Similarly now define signal pdf. Note that x has already been initialized in the line above, so we don't have to do it again
			w->factory("Gaussian:sig_pdf(x, mass[2,0,10], sigma[0,1])");
			//Create the combined model as sum of the two pdfs with normalization parameters for both.
			w->factory("SUM:model(nsig[0,1000]*sig_pdf, nbkg[0,1000000]*bkg_pdf)");
			//Set the binning of the variable. This is used only for the plot! The fit is still unbinnend

			w->var("x")->setBins(bin);

			//Set the normalizations to some values and sigma
			w->var("sigma")->setVal(sigma);
			w->var("nsig")->setVal(300);
			w->var("nbkg")->setVal(10000);
			//Now generate events according to the model, the number of events will be nsig+nbkg
			RooDataSet * data = w->pdf("model")->generate( *w->var("x"));
			//Import dataset into workspace
			data->SetName("data");
			w->import(*data);
			//Now fit model to generated data
			w->pdf("model")->fitTo(*w->data("data"));
			//Now create a frame and plot the data and the models
			//Set the binning of the variable. This is used only for the plot! The fit is still unbinnend

			//save peak values
			m1.push_back(w->var("mass")->getVal());

			//Now do a binned fit. First we need a binned dataset

			RooDataHist *hist = data->binnedClone();
			hist->SetName("datahist");
			w->import(*hist);

			w->pdf("model")->fitTo(*w->data("datahist"));

			//Now create a frame and plot the data and the models
			RooPlot* xframe2 = w->var("x")->frame();
			w->data("datahist")->plotOn(xframe2) ;
			w->pdf("model")->plotOn(xframe2) ;
			w->pdf("model")->plotOn(xframe2,Components(RooArgSet(*w->pdf("bkg_pdf"))),LineStyle(kDashed)) ;
			w->pdf("model")->plotOn(xframe2,Components(RooArgSet(*w->pdf("sig_pdf"))),LineStyle(kDashed)) ;
			xframe2->Draw();
			c1->Print(("roofitBinned_bin_"+to_string(bin)+"_sigma_"+to_string(sigma)+".pdf").c_str());
		}
	}
	cout << "PEAK VALUES ARE FOR UNBINNED - ACTUAL PEAK VALUE OF 2 ARE: \n";
	for (unsigned i=0; i<=23; i++) {
		cout << abs(m[i]-2.);
		cout << "\n";
	}
	cout << "PEAK VALUES ARE FOR BINNED - ACTUAL PEAK VALUE OF 2 ARE: \n";
	for (unsigned i=0; i<=23; i++) {
		cout << abs(m1[i]-2.);
		cout << "\n";
	}

}
