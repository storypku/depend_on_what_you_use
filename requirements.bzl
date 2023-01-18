load("@rules_python//python/pip_install:pip_repository.bzl", "whl_library")

all_requirements = ["@dwyu_py_deps_libclang//:pkg"]

all_whl_requirements = ["@dwyu_py_deps_libclang//:whl"]

_packages = [("dwyu_py_deps_libclang", "libclang==15.0.6.1     --hash=sha256:4a5188184b937132c198ee9de9a8a2316d5fdd1a825398d5ad1a8f5e06f9b40e     --hash=sha256:687d8549c110c700fece58dd87727421d0710fdd111aa7eecb01faf8e3f50d4e     --hash=sha256:69b01a23ab543908a661532595daa23cf88bd96d80e41f58ba0eaa6a378fe0d8     --hash=sha256:85afb47630d2070e74b886040ceea1846097ca53cc88d0f1d7751d0f49220028     --hash=sha256:8621795e07b87e17fc7aac9f071bc7fe6b52ed6110c0a96a9975d8113c8c2527     --hash=sha256:a1a8fe038af2962c787c5bac81bfa4b82bb8e279e61e70cc934c10f6e20c73ec     --hash=sha256:aaebb6aa1db73bac3a0ac41e57ef78743079eb68728adbf7e80ee917ae171529     --hash=sha256:f7ffa02ac5e586cfffde039dcccc439d88d0feac7d77bf9426d9ba7543d16545")]
_config = {"python_interpreter": "python3", "python_interpreter_target": None, "quiet": True, "timeout": 600, "repo": "dwyu_py_deps", "isolated": True, "extra_pip_args": [], "pip_data_exclude": [], "enable_implicit_namespace_pkgs": False, "environment": {}, "repo_prefix": "dwyu_py_deps_"}
_annotations = {}

def _clean_name(name):
    return name.replace("-", "_").replace(".", "_").lower()

def requirement(name):
   return "@dwyu_py_deps_" + _clean_name(name) + "//:pkg"

def whl_requirement(name):
   return "@dwyu_py_deps_" + _clean_name(name) + "//:whl"

def data_requirement(name):
    return "@dwyu_py_deps_" + _clean_name(name) + "//:data"

def dist_info_requirement(name):
    return "@dwyu_py_deps_" + _clean_name(name) + "//:dist_info"

def entry_point(pkg, script = None):
    if not script:
        script = pkg
    return "@dwyu_py_deps_" + _clean_name(pkg) + "//:rules_python_wheel_entry_point_" + script

def _get_annotation(requirement):
    # This expects to parse `setuptools==58.2.0     --hash=sha256:2551203ae6955b9876741a26ab3e767bb3242dafe86a32a749ea0d78b6792f11`
    # down wo `setuptools`.
    name = requirement.split(" ")[0].split("=")[0]
    return _annotations.get(name)

def install_deps():
    for name, requirement in _packages:
        whl_library(
            name = name,
            requirement = requirement,
            annotation = _get_annotation(requirement),
            **_config,
        )
