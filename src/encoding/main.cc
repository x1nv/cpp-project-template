// Copyright (c) <YEAR> <COPYRIGHT HOLDER>.
// Licensed under the MIT License.

#ifdef _DEBUG
#include <crtdbg.h>
#endif  // _DEBUG

#include <print>

#include "absl/strings/str_cat.h"
#include "say_hello.h"

int main() {
  // check heap memory leak
#ifdef _DEBUG
  _CrtSetDbgFlag(_CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF);
#endif

  // set utf-8 character sets
  // ...

  std::string message = absl::StrCat("hello", " world!");
  std::println("Welcome to this C++ project template!");
  std::println("{}", message);
  hello();

  return 0;
}
