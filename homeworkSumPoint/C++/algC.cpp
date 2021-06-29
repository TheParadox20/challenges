#include <iostream>
using namespace std;
int main(){
    //display welcoming statement
    cout<<"Welcome to the Homework Point Sum program!"<<endl;
    //initialize the variables assignments and score to be used in the loop
    double assignments=0;
    double score =0;
    while (true)
    /*
        the while loop created is an indefinate one and it only exits when a certain condition is evaluated
    */
    {
        cout<<"Do you want to enter a homework score? ('yes' or 'no')"<<endl;
        string user_input;
        cin>>user_input;
        if (user_input=="yes")
        {
            cout<<"Enter score: \n";
            double user_input;
            cin>>user_input;
            score+=user_input;
            assignments++;
        }else if (user_input=="no") // exit loop condition
        {
            break;
        }else{
            cout<<"Unrecognized entry! Please try again. \n";
        }
    }
    if(score>0) cout<<"Homework point sum is "<<score<<endl;
    //the average is obtained and if it is less than 33 that is a fail
    // the string fail is assigned to a variable grade using a ternary operator
    string grade = (score/assignments)<33?"Fail":"";
    cout<<grade;
    return 0;
}