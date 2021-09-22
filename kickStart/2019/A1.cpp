#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int testCase, N, P,hours;
    cin >> testCase; // read number of test cases
    for (int i = 1; i <= testCase; ++i) {
        cin >> N >> P; // read Number of students and then students per team.
        vector <int> S;
        int skill;
        for(int j=0;j<N;j++){
            cin>>skill;
            S.push_back(skill);
        }
        //cout<<"vector element at index 2: "<<S[2];
        sort(S.begin(),S.end());
        int highestSkill = S[P-1];
        //cout<<"Highest skill: "<<highestSkill<<endl;
        for(int k=0;k<P-1;k++){
            hours+=highestSkill-S[k];
            //cout<<highestSkill-S[k]<<endl;
        }
        cout << "Case #" << i << ": " <<hours<< endl;
        // cout knows that n + m and n * m are ints, and prints them accordingly.
        // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    }
    return 0;
}