#include <iostream>                       ///exp.cc
#include <cmath>
#include <iomanip>
#include <stdio.h>
#include <TCanvas.h>
#include <TF1.h>



//Peter Fackeldey 330532
//Sebastian Wuchterl 331453



float Exp(const float& x) {
float res = 0.0, step = 1.0; 
int n=1;
for(; n<50; ++n) {
	res += step;
	step*= x/n;
}
std::cout << "With "<< n << " steps" <<std::endl;
return res;
}

void drawExp() {
TCanvas *c1 = new TCanvas("c1","c1",800,800);
TF1 *f = new TF1("exp","TMath::Exp(x)",0,2);
f->Draw();
c1->SaveAs("exp.pdf");
delete f;
delete c1;
}

int main( int argc, char *argv[]) {
if (argc<2) return 1;
float x = atof( argv[1] );
float res = (x>0.?Exp(x):1./Exp(-x));
std::cout << std::setprecision(12) 
<< "   my exp(x) = " << res << "\n"
<< "cmath exp(x) = " << exp( x ) << std::endl;
drawExp();
return 0;
}
