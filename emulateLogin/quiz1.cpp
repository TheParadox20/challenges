#include <iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    // datatypes (int, char, string, double. float, boolean)
    //<datatype> <variableName>;
    //<datatype> <variableName1>,<variableName2>.<variableName3>=value1,value2,value3;
    //<datatype> <variableName> = value;
    int age1,age2;
    cout<<"Enter age1 ";
    cin>>age1;
    cout<<"Enter age2 ";
    cin>>age2;
    if (age1>age2)
    {       cout<<"User 1 is old";
    }else if (age1>100 && age2>100)
    {
        cout<<"TOO OLD!";
    }else
    {
        cout<<"User 2 is old";
    }    
    return 0;
}
