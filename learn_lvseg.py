    #!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jānis Zuters

""" Extract LV word splitting schemes
"""

import sys
import codecs
import argparse

from io import open
argparse.open = open

from lvseg import extract_main_forms_final, analyze_main_forms

def create_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="learn LVSEG main-forms")
    parser.add_argument(
        '--input', '-i', type=argparse.FileType('r'), default=sys.stdin,
        metavar='PATH',
        help="Input text (default: standard input).")
    parser.add_argument(
        '--output', '-o', type=argparse.FileType('w'), default=sys.stdout,
        metavar='PATH',
        help="Output file for LVSEG word splitting schemes")
    parser.add_argument(
        '--mode', '-d', type=int, default=0,
        help="Output mode for analytic output")
        # 0 - default (for segmentation)
        # 1 - segmentation rates (for analysis)
    return parser

if __name__ == '__main__':

    sys.stderr = codecs.getwriter('UTF-8')(sys.stderr.buffer)
    sys.stdout = codecs.getwriter('UTF-8')(sys.stdout.buffer)
    sys.stdin = codecs.getreader('UTF-8')(sys.stdin.buffer)

    parser = create_parser()
    args = parser.parse_args()

    if args.input.name != '<stdin>':
        args.input = codecs.open(args.input.name, 'r', encoding='utf-8')
    if args.output.name != '<stdout>':
        args.output = codecs.open(args.output.name, 'w', encoding='utf-8')

    mforms = {}                
    mfs2 = {}   
    extract_main_forms_final(mforms, mfs2, args.input)
    if args.mode == 0:
        analyze_main_forms(mforms,mfs2,args.output)
    elif args.mode == 1:
        analyze_main_forms(mforms,mfs2,fspr=args.output)
    