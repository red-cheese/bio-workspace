#!/usr/bin/python

import argparse
import os
import solution
import sys
import types
from importlib import machinery


# Default directories (repositories) with solutions.
_DEFAULT_ALGO_DIRS = ['../rosalind/bio-stronghold']

_DEFAULT_INPUT = 'in.txt'
_DEFAULT_OUTPUT = 'out.txt'


def import_algorithms(algo_dirs):
    for algo_dir in algo_dirs:
        impl_dir = os.path.join(os.path.realpath(algo_dir), 'impl')
        assert os.path.isdir(impl_dir)

        sys.path.append(impl_dir)

        for filename in os.listdir(impl_dir):
            if filename.endswith('.py') and not filename.startswith('_'):
                loader = machinery.SourceFileLoader(filename[:-3], os.path.join(impl_dir, filename))

                if loader.name in globals():
                    raise RuntimeError('Duplicate algorithm: {alg} in {dir}'
                                       .format(alg=loader.name, dir=impl_dir))

                mod = types.ModuleType(loader.name)
                loader.exec_module(mod)
                globals()[loader.name] = mod


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('id', metavar='ID',
                        help='Problem ID (e.g. DNA)')
    parser.add_argument('--impl', type=str, default=_DEFAULT_ALGO_DIRS, nargs='+',
                        help='Paths to directories with algorithms')

    parser.add_argument('-i', '--input', default=_DEFAULT_INPUT,
                        help='Input file')
    parser.add_argument('-o', '--output', default=_DEFAULT_OUTPUT,
                        help='Output file')

    parser.add_argument('--test', action='store_true',
                        help='Run algorithm test')

    args = parser.parse_args(sys.argv[1:])

    import_algorithms(args.impl)

    if args.test:
        solution.Solution.test(args.id)
    else:
        print(solution.Solution.go(args.id, args.input, args.output))


if __name__ == '__main__':
    main()
