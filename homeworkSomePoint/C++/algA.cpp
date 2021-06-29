#include <iostream>
using namespace std;
int main(){
    //display welcoming statement
    cout<<"Welcome to the Homework Point Sum program!"<<endl<<"How many assignments did you complete?: "<<endl;
    //define a variable named assignmenents to be used for conditioning the for loop
    int assignments;
    //the variable is assigned by the user through the terminal
    cin>>assignments;
    //a variable named sum is initialized
    double sum=0;
    for (int i = 1; i <= assignments; i++)
    /*
        This loop iterates depending on the number of times the number of assignments to be input
        During each iteration a variable score is created and assigned a value by the user
        The variable sum is then updated by adding the score
    */
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
    //the average is obtained and if it is less than 33 that is a fail
    // the statement fail is printed
    if ((sum/assignments)<33)
    {
        cout<<"Fail";
    }    
    return 0;
}