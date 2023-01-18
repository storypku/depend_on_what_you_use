load("@rules_python//python/pip_install:repositories.bzl", "pip_install_dependencies")
load("//:requirements.bzl", _install_py_deps = "install_deps")

def dwyu_extra_deps():

    # TODO(storypku): remove the following line once rules_python
    # [issue #497](https://github.com/bazelbuild/rules_python/issues/497) is resolved.
    # Otherwise, "bazel run @depend_on_what_you_use//:apply_fixes"
    pip_install_dependencies()

    _install_py_deps()
