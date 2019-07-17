    #!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jānis Zuters

""" Extract generic word splitting schemes
"""

import sys
import codecs
import argparse

from io import open
argparse.open = open

from genseg import extract_main_forms_final, analyze_main_forms

def create_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="learn GENSEG main-forms")
    parser.add_argument(
        '--input', '-i', type=argparse.FileType('r'), default=sys.stdin,
        metavar='PATH',
        help="Input text (default: standard input).")
    parser.add_argument(
        '--output', '-o', type=argparse.FileType('w'), default=sys.stdout,
        metavar='PATH',
        help="Output file for GENSEG word splitting schemes")
    parser.add_argument(
        '--mode', '-d', type=int, default=0,
        help="Output mode for analytic output")
        # 0 - default (for segmentation)
        # 1 - segmentation rates (for analysis)
    parser.add_argument(
        '--rootextent', type=int, default=-1,
        help="Extent of initial root extraction, 1..n, default 20")
    parser.add_argument(
        '--minroot', type=int, default=-1,
        help="Minimum root length allowed, 1..n, default 2")
    parser.add_argument(
        '--maxroot', type=int, default=-1,
        help="Maximum root length allowed, 1..n, default 10")
    parser.add_argument(
        '--rootlencoef', type=float, default=-1.0,
        help="Extent of preference of longer roots over smaller, 0.0..1.0, default 0.6, 1.0 means equal")
    parser.add_argument(
        '--maxprefix', type=int, default=-1,
        help="Maximum prefix length allowed, 1..n, default 4")
    parser.add_argument(
        '--prerate', type=float, default=-1.0,
        help="Rate of valid prefixes among all left substrings, 0.0..1.0, default 0.02")
    parser.add_argument(
        '--maxpostfix', type=int, default=-1,
        help="Maximum postfix length allowed, 1..n, default 7")
    parser.add_argument(
        '--postrate', type=float, default=-1.0,
        help="Rate of valid postfixes among all right substrings, 0.0..1.0, default 0.01")
    parser.add_argument(
        '--prepenalty', type=float, default=-1.0,
        help="Rate of panalizing root if prefix before it, 0.0..1.0, default 0.0001")
    parser.add_argument(
        '--prefignore', type=int, default=1,
        help="Prefixes are not splitted, 0/1, default 1 (prefixes not splitted, only postfixes are)")
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
    bestprecodetree,bestpostcodetree,roottree=extract_main_forms_final(mforms, mfs2, args.input
            ,rootextrcoef=args.rootextent
            ,minroot=args.minroot
            ,maxroot=args.maxroot
            ,rootlencoef=args.rootlencoef
            ,maxprefix=args.maxprefix
            ,prerate=args.prerate
            ,maxpostfix=args.maxpostfix
            ,postrate=args.postrate
            ,prepenalty=args.prepenalty
            ,premax0=args.prefignore
            )
    if args.mode == 0:
        analyze_main_forms(mforms,mfs2,bestprecodetree,bestpostcodetree,roottree,args.output)
    elif args.mode == 1:
        analyze_main_forms(mforms,mfs2,bestprecodetree,bestpostcodetree,roottree,fspr=args.output)
    