#include <stdbool.h>
#include <stdio.h>

typedef long long ll;

static inline bool pisano_period_good(ll n)
{
  register ll a = 1, b = 1;
  register ll res = 1;
  while (a != 0 || b != 1)
  {
    ll temp = b;
    b = (a + b) % n;
    a = temp;
    ++res;
    if (res > 120)
      return false;
  }

  return res == 120;
}

int main()
{
  register ll res = 0;
  for (ll i = 2; i < 1000000000; ++i)
    if (pisano_period_good(i))
      res += i;

  printf("%lli\n", res); // 4m36s

  return 0;
}
