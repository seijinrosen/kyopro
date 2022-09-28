#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(T value) {
  cout << value << endl;
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

  int current_max = 0;
  int current_max_count = 0;

  for (auto &&a : A) {
    if (a == current_max) {
      current_max_count++;
    } else if (current_max < a) {
      current_max = a;
      current_max_count = 1;
    }

    print(current_max_count);
  }
}
