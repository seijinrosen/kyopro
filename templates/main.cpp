#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = long long;

const string ascii_lowercase = "abcdefghijklmnopqrstuvwxyz";

// print functions -------------------------------------------------------------
template <typename T>
void print(T value) {
  cout << value << endl;
}
template <typename T1, typename T2>
void print(const pair<T1, T2> &p) {
  cout << p.first << " " << p.second << endl;
}
template <typename T1, typename T2, typename T3>
void print(const tuple<T1, T2, T3> &t) {
  cout << get<0>(t) << " " << get<1>(t) << " " << get<2>(t) << endl;
}
template <typename T>
void print(const vector<T> &vec, string sep = " ") {
  if (vec.empty()) {
    cout << endl;
    return;
  }
  for (size_t i = 0; i < vec.size() - 1; i++) cout << vec.at(i) << sep;
  cout << vec.back() << endl;
}
// print functions -------------------------------------------------------------

template <typename T>
map<T, int> Counter(vector<T> &vec) {
  map<T, int> counter;
  for (auto &&t : vec) counter[t]++;
  return counter;
}

vector<int> accumulate(const vector<int> &vec) {
  size_t n = vec.size();
  vector<int> acc(n + 1);
  for (size_t i = 0; i < n; i++) acc[i + 1] = acc[i] + vec[i];
  return acc;
}

vector<int> accumulate_max(const vector<int> &vec) {
  size_t n = vec.size();
  vector<int> acc(n);
  acc[0] = vec[0];
  for (size_t i = 1; i < n; i++) acc[i] = max(acc[i - 1], vec[i]);
  return acc;
}

template <typename P, typename T>
bool all(P pred, const vector<T> &vec) {
  return all_of(vec.begin(), vec.end(), pred);
}

template <typename T>
vector<tuple<T, T, T>> combinations3(const vector<T> &vec) {
  size_t n = vec.size();
  vector<tuple<T, T, T>> ret;
  for (size_t i = 0; i < n - 2; i++)
    for (size_t j = i + 1; j < n - 1; j++)
      for (size_t k = j + 1; k < n; k++)
        ret.push_back({vec[i], vec[j], vec[k]});
  return ret;
}

int count(char x, const string &s) { return count(s.begin(), s.end(), x); }

template <typename T>
set<T> difference(const set<T> &set_a, const set<T> &set_b) {
  set<T> result;
  set_difference(set_a.begin(), set_a.end(), set_b.begin(), set_b.end(),
                 inserter(result, result.end()));
  return result;
}

template <typename T>
bool elem(T value, const vector<T> &vec) {
  for (auto &&x : vec)
    if (x == value) return true;
  return false;
}

vector<pair<char, int>> run_length_encoding(const string &str) {
  vector<pair<char, int>> ret = {{str[0], 1}};
  for (auto &&c : str.substr(1)) {
    if (c == ret.back().first)
      ret.back().second++;
    else
      ret.push_back({c, 1});
  }
  return ret;
}

int ctoi(char c) { return c - '0'; }

template <typename T>
vector<pair<int, T>> enumerate(const vector<T> &vec) {
  vector<pair<int, T>> ret(vec.size());
  for (size_t i = 0; i < vec.size(); i++) ret[i] = {i, vec[i]};
  return ret;
}
vector<pair<int, char>> enumerate(const string &s) {
  vector<pair<int, char>> ret(s.size());
  for (size_t i = 0; i < s.size(); i++) ret[i] = {i, s[i]};
  return ret;
}

bool even(int n) { return n % 2 == 0; }

template <typename P, typename T>
vector<T> filter(P pred, const vector<T> &vec) {
  vector<T> ret;
  for (auto &&x : vec)
    if (pred(x)) ret.push_back(x);
  return ret;
}

template <typename T>
T head(const set<T> &st) {
  return *st.begin();
}

string int2bin(int number, int width) {
  string ret(width, '0');
  for (size_t i = 0; i < width; i++)
    if (number & 1 << i) ret[i] = '1';
  return {ret.rbegin(), ret.rend()};
}

bool odd(int n) { return n % 2 == 1; }

string my_slice(string &s, int start, int stop) {
  return s.substr(start, stop - start);
}
template <typename T>
vector<T> my_slice(const vector<T> &vec, int start, int stop = -1) {
  return {vec.begin() + start, stop == -1 ? vec.end() : vec.begin() + stop};
}

template <typename K, typename V>
map<K, V> new_map(const vector<pair<K, V>> &vec) {
  return {vec.begin(), vec.end()};
}

template <typename T>
set<T> new_set(const vector<T> &vec) {
  return {vec.begin(), vec.end()};
}

