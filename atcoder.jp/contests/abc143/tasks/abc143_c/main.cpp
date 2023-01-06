#include <bits/stdc++.h>
using namespace std;

string dedup(const string &s) {
  string result = s;
  result.erase(unique(result.begin(), result.end()), result.end());
  return result;
}

int main() {
  int N;
  string S;
  cin >> N >> S;

  int ans = dedup(S).size();

  cout << ans << endl;
}
