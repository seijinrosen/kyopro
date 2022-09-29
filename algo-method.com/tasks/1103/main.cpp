#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
}

template <typename T>
vector<T> my_slice(const vector<T> &vec, int start, int stop = -1) {
  return {vec.begin() + start, stop == -1 ? vec.end() : vec.begin() + stop};
}

vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}

int N, K;
vector<int> X;

bool func(int min_dist) {
  int k = 1;
  int now = X[0];
  for (auto &&x : my_slice(X, 1)) {
    if (min_dist <= x - now) {
      if (++k == K) return true;
      now = x;
    }
  }
  return false;
}

int main() {
  cin >> N >> K;
  X = input_vector(N);

  int lo = 1;
  int hi = X[N - 1];

  while (hi - lo > 1) {
    int mid = (hi + lo) / 2;
    if (func(mid))
      lo = mid;
    else
      hi = mid;
  }

  int ans = lo;
  print(ans);
}
