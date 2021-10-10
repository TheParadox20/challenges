#include <iostream>
using namespace std;
int main(){
    cout<<"Enter the string: \n";
    string input,final="";
    cin>>input;
    for(int i=0;i<input.size();i++){
        char current;
        if (isupper(input[i])) current= tolower(input[i]);
        else if (islower(input[i])) current = toupper(input[i]);
        else current=input[i];
        final+=current;
    }
    cout<<final;
}