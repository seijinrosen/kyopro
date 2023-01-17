#include <bits/stdc++.h>
using namespace std;

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int N, K;
  cin >> N >> K;

  set<int> st;

  for (size_t _ = 0; _ < K; _++) {
    int d;
    cin >> d;
    auto A = input_vector(d);

    for (auto &&a : A) st.insert(a);
  }

  int ans = N - st.size();

  cout << ans << endl;
}
