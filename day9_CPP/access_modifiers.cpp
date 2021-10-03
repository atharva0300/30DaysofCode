#include<bits/stdc++.h>

using namespace std;

class circle{
	public : 
	double compute_area()
	{
		return 3.14*radius*radius;
	}
		double area(){
		return 3.14*radius*radius;
	}
	void set_radius(){
		cout<<"\nEnter radius : ";
		cin>>radius;
	}
	
	private: 
	double radius;
	
	protected: 
	int id;
	
};

class child: public circle
{
	public : 
	void set_id()
	{
		cout<<"\nEnter id : ";
		cin>>id;
	}
	int put_id()
	{
		return id;
	}
};
int main(){
	
	circle obj;
	obj.set_radius();
	cout<<"\nArea : "<<obj.area()<<"\n";
	child o;
	o.set_id();
	cout<<"\nId : "<<o.put_id()<<"\n";
	system("pause");
	return 0;
}