#include <iostream>

#if defined(FOO)
#include "foo.h"
#else
#include "bar.h"  // USE BAR
#endif

int main() {
#if defined(FOO)
  int answer = foo();
  std::cout << "Foo enabled, the answer is " << answer << std::endl;
#else
  int answer = bar();
  std::cout << "Bar enabled, the answer is " << answer << std::endl;
#endif
  return 0;
}
