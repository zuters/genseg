    #!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jānis Zuters

""" Segment LV document using obtained splitting schemes
"""

import sys
import codecs
import argparse

from io import open
argparse.open = open

from lvseg import load_spwords, segment_document

def create_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="learn LVSEG main-forms")
    parser.add_argument(
        '--input', '-i', type=argparse.FileType('r'), default=sys.stdin,
        metavar='PATH',
        help="Input corpus (default: standard input).")
    parser.add_argument(
        '--split', '-j', type=argparse.FileType('r'),
        metavar='PATH',
        help="Learned segmentation vocabulary.")
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
        '--mode', '-d', type=int, default=1,
        help="Optimization mode of segmentation")
        # 0 - prefixes also segmented
        # 1 - prefix-special optimization (default)
        # 2 - prefixes not segmented
    return parser

if __name__ == '__main__':

    sys.stderr = codecs.getwriter('UTF-8')(sys.stderr.buffer)
    sys.stdout = codecs.getwriter('UTF-8')(sys.stdout.buffer)
    sys.stdin = codecs.getreader('UTF-8')(sys.stdin.buffer)

    parser = create_parser()
    args = parser.parse_args()

    args.split = codecs.open(args.split.name, 'r', encoding='utf-8')
    if args.input.name != '<stdin>':
        args.input = codecs.open(args.input.name, 'r', encoding='utf-8')
    if args.output.name != '<stdout>':
        args.output = codecs.open(args.output.name, 'w', encoding='utf-8')

    spwords = load_spwords(args.split)
    segment_document(args.input, args.output, spwords, args.marker1, args.marker2, args.mode)
