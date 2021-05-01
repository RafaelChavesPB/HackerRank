#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, num, ans = 0;
    vector<int> socks(101, 0);
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> num;
        socks[num]++;
    }
    for (auto it : socks)
        ans += it / 2;
    cout<<ans<<endl;
    return 0;
}