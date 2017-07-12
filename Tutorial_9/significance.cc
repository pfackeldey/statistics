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
#include "RooCategory.h"
#include "RooStats/ModelConfig.h"
#include <RooStats/FrequentistCalculator.h>
#include <RooStats/HybridCalculator.h>
#include <RooStats/HypoTestResult.h>
#include <RooStats/ProfileLikelihoodTestStat.h>
#include <RooStats/HypoTestInverter.h>
using namespace std;

using namespace RooFit;
using namespace RooStats;




int main(void)
{
	
		//Simple Poisson cut & count using RooStats
		
		
		//First create the model, very similar to what we have done in RooFit two weeks ago
		
	   int nobs = 5;   // number of observed events
	   double b = 1; // number of background events
	   double sigmab = 0.2;   // relative uncertainty in b

	   RooWorkspace *w = new RooWorkspace("w");

	   // make Poisson model * Gaussian constraint
	   w->factory("sum:nexp(s[3,0,15],b[1,0,10])");
	   // Poisson of (n | s+b)
	   w->factory("Poisson:pdf(nobs[0,50],nexp)");
	   w->factory("Gaussian:constraint(b0[0,10],b,sigmab[1])");
	   w->factory("PROD:model(pdf,constraint)");	
	   
	   RooRealVar * obs = w->var("nobs");
	   w->var("b0")->setVal(b);
	   w->var("b0")->setConstant(true); // needed for being treated as global observables
	   w->var("sigmab")->setVal(sigmab*b);  

	   // use this to avoid too large ranges 
	   w->var("b")->setMax(10*b);
	   w->var("s")->setMax(10*b);
	   
	   //set value of observed events
	   obs->setVal(nobs);	   	
	   

	   // make data set with the number of observed events
	   RooDataSet * data = new RooDataSet("data","", *obs );
	   data->add(*obs );
	   w->import(*data);

	   ModelConfig * sbModel = new ModelConfig("sbModel",w);
	   sbModel->SetPdf(*w->pdf("model"));
	   sbModel->SetParametersOfInterest(*w->var("s"));
	   sbModel->SetObservables(*w->var("nobs"));
	   sbModel->SetNuisanceParameters(*w->var("b"));

	   // these are needed for the hypothesis tests
	   sbModel->SetSnapshot(*w->var("s"));
	   sbModel->SetGlobalObservables(*w->var("b0"));

	   sbModel->Print();
	
	   
	   
	   RooRealVar* poi = (RooRealVar*) sbModel->GetParametersOfInterest()->first();
	   ModelConfig * bModel = (ModelConfig*) sbModel->Clone("bModel");
	   double oldval = poi->getVal();
	   poi->setVal(0);
	   bModel->SetSnapshot( *poi  );
	   poi->setVal(oldval);	
			  
	   HybridCalculator *  fc  = new HybridCalculator(*data, *sbModel, *bModel);
	   fc->SetToys(10000,1000);    // 1000 for null (S+B) , 50 for alt (B)	
	   HypoTestInverter calc(*fc);
  
	   
	   ToyMCSampler *toymcs = (ToyMCSampler*)calc.GetHypoTestCalculator()->GetTestStatSampler();
	   // for number counting (extended pdf do not need this)
	   // toymcs->SetNEventsPerToy(1);
	   

	   // profile likelihood test statistics 
	   ProfileLikelihoodTestStat profll(*sbModel->GetPdf());
	   // for CLs (bounded intervals) use one-sided profile likelihood

	   // ratio of profile likelihood - need to pass snapshot for the alt 
	   // RatioOfProfiledLikelihoodsTestStat ropl(*sbModel->GetPdf(), *bModel->GetPdf(), bModel->GetSnapshot());
	   

	   // set the test statistic to use 
	   toymcs->SetTestStatistic(&profll);	   
	  if (!sbModel->GetPdf()->canBeExtended())
		 toymcs->SetNEventsPerToy(1);	   
       HypoTestResult* calcResult = fc->GetHypoTest();

      calcResult->Print();


	
               
	
}
