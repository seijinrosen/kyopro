#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

template <typename P, typename T>
bool all(P pred, const vector<T> &vec) {
  return all_of(vec.begin(), vec.end(), pred);
}

bool even(int n) { return n % 2 == 0; }

template <typename P, typename T>
vector<T> filter(P pred, const vector<T> &vec) {
  vector<T> ret;
  for (auto &&x : vec)
    if (pred(x)) ret.push_back(x);
  return ret;
}

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int main() {
  int N;
  cin >> N;
  auto A = input_vector(N);

  auto ans =
      all([](int a) { return a % 3 == 0 || a % 5 == 0; }, filter(even, A));

  print(ans ? "APPROVED" : "DENIED");
}
