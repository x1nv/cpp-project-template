# Copyright (c) 2026 x1nv.
# Licensed under the MIT License.

import os
import re
import sys
from pathlib import Path

LICENSE_HEADER = (
    "// Copyright (c) <YEAR> <COPYRIGHT HOLDER>.\n"
    "// Licensed under the MIT License.\n\n"
)

# generate define guard header
def create_guard_define(filename):
    project_name = Path.cwd().name.upper().replace("-", "_")
    path = Path(filename)

    # ignore /src/
    parts = list(path.with_suffix("").parts)
    if 'src' in parts:
        parts = parts[parts.index('src') + 1:]
    processed_parts = [p.replace("-", "_").upper() for p in parts]
    path_prefix = "_".join(processed_parts)

    guard_name = f"{project_name}_{path_prefix}_H_"
    return (
        f"#ifndef {guard_name}\n"
        f"#define {guard_name}\n"
        "\n\n\n"
        f"#endif  // {guard_name}\n"
    )

# create .cc and .h files
def create_files(filename):
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    h_path = path.parent / f"{path.name}.h"
    cc_path = path.parent / f"{path.name}.cc"
    with open(h_path, "w") as f:
        f.write(LICENSE_HEADER)
        f.write(f"{create_guard_define(filename)}")
    with open(cc_path, "w") as f:
        f.write(LICENSE_HEADER)
        f.write(f"#include \"{path.name}.h\"")

# find BUILD
def find_build_file(filename):
    project_root = Path.cwd().absolute()
    current = Path(filename).absolute()
    while current != current.parent:
        if (current / "BUILD").is_file():
            return current / "BUILD"
        if current == project_root:
            raise FileNotFoundError(f"BUILD not found")
        current = current.parent

# add 'load("@rules_cc//cc:cc_library.bzl", "cc_library")' to BUILD
def add_load_cc_library(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    load_statement = 'load("@rules_cc//cc:cc_library.bzl", "cc_library")'
    if load_statement not in content:
        content = f"{load_statement}\n" + content
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def find_substr(content, substr, flags = 0) -> int:
    match = re.search(substr, content, flags)
    if not match:
        raise ValueError(f"not found content: '{substr}'")
    return match

def calculate_relative_path(parent_path, file_path) -> str:
    abs_parent_dir = Path(parent_path).absolute().parent
    abs_file_path = Path(file_path).absolute()
    relative_path = abs_file_path.relative_to(abs_parent_dir)
    return str(relative_path).replace(os.sep, "/")

# add cc_library to BUILD
def add_cc_library(build_path, filename):
    with open(build_path, "r", encoding="utf-8") as f:
        content = f.read()

    # for BUILD to .h and .cc
    relative_path = calculate_relative_path(build_path, filename)

    # insert this cc_library before the cc_binary
    insert_pos = find_substr(content, r"cc_binary\(").start()
    cc_library_rule = (
        f"cc_library(\n"
        f"    name = \"{Path(filename).name}\",\n"
        f"    hdrs = [\"{relative_path}.h\"],\n"
        f"    srcs = [\"{relative_path}.cc\"],\n"
        f")\n\n"
    )
    content = content[:insert_pos] + cc_library_rule + content[insert_pos:]

    with open(build_path, "w", encoding="utf-8") as f:
        f.write(content)

# insert new cc_library into cc_binary
def apply_cc_library(build_path, filename):
    with open(build_path, "r", encoding="utf-8") as f:
        content = f.read()

    # find 'deps = [' on cc_binary
    insert_pos = find_substr(content, r"cc_binary.*?deps.*?\[",  re.DOTALL).end()
    content = content[:insert_pos] + f'\n        ":{Path(filename).name}", ' + content[insert_pos:]

    with open(build_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Create file failed, Usage: python tools/newcc.py <filename>")
    create_files(sys.argv[1])
    build_path = find_build_file(sys.argv[1])

    # ask user whether to automatically add cc_library to BUILD (case-insensitive)
    print(f"Automatically identified BUILD file path: {build_path}")
    answer = input("Do you want to automatically add cc_library to BUILD file? (y/n): ").strip().lower()
    if answer in ('y', 'yes'):
        add_load_cc_library(build_path)
        add_cc_library(build_path, sys.argv[1])
        apply_cc_library(build_path, sys.argv[1])
    else:
        print("Skipped automatic BUILD modification. Files created but not added to BUILD.")
    print("Created successfully")