template <typename T>
vector<pair<T, T>> pairwise(const vector<T> &vec) {
  size_t n = vec.size() - 1;
  vector<pair<T, T>> ret(n);
  for (size_t i = 0; i < n; i++) ret[i] = {vec[i], vec[i + 1]};
  return ret;
}

int int2bin(const string &bin) {
  string reversed = {bin.rbegin(), bin.rend()};
  int ret = 0;
  for (size_t i = 0; i < bin.size(); i++)
    if (reversed[i] == '1') ret += 1 << i;
  return ret;
}

map<int, int> prime_factorize(int n) {
  map<int, int> counter;
  int p = 2;
  while (p * p <= n) {
    int e = 0;
    while (n % p == 0) {
      e++;
      n /= p;
    }
    if (e != 0) counter[p] = e;
    p++;
  }
  if (n != 1) counter[n] = 1;
  return counter;
}

vector<int> range(int stop) {
  vector<int> ret(stop);
  iota(ret.begin(), ret.end(), 0);
  return ret;
}
vector<int> range(int start, int stop) {
  vector<int> ret(stop - start);
  iota(ret.begin(), ret.end(), start);
  return ret;
}

string repeat(const string &s, int n) {
  string ret;
  for (size_t i = 0; i < n; i++) ret += s;
  return ret;
}

string reverse(const string &s) { return {s.rbegin(), s.rend()}; }

template <typename T>
vector<T> sort(const vector<T> &vec, bool reverse = false) {
  vector<T> ret = {vec.begin(), vec.end()};
  if (reverse)
    sort(ret.begin(), ret.end(), greater());
  else
    sort(ret.begin(), ret.end());
  return ret;
}

vector<string> split(char x, const string &s) {
  vector<string> ret;
  string now = "";
  for (auto &&c : s) {
    if (c == x) {
      ret.push_back(now);
      now = "";
    } else {
      now += c;
    }
  }
  if (!now.empty()) ret.push_back(now);
  return ret;
}

bool is_prefix(const string &prefix, const string &s) {
  if (s.size() < prefix.size()) return false;
  return s.substr(0, prefix.size()) == prefix;
}

template <typename T>
vector<T> step2(const vector<T> &vec) {
  vector<T> ret;
  for (size_t i = 0; i < vec.size(); i++)
    if (i % 2 == 0) ret.push_back(vec[i]);
  return ret;
}

template <typename T>
T sum(const vector<T> &vec) {
  return accumulate(vec.begin(), vec.end(), 0.0);
}

int sum_of_each_digit(int i) {
  int ret = 0;
  for (auto &&c : to_string(i)) ret += c - '0';
  return ret;
}

template <typename T>
vector<T> tail(const vector<T> &vec) {
  return {vec.begin() + 1, vec.end()};
}

vector<string> tails(const string &str) {
  vector<string> ret(str.size() + 1);
  for (size_t i = 0; i <= str.size(); i++) ret[i] = str.substr(i);
  return ret;
}

string take(int n, const string &s) { return s.substr(0, n); }
template <typename T>
vector<T> take(int n, const vector<T> &vec) {
  return {vec.begin(), vec.begin() + n};
}

string yes_no(bool b) { return b ? "Yes" : "No"; }

vector<pair<char, char>> zip(const string &a, const string &b) {
  size_t n = min(a.size(), b.size());
  vector<pair<char, char>> ret(n);
  for (size_t i = 0; i < n; i++) ret[i] = {a[i], b[i]};
  return ret;
}
template <typename T1, typename T2>
vector<pair<T1, T2>> zip(const vector<T1> &a, const vector<T2> &b) {
  size_t n = min(a.size(), b.size());
  vector<pair<T1, T2>> ret(n);
  for (size_t i = 0; i < n; i++) ret[i] = {a[i], b[i]};
  return ret;
}

// input functions -------------------------------------------------------------
vector<int> input_vector(int n) {
  vector<int> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}
template <typename T>
vector<T> input_vector(int n) {
  vector<T> ret(n);
  for (auto &&i : ret) cin >> i;
  return ret;
}
using Pair = pair<int, int>;
vector<Pair> input_pair_vector(int n) {
  vector<Pair> ret(n);
  for (auto &&[a, b] : ret) cin >> a >> b;
  return ret;
}
using Tuple = tuple<int, int, int>;
vector<Tuple> input_tuple_vector(int n) {
  vector<Tuple> ret(n);
  for (auto &&[a, b, c] : ret) cin >> a >> b >> c;
  return ret;
}
// input functions -------------------------------------------------------------

int main() {
  int N;
  cin >> N;
}
