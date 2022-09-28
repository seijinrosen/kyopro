#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

string yes_no(bool b) { return b ? "Yes" : "No"; }

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int N;
  cin >> N;
  auto A = input_vector(N);
  for (auto &&a : A) a--;

  vector<bool> bucket(N, false);

  bool ans = true;
  for (auto &&a : A) {
    if (bucket[a]) {
      ans = false;
      break;
    }
    bucket[a] = true;
  }

  print(yes_no(ans));
}
