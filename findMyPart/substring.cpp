#include <iostream>
using namespace std;
int main(){
    cout<<"Enter search string: \n";
    string search,sub_string;
    cin>>search;
    cout<<"Enter the substring to be searched: \n";
    cin>>sub_string;
    int num=0;
    while (true)
    {
        if(search.find(sub_string)>0 && search.find(sub_string)< 1844551615){
            search.erase(0,search.find(sub_string)+sub_string.size());
            num++;
            continue;          
        }
        break;
    }
    cout<<"Number of occurrences: "<<num;
}