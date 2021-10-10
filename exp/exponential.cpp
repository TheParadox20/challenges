#include <iostream>
using namespace std;
int power(int x, int y){
    int omega =x;
    for (int i = 0; i < y-1; i++){
        omega*=x;
    }
    return omega;
}
int main()
{
    cout<<power(5,3);
    return 0;
}
