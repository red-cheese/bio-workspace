#!/usr/bin/python

import argparse
import os
import solution
import sys
import types
from importlib import machinery


_DEFAULT_IMPL_DIRS = ['../rosalind/bio-stronghold/impl', '../bio-coursera/impl']

_DEFAULT_INPUT = 'in.txt'
_DEFAULT_OUTPUT = 'out.txt'


def import_algorithms(impl_dirs):
    for impl in impl_dirs:
        impl = os.path.realpath(impl)
        assert os.path.isdir(impl)

        for filename in os.listdir(impl):
            if filename.endswith('.py') and not filename.startswith('_'):
                loader = machinery.SourceFileLoader(filename[:-3], os.path.join(impl, filename))
                mod = types.ModuleType(loader.name)
                loader.exec_module(mod)
                globals()[loader.name] = mod


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('id', metavar='ID',
                        help='Problem ID (e.g. DNA)')
    parser.add_argument('--impl', type=str, default=_DEFAULT_IMPL_DIRS, nargs='+',
                        help='Paths to directories with algorithms')

    parser.add_argument('-i', '--input', default=_DEFAULT_INPUT,
                        help='Input file')
    parser.add_argument('-o', '--output', default=_DEFAULT_OUTPUT,
                        help='Output file')

    parser.add_argument('--test', default=False, help='Run algorithm test')

    args = parser.parse_args(sys.argv[1:])

    import_algorithms(args.impl)

    if args.test:
        solution.Solution.test(args.id)
    else:
        print(solution.Solution.go(args.id, args.input, args.output))


if __name__ == '__main__':
    main()
