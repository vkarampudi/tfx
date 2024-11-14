workspace(name = "tfx")

# To update TensorFlow to a new revision.
# TODO(b/177694034): Follow the new format for tensorflow import.
# 1. Update the '_TENSORFLOW_GIT_COMMIT' var below to include the new git hash.
# 2. Get the sha256 hash of the archive with a command such as...
#    curl -L https://github.com/tensorflow/tensorflow/archive/<git hash>.tar.gz | sha256sum
#    and update the 'sha256' arg with the result.
# 3. Request the new archive to be mirrored on mirror.bazel.build for more
#    reliable downloads.

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# TF 1.15
# LINT.IfChange(tf_commit)
_TENSORFLOW_GIT_COMMIT = "810f233968cec850915324948bbbc338c97cf57f"
# LINT.ThenChange(:io_bazel_rules_clousure)
http_archive(
    name = "org_tensorflow",
    sha256 = "3b875c5121e752adc86578dc24747a220acfa2a7afa4026ff4172500b100854f",
    git_commit = "5bc9d26649cca274750ad3625bd93422617eed4b",
    urls = [
      # Bazel mirror disabled due to b/162781348.
      # "https://mirror.bazel.build/github.com/tensorflow/tensorflow/archive/%s.tar.gz" % _TENSORFLOW_GIT_COMMIT,
      "https://github.com/tensorflow/tensorflow/archive/%s.tar.gz" % _TENSORFLOW_GIT_COMMIT,
    ],
    strip_prefix = "tensorflow-%s" % _TENSORFLOW_GIT_COMMIT,
)

# Needed by tf_py_wrap_cc rule from Tensorflow.
# When upgrading tensorflow version, also check tensorflow/WORKSPACE for the
# version of this -- keep in sync.
http_archive(
    name = "bazel_skylib",
    sha256 = "74d544d96f4a5bb630d465ca8bbcfe231e3594e5aae57e1edbf17a6eb3ca2506",
    urls = [
        "https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/bazel-skylib/releases/download/1.3.0/bazel-skylib-1.3.0.tar.gz",
        "https://github.com/bazelbuild/bazel-skylib/releases/download/1.3.0/bazel-skylib-1.3.0.tar.gz",
    ],
)

# TensorFlow depends on "io_bazel_rules_closure" so we need this here.
# Needs to be kept in sync with the same target in TensorFlow's WORKSPACE file.
# LINT.IfChange(io_bazel_rules_clousure)
http_archive(
    name = "io_bazel_rules_closure",
    sha256 = "5b00383d08dd71f28503736db0500b6fb4dda47489ff5fc6bed42557c07c6ba9",
    strip_prefix = "rules_closure-308b05b2419edb5c8ee0471b67a40403df940149",
    urls = [
        "http://mirror.tensorflow.org/github.com/bazelbuild/rules_closure/archive/308b05b2419edb5c8ee0471b67a40403df940149.tar.gz",
        "https://github.com/bazelbuild/rules_closure/archive/308b05b2419edb5c8ee0471b67a40403df940149.tar.gz",  # 2020-02-14
    ],
)
# LINT.ThenChange(:tf_commit)

http_archive(
    name = "com_google_protobuf",
    sha256 = "930c2c3b5ecc6c9c12615cf5ad93f1cd6e12d0aba862b572e076259970ac3a53",
    strip_prefix = "protobuf-3.21.12",
    urls = ["https://github.com/protocolbuffers/protobuf/archive/v3.21.12.tar.gz"],
)

load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")

protobuf_deps()


# MLMD depends on "io_bazel_rules_go" so we need this here.
http_archive(
    name = "io_bazel_rules_go",
    sha256 = "492c3ac68ed9dcf527a07e6a1b2dcbf199c6bf8b35517951467ac32e421c06c1",
    urls = ["https://github.com/bazelbuild/rules_go/releases/download/0.17.0/rules_go-0.17.0.tar.gz"],
)

# Please add all new TFX dependencies in workspace.bzl.
load("//tfx:workspace.bzl", "tfx_workspace")
tfx_workspace()

# Specify the minimum required bazel version.
load("@bazel_skylib//lib:versions.bzl", "versions")
versions.check("6.4.0")
