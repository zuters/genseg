#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Janis Zuters

from char_tools import wordstartsymbol

def add_to_codetree(tword,codetree,freq=1):
    """ Adds word to tree structure - one node per symbol
    """
    unique=0
    for pos in range(len(tword)):
        s = tword[pos]
        if s not in codetree:
            codetree[s] = [0,{}]
            unique+=1
        codetree[s][0] += freq
        codetree = codetree[s][1]
    return unique

def add_to_codetree_terminal(tword,codetree,freq=1):
    """ Adds word to tree structure - one node per symbol
        word end in the tree characterized by node[0]>0
    """
    for pos in range(len(tword)):
        s = tword[pos]
        if s not in codetree:
            codetree[s] = [0,{}]
        if pos==len(tword)-1:
            codetree[s][0] = freq
        else:
            codetree = codetree[s][1]

def create_frequent_tree(fvocab,post=False):
    ftree = {}
    for w in fvocab:
        ww = w
        if post:
            ww = w[-2:0:-1]+wordstartsymbol
        add_to_codetree(ww,ftree,fvocab[w])
    return ftree

def create_frequent_tree_terminal(fvocab):
    ftree = {}
    for w in fvocab:
        add_to_codetree_terminal(w,ftree,fvocab[w])
    return ftree

def search_codetree(tword,codetree):
    """ Finds the word in codetree (symbol per node),
        returns frequency or 0 if not found
    """
    pos = 0
    while True:
        s = tword[pos]
        if s not in codetree:
            return 0
        elif pos==len(tword)-1:
            return codetree[s][0]
        else:
            pos += 1
            codetree = codetree[s][1]
    
def search_codetree_minfreq(word,codetree,minfreq=1,minlen=1,fullwords=False):
    """ Finds in codetree (symbol per node) longest possible left substring of word,
        at least of len=minlen and at least of freq=minfreq;
        returns frequency and substring length or None if not found
    """
    ret = None
    for pos in range(len(word)):
        s = word[pos]
        if s not in codetree:
            break
        else:
            if codetree[s][0]<minfreq:
                break
            if fullwords:
                if pos==len(word)-1:
                    ret = codetree[s][0],pos+1
            else:
                if pos+1>=minlen or pos==len(word)-1:
                    ret = codetree[s][0],pos+1
            codetree = codetree[s][1]
    return ret
    
def get_word_lefts_frequent(word,codetree,minfreq=1,fullwords=False):
    flen = search_codetree_minfreq(word,codetree,minfreq,fullwords)
    ret = []
    if flen is not None:
        ret = [(word[:flen[1]],flen[0])]
    return ret
    
def get_sentence_word_lefts_frequent(s,codetree,minfreq=1,fullwords=False):
    ret = []
    for w in s:
        ret += get_word_lefts_frequent(w,codetree,minfreq,fullwords)
    return ret

def explore_codetree_plus(codetree,tword,wordpos0=0,emptysubword=False):
    store={}
    if emptysubword:
        store[0]=0 # for empty subword
    wlen = len(tword)
    for wordpos in range(wordpos0,wlen):
        s = tword[wordpos]
        if s not in codetree:
            break
        val = codetree[s][0]    
        if val>0:
            pos = wordpos-wordpos0+1
            store[pos]=val
        codetree = codetree[s][1]
    return store
    
def read_codetree(datafile,reverse=False):
    codetree = {}
    for line in datafile:
        item = line.split()
        word = item[0]
        if reverse: word=word[::-1]
        if len(item)>1:
            num = int(item[1])
        else:
            num = 1
        add_to_codetree_terminal(word,codetree,num)
    return codetree
