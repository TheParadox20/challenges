#include <iostream>
using namespace std;

int main () {
    double a,b,result;
    char op;
    cout<<"Welcome to the calculator app:\n";
    cout<<"Enter a: ";
    cin>>a;
    cout<<"Enter b: ";
    cin>>b;
    cout<<"Enter the op";
    cin>>op;
    switch (op)
    {
    case '+':
        result=a+b;
        break;
    case    '-':
        result=a-b;
        break;
    case '*':
        result=a*b;
        break;
    case '/':
        result=a/b;
        break;
    default:
        cout<<"Wrong operator:";
        result=0;
        break;
    }
    cout<<a<<" "<<op<<" "<<b<<" = "<<result;
    return 0;    
}