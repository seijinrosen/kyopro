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

template <typename T1, typename T2>
vector<pair<T1, T2>> zip(const vector<T1> &a, const vector<T2> &b) {
  vector<pair<T1, T2>> ret;
  for (size_t i = 0; i < min(a.size(), b.size()); i++)
    ret.push_back({a[i], b[i]});
  return ret;
}

template <typename T>
vector<pair<T, T>> pairwise(const vector<T> &vec) {
  return zip(vec, my_slice(vec, 1));
}

int main() {
  int N, T;
  cin >> N >> T;

  vector<int> T_LIST(N);
  for (auto &&t : T_LIST) cin >> t;

  int ans = T;
  for (auto &&[a, b] : pairwise(T_LIST)) ans += min(T, b - a);

  print(ans);
}
