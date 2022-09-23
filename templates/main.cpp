#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = long long;

template <typename T>
void print(T value) {
  cout << value << endl;
}
template <typename T>
void print(vector<T> &vec, string sep = " ") {
  if (vec.empty()) {
    cout << endl;
    return;
  }
  for (size_t i = 0; i < vec.size() - 1; i++) cout << vec.at(i) << sep;
  cout << vec.back() << endl;
}

template <typename T>
map<T, int> Counter(vector<T> &vec) {
  map<T, int> counter;
  for (auto &&t : vec) counter[t]++;
  return counter;
}

int bin2int(const string &bin) {
  int ret = 0;
  for (auto &&[i, c] : enumerate(reverse(bin)))
    if (c == '1') ret += 1 << i;
  return ret;
}

vector<pair<int, char>> enumerate(const string &s) {
  vector<pair<int, char>> ret(s.size());
  for (size_t i = 0; i < s.size(); i++) ret[i] = {i, s[i]};
  return ret;
}

string my_slice(string &s, int start, int stop) {
  return s.substr(start, stop - start);
}
template <typename T>
vector<T> my_slice(const vector<T> &vec, int start, int stop = -1) {
  return {vec.begin() + start, stop == -1 ? vec.end() : vec.begin() + stop};
}

template <typename T>
vector<pair<T, T>> pairwise(const vector<T> &vec) {
  return zip(vec, my_slice(vec, 1));
}

string reverse(const string &s) { return string(s.rbegin(), s.rend()); }

template <typename T>
T sum(vector<T> &vec) {
  return accumulate(vec.begin(), vec.end(), 0.0);
}

string yes_no(bool b) { return b ? "Yes" : "No"; }

template <typename T1, typename T2>
vector<pair<T1, T2>> zip(const vector<T1> &a, const vector<T2> &b) {
  vector<pair<T1, T2>> ret;
  for (size_t i = 0; i < min(a.size(), b.size()); i++)
    ret.push_back({a[i], b[i]});
  return ret;
}

int main() {
  int N;
  cin >> N;
}
