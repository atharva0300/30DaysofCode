#include<bits/stdc++.h>

using namespace std;

class implementabstraction
{
	private :
	int a , b;
	
	public : 
	// method to set the values 
	// private members 
	void set(int x , int y)
	{
		a= x;
		b = y;
	}
	
	void display()
	{
		cout<<"a : "<<a<<"\n";
		cout<<"b : "<<b<<"\n";
	}
	
};

int main()
{
	implementabstraction obj;
	obj.set(1 ,2);
	obj.display();
	
	system("pause");
	return 0;
}