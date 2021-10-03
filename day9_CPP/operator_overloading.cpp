#include<bits/stdc++.h>

using namespace std;

class Complex
{
	private : 
	int real , imag;
	
	public : 
	Complex(int r=0 , int i=0)
	{
		real  =r;
		imag =i;
	}
	
	//This above function gets automatically called 
	Complex operator + (Complex const &obj)
	{
		Complex res;
		res.real = real + obj.real;
		res.imag = imag + obj.imag;
		return res;
	}
	void print()
	{
		cout<<real<<" +i"<<imag<<"\n";
	}
};
int main()
{
	Complex c1(12,3) , c2(13,4);
	Complex c3 = c1 + c2;
	c3.print();
	
	system("pause");
	return 0;
}