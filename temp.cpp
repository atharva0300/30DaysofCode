#include<bits/stdc++.h>
#include<string>
using namespace std;

int main()
{
	int arr3[] = {1,6,2,3,4};
	int size2 = sizeof(arr3)/sizeof(int);
	int start =0;
	sort(arr3 , arr3 +size2);
	int end = size2-1;
	int x=1;
	while(start<=end)
	{
		int mid = (start+end)/2;
		if(arr3[mid]==x)
		{
			cout<<"Number found\n";
			break;
		}
		if(arr3[mid]>x)
		{
			end = mid -1;
		}
		else 
		{
			start = mid +1;
		}
	}
	//method 2 
	int k=0;
	for(int b=size2/2; size2>=1;size2/=2)
	{
		while(k+b<size2 && arr3[k+b]<=x)
		{
			k = k+b;
		}
	}
	if(arr3[k]==x)
	{
		cout<<"Element found\n";
		
	}
	
	vector<int>v;
	v.push_back(12);
	v.push_back(13);
	cout<<v[0]<<"\n";
	cout<<v[1]<<"\n";
	
	for(auto x : v)
	{
		cout<<x<<"\n";
	}
	v.pop_back();
	cout<<"\n";
	for(auto x : v)
	{
		cout<<x<<"\n";
	}
	
	vector<int>v1 ={1,2,3,4,5};
	vector<int>v2(10);
	for(int i=0;i<10;i++)
	{
		v2.push_back(i);
	}
	cout<<"\n";
	for(auto x :v2)
	{
		cout<<x<<"\n";
	}
	string a = "hatti";
	string b=a+a;
	cout<<b<<"\n";
	b[5] = 'v';
	cout<<b<<"\n";
	//creating a substring
	string c = b.substr(3,4);
	cout<<c<<"\n";
	
	//set structures 
	set<int>s;
	s.insert(3);
	s.insert(2);
	s.insert(1);
	cout<<"count : "<<s.count(3)<<"\n";
	s.erase(1);
	s.insert(4);
	for(auto x  :s)
	{
		cout<<x<<"\n";
	}
	cout<<"\n";
	set<int> s2= {1,2,3,4,5};
	for(auto x : s2)
	{
		cout<<x<<"\n";
	}
	
	multiset<int> s3;
	s3.insert(5);
	s3.insert(5);
	cout<<"\n";
	for(auto x : s3)
	{
		cout<<x<<"\n";
	}
	s3.erase(5);
	cout<<"\n";
	cout<<s3.count(5)<<"\n";
	for(auto x : s3)
	{
		cout<<x<<"\n";
	}
	cout<<"\n";
	
	map<string,int>m;
	m["monkey"] = 4;
	m["banana"] = 2;
	m["person"] = 1;
	cout<<m["banana"]<<"\n";
	//iterating over a map 
	if(m.count("aybabtu"))
	{
		cout<<"Yes\n";
	}
	else 
	{
		cout<<"No\n";
	}
	if(m.count("monkey"))
	{
		cout<<"Yes\n";
		
	}
	
	//iterating over a map uwing auto in a for loop
	for(auto x : m)
	{
		cout<<x.first<<" "<<x.second<<"\n";
	}
	//iterators and ranges 
	vector<int>v3 ={1,2,3};
	sort(v3.rbegin() , v3.rend());
	cout<<"\n";
	for(auto x : v3)
	{
		cout<<x<<"\n";
	}
	random_shuffle(v3.begin() , v3.end());
	cout<<"Random shuffle : \n";
	for(auto x : v3)
	{
		cout<<x<<"\n";
	}
	
	set<int> s4={1,3,5,7,2,4,6};
	set<int>::iterator it = s4.begin();
	cout<<"Iterator notw points : "<<*it<<"\n";
	cout<<"Printing iterator in a loop : \n";
	for(auto it= s4.begin(); it!=s4.end();it++)
	{
		cout<<*it<<"\n";
	}
	//printing the largest element of a set 
	auto it2 = s4.end();it2--;
	cout<<"largest element : \n";
	cout<<*it2<<"\n";
	
	//finding an element in a set using an iterator 
	int x2 =99;
	auto it3 = s4.find(x2);
	if(it3==s.end())
	{
		cout<<"x not found \n";
	}
	
	//bitset 
	cout<<"bitsets \n";
	bitset<10>b2;
	b2[1]= 1;
	b2[2] = 0;
	cout<<b2[1]<<"\n";
	cout<<b2[2]<<"\n";
	bitset<10> b3(string ("0010011010"));
	//from right to left 
	cout<<b3[4]<<"\n";
	cout<<b3[6]<<"\n";
	bitset<10>b4(string("101011001"));
	cout<<"Counting numer of one's in the string : \n";
	cout<<b4.count()<<"\n";
	
	//deque 
	deque<int>d;
	d.push_back(5);
	d.push_back(12);
	d.push_front(13);
	d.pop_back();
	d.pop_front();
	cout<<"Inside a deque : \n";
	for(auto x : d)
	{
		cout<<x<<"\n";
	}
	
	//stack 
	stack<int>stk;
	stk.push(12);
	cout<<"Stack elements \n";
	stk.push(113);
	cout<<stk.top()<<"\n";
	
	//queue
	cout<<"Printing queue \n";
	queue<int>q;
	q.push(3);
	q.push(12);
	cout<<q.front()<<"\n";
	q.push(14);
	q.pop();
	cout<<q.front()<<"\n";
	
	//priority queue 
	//aready arranges the queue in descending order 
	cout<<"Priority queue : \n";
	priority_queue<int> q2;
	q2.push(12);
	q2.push(14);
	cout<<q2.top()<<"\n";
	q2.pop();
	cout<<q2.top()<<"\n";
	cout<<"vector size : "<<v3.size()<<"\n";
	system("pause");
	return 0;
}