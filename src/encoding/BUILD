load("@rules_cc//cc:cc_binary.bzl", "cc_binary")
load("@rules_cc//cc:cc_library.bzl", "cc_library")

cc_library(
    name = "say_hello",
    hdrs = ["say_hello.h"],
    srcs =  ["say_hello.cc"],
)

cc_binary(
    name = "encoding",
    srcs = ["main.cc"],
    deps = [
        ":say_hello",
        "@mimalloc//:mimalloc",
        "@abseil-cpp//absl/strings"
    ],
)
