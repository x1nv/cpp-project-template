// Copyright (c) <YEAR> <COPYRIGHT HOLDER>.
// Licensed under the MIT License.

#ifdef _DEBUG
#include <crtdbg.h>
#endif  // _DEBUG
#define WIN32_LEAN_AND_MEAN
#include <windows.h>

#include <print>
#include <string>

#include "absl/strings/str_cat.h"
#include "src/encoding/say_hello.h"

namespace {

void SetUtf8ConsoleOutput() {
  SetConsoleOutputCP(CP_UTF8);
  SetConsoleCP(CP_UTF8);
}

}  // namespace

int main() {
  // Check heap memory leak.
#ifdef _DEBUG
  _CrtSetDbgFlag(_CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF);
#endif

  // Set utf-8 character sets.
  // Otherwise, printf will display Chinese characters as garbled text.
  SetUtf8ConsoleOutput();

  std::println("你好, 世界");
  std::string message = absl::StrCat("hello", " world!");
  std::println("Welcome to this C++ project template!");
  std::println("{}", message);
  hello();
  system("pause");

  return 0;
}
