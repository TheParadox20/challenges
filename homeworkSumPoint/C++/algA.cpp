#include <iostream>
using namespace std;
int main(){
    cout<<"Welcome to the Homework Point Sum program!"<<endl<<"How many assignments did you complete?: "<<endl;
    int assignments;
    cin>>assignments;
    double sum=0;
    for (int i = 1; i <= assignments; i++)
   
    {
        cout<<"Enter score "<<i<<": "<<endl;
        double score;
        cin>>score;
        sum+=score;
    }
    if (sum>0)
    {
        cout<<"Homework point sum is "<<sum<<endl;
    }
   
    if ((sum/assignments)<33)
    {
        cout<<"Fail";
    }    
    return 0;
}