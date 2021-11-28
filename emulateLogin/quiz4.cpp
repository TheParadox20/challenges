#include <iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    string user1 = "brenda",user2 = "sam",user3 = "felicia",user4 = "siz",user5 = "abner", pass1="tiktok",pass2="coder",pass3="instagram",pass4="salsa",pass5="games";
    string username,password;
    cout<<"Enter your username: ";
    while (true)
    {
        cin>>username;
        if (username!=user1 && username!=user2 && username!=user3 && username!=user4 && username!=user5)
        {
            cout<<"User "<<username<<" doesn't exist\n"<<"Enter valid username: ";
        }else
        {
            break;
        }
        
    }
    
    while (true)
    {
        cout<<"Enter password for "<<username<<": ";
        cin>>password;
        if (username==user1 && password==pass1)
        {
            cout<<"You logged in as "<<username;
            break;
        }
        else if (username==user2 && password==pass2)
        {
            cout<<"You logged in as "<<username;
            break;
        }
        else if (username==user3 && password==pass3)
        {
            cout<<"You logged in as "<<username;
            break;
        }
        else if (username==user4 && password==pass4)
        {
            cout<<"You logged in as "<<username;
            break;
        }
        else if (username==user5 && password==pass5)
        {
            cout<<"You logged in as "<<username;
            break;
        }
        else
        {
            cout<<"Wrong password for user "<<username<<"\n\t-------------\n\t| Try again |\n\t-------------\n";
        }
    }
        
    return 0;
}
