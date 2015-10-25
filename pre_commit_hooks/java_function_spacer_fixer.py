from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from pre_commit_hooks.util import cmd_output

import argparse
import io
import tokenize

def fix_spaces_between_java_functions(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retv = 0
    print('eggs n bacon')
    cmd_output('eggs n bacon')
    for filename in args.filenames:
        print('Found file {0}'.format(filename))
    return retv

if __name__ == '__main__':
    fix_spaces_between_java_functions()

