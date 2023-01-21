#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(const vector<T> &vec, string sep = " ") {
  if (vec.empty()) {
    cout << endl;
    return;
  }
  for (size_t i = 0; i < vec.size() - 1; i++) cout << vec.at(i) << sep;
  cout << vec.back() << endl;
}

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int N, P, Q, R, S;
  cin >> N >> P >> Q >> R >> S;
  auto A = input_vector(N);

  vector<int> ans;
  for (int i = 0; i < P - 1; i++) ans.push_back(A[i]);
  for (int i = R - 1; i < S; i++) ans.push_back(A[i]);
  for (int i = Q; i < R - 1; i++) ans.push_back(A[i]);
  for (int i = P - 1; i < Q; i++) ans.push_back(A[i]);
  for (int i = S; i < N; i++) ans.push_back(A[i]);

  print(ans);
}
