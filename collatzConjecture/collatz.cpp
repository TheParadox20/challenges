#include <iostream>
using namespace std;
int main(){
    cout<<"Enter a positive number: \n";
    int n;
    cin>>n;
    if (n>0)
    {
        do
        {
            cout<<n<<endl;
            if(n%2==0) n/=2;
            else if(n%2!=0) n=n*3+1;
            if(n==1) cout<<n;
        } while (n!=1);
        
    }else cout<<"Not a positive number. Exiting.";
    
}