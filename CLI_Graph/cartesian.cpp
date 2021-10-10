#include <iostream>
using namespace std;
int main(){
    char cartesian [30][100]; //creating the grid array
    //filling the grid array [30][100]
    for(int i=0;i<30;i++){
        for(int j=0;j<100;j++){
            cartesian[i][j]='.';//use any char to fill out the array by replacing '<this>'
        }
    }
    //printing the cartesian plane
    for(int i=0;i<30;i++){
        for(int j=0;j<100;j++){
             cout<<cartesian[i][j];
           }
        cout<<endl;
    }
    system("pause");
}