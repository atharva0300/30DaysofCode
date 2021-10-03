#include<bits/stdc++.h>

using namespace std;

class base
{
	public : 
	virtual void print()
	{
		cout<<"\nprint base class : \n";
	}
	void show()
	{
		cout<<"\nshow base class\n";
	}
};

class derived : public base
{
	void print()
	{
		cout<<"\nprint derived class \n";
	}
	void show()
	{
		cout<<"\nshow derived class\n";
	}
};
int main()
{
	base *bptr;
	derived d;
	bptr=  &d;
	// virtual function, binded at runtime ( runtime polymorphism )
	bptr->print();
	
	// non -virtual funcion\, binded at compile time 
	bptr->show();
	
	system("pause");
	return 0;
}