#include<iostream>
#include<string>
#include<cmath>
#include<math.h>
using namespace std;


void permute(string , string);
int squares(int);
int cubes(int);
int array_sum(int[],int);
int ex_2(int);
int ex_3(int);
int ex_8(int[] , int );
int summation(int);
int reversing(int);

int main_1()
{
    /*string s ;
    string answer = "";
    cout<<"\nEnter a string : ";
    cin>>s;
    cout<<"\nAll the possible strings are : ";
    permute(s , answer);*/
    cout<<"\nEnter a number : ";
    int n;
    cin>>n;
    cout<<"\nSquare of that number : "<<pow(n,2);
    cout<<"\nSum of squares of numbers till n : "<<squares(n);
    cout<<"\nSum of cubes till n numbers : "<<cubes(n);
    int m=4;
    cout<<"\n\nSolution ex_2() : "<<"\n"<<ex_2(m);
    int j=7;
    //cout<<"\n\nSolution of ex_3() : "<<ex_3(j);
    int array[] = {1,3,5};
    cout<<"\nArray sum : "<<ex_8(array , 2);
    cout<<"\nEnter a number : ";
    int k;
    cin>>k;
    cout<<"\nSummation of the digits of the digits of the number is : "<<summation(k);
    cout<<"\nReversing the digits of the number : "<<reversing(k);

    return 0;
}

void permute(string s ,string answer )
{
    if(s.length()==0)
    {
        cout<<"\n"<<answer<<" ";
        return;
    }
    for (int i=0;i<s.length();i++)
    {
        char ch = s[i];
        string left_substring = s.substr(0,i);
        cout<<"\nleft substring : "<<left_substring;
        string right_substring = s.substr(i+1);
        cout<<"\nright substring : "<<right_substring;
        string rest = left_substring + right_substring;
        cout<<"\nrest : "<<rest;
        permute(rest, answer+ch);
    }
}

int squares(int n)
{
    if (n==1)
    {
        return n;
    }
    else
    {
        return pow(n,2) + squares(n-1);
    }
}

int cubes(int n)
{
    if(n==1)
    {
        return n;
    }
    else
    {
        return pow(n,3) + cubes(n-1);
    }
}

int ex_2(int m)
{
    cout<<"\nm : "<<m;
    if(m==0)
    {
        return 0;
    }
    else
    {
        return 3 + ex_2(m-1);
    }
}

int ex_3(int n)
{
    if(n==0)
    {
        return 0;
    }
    else
    {
        return ex_3(n-1) + ex_3(n-2);
    }
}

int ex_8(int a[] , int s)
{
    if(s==0)
    {
        return a[0];
    }
    else
    {
        return (a[s] + ex_8(a , s-1));
    }

}

int summation(int n)
{
    cout<<"\nn : "<<n;
    if(n<10)
    {
        return n;
    }
    else
    {
        return summation(floor(n/10)) + (n%10);
    }
}

int reversing(int n)
{
    if(n<10)
    {
        return n;
    }
    else
    {
        cout<<n%10;
        return reversing(floor(n/10));
    }
}

