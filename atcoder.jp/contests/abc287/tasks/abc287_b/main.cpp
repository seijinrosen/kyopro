#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, M;
  cin >> N >> M;
  vector<string> S(N), T(M);
  for (auto &&v : S) cin >> v;
  for (auto &&v : T) cin >> v;

  set<string> st = {T.begin(), T.end()};

  int ans = 0;
  for (auto &&s : S)
    if (st.count(s.substr(3))) ans++;

  cout << ans << endl;
}
