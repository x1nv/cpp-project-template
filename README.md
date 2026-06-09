# C++ Project Template

Writing a Google-style LLVM C++ project template with Bazel using VS Code on Windows.

## You need change template files

| File | Config |
| --- | --- |
| LICENSE | `<YEAR>` and `<COPYRIGHT HOLDER>` |
| .cc/.h files | `<YEAR>` and `<COPYRIGHT HOLDER>` |
| release_version.yml | `<YEAR>` and `<COPYRIGHT HOLDER>` |
| .clangd | `/std:` default is `c++23preview` |
| BUILD | change linker configs |
| .bazelrc | compilation options, default is clang-cl.exe configs |
| .vscode/tasks.json | definition of how to compile |
| release_version.yml | custom release workflow |

## You need install compile environment

- Visual Studio
- VSCode
- Node.js
- Python
- LLVM
- Bazel

## You need install VSCode Extension

- C/C++
- clangd
- Bazel
- Clang-Format
- EditorConfig

## Project Directory Structure

> [!WARNING]
> Before importing any library, you must verify that it supports your project's current C++ standard to avoid introducing elusive, low-level bugs.

**External dependencies are typically managed via Bazel.**

```text
Project/
├── MODULE.bazel
├── ICENSE
├── src/                       # source code for internal implementation
│   └── encoding/              # example module directory
│       ├── BUILD
│       ├── base85.cc
│       ├── base85.h
│       └── base85_test.cc
├── include/                   # public headers and exported interfaces
└── third_party/               # local external libraries/dependencies
```

## How use this C/C++ project template

Windows **PowerShell** input:

```bash
cd E:\                                    # your local disk letter
gh repo create <MY NEW PROJECT> --template "x1nv/cpp-project-template" --public --clone
cd <MY NEW PROJECT>
npm install                               # for install Commitizen to Git commit
pip install pre-commit                    # if not previously installed
pre-commit install                        # install pre-commit hook
pre-commit install --hook-type commit-msg # install commit-msg hook
code .                                    # launch vscode
```

## Hot use Commitizen to Git commit

```bash
git add .
npx cz
```

## Quickly create .h/.cc files

```bash
python3 tools/newcc.py <filename> # Example: python3 tools/newcc.py src/encoding/failed_exit
```

## VSCode Code Snippets

This project includes custom C++ code snippets in `.vscode/cpp.code-snippets`. Type the prefix in a `.cc`/`.h` file and press `Tab` or `Enter` to expand.

| Prefix | Description |
| --- | --- |
| `newclass` | Create a `final` class with deleted copy constructor/assignment |
| `nspace` | Create a Google-style namespace block with closing comment |
