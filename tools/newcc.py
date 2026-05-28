# Copyright (c) 2026 x1nv.
# Licensed under the MIT License.

import sys
from pathlib import Path

LICENSE_HEADER = (
    "// Copyright (c) <YEAR> <COPYRIGHT HOLDER>.\n"
    "// Licensed under the MIT License.\n\n"
)

# generate define guard header
def create_guard_define(filename: str):
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
def create_files(filename: str):
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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Create file failed, Usage: python tools/newcc.py <filename>")
    create_files(sys.argv[1])
