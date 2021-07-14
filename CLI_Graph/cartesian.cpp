#include <iostream>
using namespace std;
int main(){
    char cartesian [6][18]; //creating the grid array
    //filling the grid array
    for(int i=0;i<6;i++){
        for(int j=0;j<18;j++){
            cartesian[i][j]='.';//use any char to fill out the array by replacing '<this>'
        }
    }
    //printing the cartesian plane
    for(int i=0;i<6;i++){
        if(i!=5){
           for(int j=0;j<1;j++){
             cout<<cartesian[i][j];
           }
        }else{
            for(int j=0;j<18;j++){
              cout<<cartesian[i][j];
            }
        }
        cout<<endl;
    }
    system("pause");
}