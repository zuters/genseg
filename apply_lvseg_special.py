    #!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jānis Zuters

""" Segment LV document using obtained morphological structure
"""

import sys
import codecs
import argparse

from io import open
argparse.open = open

from lvseg import load_learned_and_analyze_main_forms, segment_document

def create_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="learn LVSEG main-forms")
    parser.add_argument(
        '--input', '-i', type=argparse.FileType('r'), default=sys.stdin,
        metavar='PATH',
        help="Input corpus (default: standard input).")
    parser.add_argument(
        '--morpho', '-j', type=argparse.FileType('r'),
        metavar='PATH',
        help="Learned morphological structure.")
    parser.add_argument(
        '--output', '-o', type=argparse.FileType('w'), default=sys.stdout,
        metavar='PATH',
        help="Output file for segmented corpus.")
    parser.add_argument(
        '--marker1', '-m', type=str, default='9474', metavar='STR',
        help="Segmentation marker (default: '%(default)s'))")
    parser.add_argument(
        '--marker2', '-n', type=str, default='9553', metavar='STR',
        help="Uppercase marker (default: '%(default)s'))")
    parser.add_argument(
        '--mode', '-d', type=int, default=0,
        help="Optimization mode of segmentation")
        # 0 - default
        # 1 - prefix-special optimization
    return parser

if __name__ == '__main__':

    sys.stderr = codecs.getwriter('UTF-8')(sys.stderr.buffer)
    sys.stdout = codecs.getwriter('UTF-8')(sys.stdout.buffer)
    sys.stdin = codecs.getreader('UTF-8')(sys.stdin.buffer)

    parser = create_parser()
    args = parser.parse_args()

    args.morpho = codecs.open(args.morpho.name, 'r', encoding='utf-8')
    if args.output.name != '<stdout>':
        args.output = codecs.open(args.output.name, 'w', encoding='utf-8')

    spwords = load_learned_and_analyze_main_forms(args.morpho, args.input.name, "")
    segment_document(args.input.name, args.output, spwords, args.marker1, args.marker2, args.mode)
