import argparse
import fileinput
import os
import sys

def fix_spaces_between_java_functions_two(argv=None):
     parser = argparse.ArgumentParser()
     parser.add_argument(
        '--no-markdown-linebreak-ext',
        action='store_const',
        const=[],
        default=argparse.SUPPRESS,
        dest='markdown_linebreak_ext',
        help='Do not preserve linebreak spaces in Markdown'
    )
     parser.add_argument(
          '--markdown-linebreak-ext',
          action='append',
          const='',
          default=['md,markdown'],
          metavar='*|EXT[,EXT,...]',
          nargs='?',
          help='Markdown extensions (or *) for linebreak spaces'
    )
     parser.add_argument('filenames', nargs='*', help='Filenames to fix')
     args = parser.parse_args(argv)
     md_args = args.markdown_linebreak_ext
     print(args)
     print(md_args)
     return 0


fix_spaces_between_java_functions_two()
	
