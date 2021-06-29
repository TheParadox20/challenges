#include <iostream>
using namespace std;
int main(){
    //display welcoming statement
    cout<<"Welcome to the Homework Point Sum program!"<<endl;
    //initialize the variables assignments, itterations and score to be used in the loop
    double sum=0;
    int assignments=0;
    int itterations=0;
    while (true)
    /*
        the while loop created is an indefinate one and it only exits when a certain condition is evaluated
    */
    {
        cout<<"Enter a homework score, or -1 to quit:"<<endl;
        double score;
        cin>>score;
        if(score<0){ //exit loop condion
            break;
        }
        sum+=score;
        //the variable assignments counts the number of assignments enterd
        assignments++;
        //the variable itterations counts the number of times the loop loops
        itterations++;
    }
    if (itterations>0)
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