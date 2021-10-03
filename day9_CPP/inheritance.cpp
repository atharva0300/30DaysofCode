#include<bits/stdc++.h>

using namespace std;

class parent
{
	public : 
	int id;
	parent()
	{
		cout<<"\nThis is the parent class ";
	}
	private : 
	int x;
	protected : 
	int y;
};

class child: public parent
{
	public : 
	int person;
	child ()
	{
		cout<<"\nThis is child class ";
	}
};

class third : public parent , public child 
{
	public : 
	int four;
	third ()
	{
		cout<<"\nThis is the third class \n";
	}
};

class one
{
	public : 
	int one;
};

class two : public one
{
	public :
	int two;
};

class three : public one
{
	public : 
	int three;
};

class four : public two , public three
{
	public : 
	int four;
};
int main()
{
	child one;
	one.person =7;
	one.id= 12;
	cout<<"\nperson : "<<one.person;
	cout<<"\nid : "<<one.id<<"\n";
	parent two;
	cout<<"\nafte that : \n";
	cout<<"\n";
	third reason;
	reason.four  = 4;
	cout<<reason.four;
	cout<<"\n";
	
	four object ;
	object.two::one = 10;
	object.three::one = 100;
	
	object.two = 20;
	object.three = 30;
	object.four = 40;
	
	cout<<"\none from b : "<<object.two::one<<"\n";
	cout<<"\none form c : "<<object.three::one<<"\n";
	
	cout<<"\ntwo : "<<object.two;
	cout<<"\nthree : "<<object.three;
	cout<<"\nfour  : "<<object.four<<"\n";
	system("pause");
	return 0;
}