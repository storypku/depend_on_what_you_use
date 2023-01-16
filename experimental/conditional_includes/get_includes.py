#! /usr/bin/env python3
# Adapted from: https://github.com/llvm/llvm-project/blob/main/clang/bindings/python/examples/cindex/cindex-includes.py
# Example usage:
#   ./get_includes.py --library /usr/lib/llvm-9/lib/libclang-9.so main.cc -- -DBAR
#
# References:
# 1. https://github.com/PointCloudLibrary/clang-bind/blob/master/clang_bind/parse.py
# 2. https://www.fun4jimmy.com/posts/finding-all-includes-in-a-file-using-libclang-and-python/

import argparse
import sys

from clang.cindex import Config, CursorKind, Index, TranslationUnit

_DEFAULT_LIBCLANG_SO = "/opt/llvm/lib/libclang.so"


def setup_clang(library):
    print(f"[DEBUG] libclang.so: located at {library}")
    Config.set_library_file(library)


# It seems that depth info is not available with this approach.
def get_direct_includes_approach_1(filename):
    parse_options = TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD | TranslationUnit.PARSE_SKIP_FUNCTION_BODIES
    tu = TranslationUnit.from_source(filename, None, None, parse_options, None)
    for child in tu.cursor.get_children():
        if child.kind == CursorKind.INCLUSION_DIRECTIVE and child.location.file.name == filename:
            print(f"A1 => {child.spelling}")


def get_direct_includes_approach_2(tu):
    for inc in tu.get_includes():
        if inc.depth != 1:
            continue

        print(f"A2: {inc.source.name} -> {inc.include.name}")
        # Start from one char after the opening bracket or quote
        start_location = (inc.location.line, inc.location.column + 1)
        # Hack(storypku): black magic here, we use -1 to indicate the end of the include line
        end_location = (inc.location.line, -1)
        range_ = tu.get_extent(inc.source.name, (start_location, end_location))
        include = "".join(tok.spelling for tok in list(tu.get_tokens(extent=range_))[:-1])
        print(f"A2 => {include}")


def get_direct_includes_approach_3(tu):
    for inc in tu.get_includes():
        if inc.depth != 1:
            continue
        print(f"A3: {inc.source.name} -> {inc.include.name}")
        with open(inc.source.name, encoding="utf-8") as fin:
            fin.seek(inc.location.offset + 1)
            include = fin.readline().replace('"', ">").split(">")[0]
            print(f"A3 => {include}")


def main():
    def usage(prog):
        return f"{prog} filename -- [clang_args...]"

    parser = argparse.ArgumentParser(usage=usage(sys.argv[0]))
    parser.add_argument("--library", type=str, nargs="?", default=_DEFAULT_LIBCLANG_SO, help="Path to libclang.so")
    parser.add_argument("filename", type=str, metavar="FILE", help="C/C++ file to extract includes")
    parser.add_argument("clang_args", type=str, nargs="*", metavar="CLANG_ARG", help="Arguments to forward to clang")
    args = parser.parse_args()

    setup_clang(args.library)

    get_direct_includes_approach_1(args.filename)

    index = Index.create()
    options = TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD | TranslationUnit.PARSE_SKIP_FUNCTION_BODIES
    tu = index.parse(args.filename, args.clang_args, options=options)
    if not tu:
        parser.error("unable to load input")

    get_direct_includes_approach_2(tu)

    get_direct_includes_approach_3(tu)


if __name__ == "__main__":
    main()
