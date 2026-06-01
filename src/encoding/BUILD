load("@rules_cc//cc:cc_binary.bzl", "cc_binary")
load("@rules_cc//cc:cc_library.bzl", "cc_library")

cc_library(
    name = "say_hello",
    srcs = ["say_hello.cc"],
    hdrs = ["say_hello.h"],
)

cc_binary(
    name = "main",
    srcs = ["main.cc"],
    malloc = "@mimalloc",
    deps = [
        ":say_hello",
        "@abseil-cpp//absl/strings",
    ],
)
