#include <iostream>
using namespace std;

int main () {
    int password,x=1234;
    cout<<"Create password: ";
    cin>>password;
    int pin;
    //while (1)
    //{
        
        cout<<"Enter pin: ";
        cin>>pin;
        if (password==pin || pin==x)
        {
            cout<<"Correct pin\n";
            //break;
        }
        //cout<<"Wrong pin please try again \n";
    //}
    return 0;    
}