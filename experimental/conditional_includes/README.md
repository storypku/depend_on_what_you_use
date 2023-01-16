# How to Run

1. Install Clang Python Bindings via:

```
python3 -m pip install clang
```

Or, to install a specific version:

```
python3 -m pip install clang==10.0.1
```

2. Install `libclang.so`.

You can do so via your package manager. On ubuntu 18.04:

```
sudo apt-get update
sudo apt-get install libclang-10-dev
```

Or download LLVM pre-built binaries from its GitHub release [page](https://github.com/llvm/llvm-project/releases).

You may need to ensure that versions of Clang Python Bindings and libclang.so match.

The following combinations were tested with different versions of Clang Python Bindings and libclang.so

```
pypi:clang==9.0      /usr/lib/llvm-9/lib/libclang-9.so       (from libclang-9-dev)
pypi:clang==10.0.1   /usr/lib/llvm-10/lib/libclang-10.so     (from libclang-10-dev)
pypi:clang==13.0.1   /opt/llvm-13/lib/libclang.so            (from llvm dist 13.0.1)

pypi:clang==14.0     /usr/lib/llvm-9/lib/libclang-9.so       (from libclang-9-dev)
pypi:clang==14.0     /usr/lib/llvm-10/lib/libclang-10.so     (from libclang-10-dev)
pypi:clang==14.0     /opt/llvm-13/lib/libclang.so            (from llvm dist 13.0.1)
pypi:clang==14.0     /opt/llvm-14/lib/libclang.so            (from llvm dist 14.0.0)
pypi:clang==14.0     /opt/llvm-15/lib/libclang.so            (from llvm dist 15.0.6)
```

3. Experiment with `get_includes.py`

```
./get_includes.py --library=/usr/lib/llvm-10/lib/libclang-10.so main.cc -- -DFOO
```
