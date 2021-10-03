#include<bits/stdc++.h>

using namespace std;

class person{
	
	public : 
		string name;
		void printname(){
			cout<<"name : "<<name<<"\n";
		}
	
};
int main(){
	
	person p;
	p.name = "atharva";
	p.printname();
	system("pause");
	return 0;
}