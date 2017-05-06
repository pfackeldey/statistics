#include <iostream>  //std::cout, std::endl
#include <ctime>     //time
#include <cmath>     //sqrt
#include <map>       //std::map
#include <utility>   //std::pair

using namespace std;

double Gaussian(const double x)
{
  // Gauss-Kurve;
  const double sigma=1.0;
  const double mu=0.0;
  return 1.0/(sigma*sqrt(2.0*M_PI))*exp(-0.5*(x-mu)*(x-mu)/(sigma*sigma));
}


double Romberg( double(*f)(const double), const double a, const double b)
{
  map<pair<int,int>, double> R;
  
  R[make_pair(0,0)] = 0.5 * (b - a) * (f(a) + f(b)); // R[0][0]
  int n = 0;
  while (n < 25) {
        ++n;
        double h = double(b - a) / pow(2.0, n);
        // for proper limits
	double sum=0.0;
	for (int k=1; k<=pow(2.0,n-1); ++k) sum += f(a+(2*k-1)*h);
	
  	R[make_pair(n,0)] = 0.5*R[make_pair(n-1,0)] + h*sum;
		
			      
  } 
  
  cout << "Can't provide a result as computation is not completely implemented" << endl;
  return -1;
  // cout << "integrated f(x) from "
       // << a<<" to "
       // << b<<" with Romberg: "
       // << R[make_pair(n,n)] << endl;
  //return R[make_pair(n,n)];
}

    
int main(void)
{
  Romberg( Gaussian, -1, 1);
    
  return 0;
}
