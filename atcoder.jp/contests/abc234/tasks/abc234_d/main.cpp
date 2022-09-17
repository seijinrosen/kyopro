#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

template <typename T>
void print(vector<T> &vec, string sep = " ") {
  if (vec.empty()) {
    cout << endl;
    return;
  }
  for (size_t i = 0; i < vec.size() - 1; i++) cout << vec.at(i) << sep;
  cout << vec.back() << endl;
}

int main() {
  int N, K;
  cin >> N >> K;

  vector<int> P(N);
  for (auto &&p : P) cin >> p;

  vector<bool> bucket(N + 1);
  rep(i, K) bucket[P[i]] = true;

  int idx = 0;
  while (!bucket[idx]) idx++;

  vector<int> ans_vec = {idx};

  for (int i = K; i < N; i++) {
    if (idx < P[i]) {
      idx++;
      bucket[P[i]] = true;
      while (!bucket[idx]) idx++;
    }
    ans_vec.push_back(idx);
  }

  print(ans_vec, "\n");
}
