#include<bits/stdc++.h>

using namespace std;


class person 
{
	public : 
	void func(int x)
	{
		cout<<"x  : "<<x<<"\n";
	}
	
	void func(double x)
	{
		cout<<"x : "<<x<<"\n";
	}
	
	void func(char x)
	{
		cout<<"x : "<<x<<"\n";
	}
	
	void func(int x , int y)
	{
		cout<<"x : "<<x;
		cout<<"\ny : "<<y<<"\n";
	}
};

int main()
{
	person one ;
	one.func(1);
	one.func(12.3);
	one.func('a');
	one.func(12 , 13);
	system("pause");
	return 0;
}