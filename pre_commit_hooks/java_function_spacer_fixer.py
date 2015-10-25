from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import io
import tokenize

def fix_spaces_between_java_functions(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        print('Found file {0}'.format(filename))
    return retv
