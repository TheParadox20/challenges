#include <iostream>
using namespace std;
int main(){
    cout<<"Enter the length: \n";
    int length;
    cin>>length;
    //upper level
    for(int upperLevels=0,divison=length-1,x=(2*length-1);upperLevels<length-1;upperLevels++,divison--,x-=2){
        //variable x aids in calculating number of stars
        //variable division used in spacing
        //spaces
        int i=0;
        while(i!=divison){
            cout<<" ";
            i++;
        }
        //stars
        int stars=2*length-x;
        i=0;
        while(i!=stars){
            cout<<"*";
            i++;
        }
        cout<<endl;
    }
    //origin
    for(int origin=0;origin<length*2-1;origin++) cout<<"*";
    cout<<endl;
    //lower level
    /* for(int lowerLevels=0,divisons=1,x=length-1;lowerLevels<length-1;lowerLevels++,divisons++,x+=2){
        //spaces
        int i=0;
        while(i!=divisons){
            cout<<" ";
            i++;
        }
        //stars
        int stars=2*length-x;
        i=0;
        while(i!=stars){
            cout<<"*";
            i++;
        }
        cout<<endl;
    } */
    system("pause");
}