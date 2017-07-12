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
#include <RooStats/HypoTestInverter.h>
#include <RooStats/ProfileLikelihoodTestStat.h>
#include <RooStats/RatioOfProfiledLikelihoodsTestStat.h>
#include <RooStats/SimpleLikelihoodRatioTestStat.h>
#include <RooStats/SamplingDistPlot.h>
#include <RooStats/HypoTestInverterPlot.h>
using namespace std;

using namespace RooFit;
using namespace RooStats;




int main(void)
{
	
		//Simple Poisson cut & count using RooStats
		
		
		//First create the model, very similar to what we have done in RooFit last week
		
	   int nobs = 0;   // number of observed events
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
	   w->var("b")->setMax(b+5*b*sigmab);
	   //~ w->var("s")->setMax(b+5*b*sigmab);
	   
	   //set value of observed events
	   obs->setVal(nobs);	   	
	   

	   // make data set with the namber of observed events
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
			  
	   HybridCalculator *  fc  = new HybridCalculator(*data, *bModel, *sbModel);
	   fc->SetToys(1000,500);    // 1000 for null (S+B) , 500 for alt (B)	


	   
	   HypoTestInverter calc(*fc);

	   // set confidence level (e.g. 95% upper limits)
	   	   calc.SetConfidenceLevel(0.95);
	   calc.UseCLs(true);   	

	   SimpleLikelihoodRatioTestStat  slrts(*bModel->GetPdf(), *sbModel->GetPdf());
	   // null parameters must includes snapshot of poi plus the nuisance values 
	   RooArgSet nullParams(*bModel->GetSnapshot());
	   if (bModel->GetNuisanceParameters()) nullParams.add(*bModel->GetNuisanceParameters());
	   
	   slrts.SetNullParameters(nullParams);
	   RooArgSet altParams(*sbModel->GetSnapshot());
	   if (sbModel->GetNuisanceParameters()) altParams.add(*sbModel->GetNuisanceParameters());
	   slrts.SetAltParameters(altParams);

	   
	   ToyMCSampler *toymcs = (ToyMCSampler*)calc.GetHypoTestCalculator()->GetTestStatSampler();
	   // for number counting (extended pdf do not need this)
	   // toymcs->SetNEventsPerToy(1);
	   

	   // profile likelihood test statistics 
	   ProfileLikelihoodTestStat profll(*sbModel->GetPdf());
	   // ratio of profile likelihood - need to pass snapshot for the alt 
	    RatioOfProfiledLikelihoodsTestStat ropl(*sbModel->GetPdf(), *bModel->GetPdf(), bModel->GetSnapshot());


	   // set the test statistic to use 
	   //~ toymcs->SetTestStatistic(&ropl);
	   //~ toymcs->SetTestStatistic(&profll);
	   toymcs->SetTestStatistic(&slrts);

	  // if the pdf is not extended (e.g. in the Poisson model)                                            
	  // we need to set the number of events  
	  if (!sbModel->GetPdf()->canBeExtended())
		 toymcs->SetNEventsPerToy(1);
	 
	 
	   int npoints = 10;  // number of points to scan
	   // min and max (better to choose smaller intervals)
	   double poimin = poi->getMin();
	   double poimax = poi->getMax();
	   //poimin = 0; poimax=10;

	   std::cout << "Doing a fixed scan  in interval : " << poimin << " , " << poimax << std::endl;
	   calc.SetFixedScan(npoints,poimin,poimax);
	  

	   HypoTestInverterResult * r = calc.GetInterval();
	   
	   
	   double upperLimit = r->UpperLimit();
	   double ulError = r->UpperLimitEstimatedError();
	   // double lowerLimit = r->LowerLimit();
	   // double llError = r->LowerLimitEstimatedError();
	   // if (lowerLimit < upperLimit*(1.- 1.E-4)) 
	   //    std::cout << "The computed lower limit is: " << lowerLimit << " +/- " << llError << std::endl;
	   std::cout << "The computed upper limit is: " << upperLimit << " +/- " << ulError << std::endl;
	  
	   // compute expected limit
	   std::cout << "Expected upper limits, using the B (alternate) model : " << std::endl;
	   std::cout << " expected limit (median) " << r->GetExpectedUpperLimit(0) << std::endl;
	   std::cout << " expected limit (-1 sig) " << r->GetExpectedUpperLimit(-1) << std::endl;
	   std::cout << " expected limit (+1 sig) " << r->GetExpectedUpperLimit(1) << std::endl;      
	   
	   HypoTestInverterPlot *plot = new HypoTestInverterPlot("HTI_Result_Plot","",r);

	   // plot in a new canvas with style
	   TCanvas * c1 = new TCanvas("HypoTestInverter Scan"); 
	   c1->SetLogy(false);

	   plot->Draw("CLb 2CL");  // plot also CLb and CLs+b 
	   //plot->Draw("OBS");  // plot only observed p-value


	   // plot also in a new canvas the test statistics distributions 
	  
	   // plot test statistics distributions for the two hypothesis
	   // when distribution is generated (case of FrequentistCalculators)	   
	              
	   const int n = r->ArraySize();
	   if (n> 0 &&  r->GetResult(0)->GetNullDistribution() ) { 
		  TCanvas * c2 = new TCanvas("Test Statistic Distributions","",2);
		  if (n > 1) {
			 int ny = TMath::CeilNint( sqrt(n) );
			 int nx = TMath::CeilNint(double(n)/ny);
			 c2->Divide( nx,ny);
		  }
		  for (int i=0; i<n; i++) {
			 if (n > 1) c2->cd(i+1);
			 SamplingDistPlot * pl = plot->MakeTestStatPlot(i);
			 pl->SetLogYaxis(true);
			 pl->Draw();
		  }
		  c2->Print("testStat.pdf");	
	   }

}
