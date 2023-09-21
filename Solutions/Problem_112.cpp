#include <bits/stdc++.h>

using namespace std;
using ll = long long;

bool is_bouncy(int n)
{
  bool is_increasing{true};
  bool is_decreasing{true};
  int prev_digit{-1};
  while (n)
  {
    int digit{n % 10};
    n /= 10;

    if (prev_digit != -1)
    {
      is_increasing &= digit >= prev_digit;
      is_decreasing &= digit <= prev_digit;
    }
    prev_digit = digit;
  }

  return !is_increasing && !is_decreasing;
}

int main()
{
  int bouncy_count{0};
  int cur{1};
  while (1)
  {
    bouncy_count += is_bouncy(cur);
    if (100 * bouncy_count == 99 * cur)
      break;
    ++cur;
  }

  cout << cur << '\n';

  return 0;
}