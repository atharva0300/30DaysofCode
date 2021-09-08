#include<bits/stdc++.h>
using namespace std;

int main()
{
	cout<<"Hello there\n"<<"My name is person\n";
	cout<<sqrt(12)<<"\n";
	int a=2;
	int b=3;
	int sum = a+b;
	// char , int . float , double , bool
	//char - stores the characters 
	// int - stores the integer 
	// double - stores double values 
	// bool - stores true and false 
	char c ='a';
	int a2 =3;
	double b2 =3.5;
	cout<<c<<" "<<a2;
	cout<<b2<<"\n";
	//Simple oeprators 
	cout<<20%7<<"\n";
	cout<<7*4<<"\n";
	int a3= 5;
	cout<<a3+1<<"\n";
	cout<<a3++<<"\n";
	cout<<++a3<<"\n";
	
	char c3 ='a';
	cout<<"ASCII value of "<<c3<<" is : "<<int(c3)<<"\n";
	//typecasting cahrater data type to integer data type
	char c4 = 'b';
	cout<<(int(c3)-int(c4))<<"\n";
	double d2;
	cin>>d2;
	cout<<int(d2)<<"\n";
	cin.get();
	//Overflow 
	cout<<7/2<<"\n";
	cout<<int('c')<<"\n";
	
	//Operator precedence 
	// ++ , -- > all other 
	cout<<7/2*3<<"\n";
	cout<<3*7/2<<"\n";
	
	// data types 
	// int , char , long int , long long int , float , double 
	// int range - -10^9 < int < 10^9
	// long int range - -10^12 < ling int < 10^12
	// long long int range - -10^18 < long long int < 10^18
	int a5 = 1000000;
	int b5= 1000000;
	int c5 = a5*b5;
	// gives garbage value 
	
	double a6 = 1000000;
	double b6= 1000000;
	double c6 = a6*b6;
	cout<<setprecision(0)<<c6<<"\n";
	
	double c8 = 1e24;
	cout<<c8<<"\n";
	
	cout<<sizeof(signed int)<<"\n";
	cout<<"Hit Enter : \n";
	cin.get();
	return 0;
}