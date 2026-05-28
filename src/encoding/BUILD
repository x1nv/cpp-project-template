load("@rules_cc//cc:cc_binary.bzl", "cc_binary")

cc_binary(
    name = "encoding",
    srcs = glob(["*.cc", "*.h"]),
    deps = [
        "@mimalloc//:mimalloc",
        "@abseil-cpp//absl/strings"
    ],
)
