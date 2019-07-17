#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Janis Zuters
# split parallel corpora by sentence lengths of lang1

import codecs
from collections import Counter

from voc_tools import extract_frequent_vocabulary
from voc_tools import add_to_vocab_multi, add_to_vocab_multi_reverse
from tree_tools import add_to_codetree_terminal, search_codetree, explore_codetree_plus

MAXPREFIX = 4
MAXPOSTFIX = 7
MINROOT = 2
MAXROOT = 10
ROOTLENCOEF = 0.6
PREVALIDRATE = 0.02
POSTVALIDRATE = 0.01
PREPENALTY = 0.0001
ROOTEXTRACTEXTENT = 20

def add_to_struct_k30(sh,k1,k2,k3,data,k10=[0.0],k20=[0.0]):
    if k1 not in sh:
        k10a = tuple(k10)
        sh[k1] = [list(k10a),{}]
    if k2 not in sh[k1][1]:    
        k20a = tuple(k20)
        sh[k1][1][k2] = [list(k20a),{}]
    if k3 not in sh[k1][1][k2][1]:
        sh[k1][1][k2][1][k3] = []
    for d in data:
        if d not in sh[k1][1][k2][1][k3]:
            sh[k1][1][k2][1][k3].append(d)

def extract_main_forms_generic(mforms,mfs2,voc,pretree,posttree,roottree,premax0=False):
    for word in voc:
        if word.isalpha():
            if premax0 == False:
                premax = max(0,min(MAXPREFIX,len(word)-MINROOT))
            else:
                premax = 0
            postmax = max(0,min(MAXPOSTFIX,len(word)-MINROOT))
            for r1 in range(0,premax+1):
                prefix = word[:r1]
                if r1>0 and search_codetree(prefix,pretree)==0:
                    break
                for r20 in range(0,postmax+1):
                    r2 = len(word)-r20
                    if r2-r1<MINROOT:
                        break
                    postfix = word[r2:]
                    if r20>0 and search_codetree(postfix[::-1],posttree)==0:
                        break
                    root = word[r1:r2]
                    
                    if search_codetree(root,roottree):
                        mainform=(root,)
                        if r1==0:
                            spword = (root,postfix)
                            data = [('R','POST')]
                        else:
                            spword = (root,postfix,prefix)
                            data = [('R','POST','PREF')]
                        add_to_struct_k30(mforms,mainform,word,spword,data)
                        add_to_struct_k30(mfs2,word,mainform,spword,data)
            if word not in mfs2:
                mainform=(word,)
                spword = (word,'')
                data = [('R','W')]
                add_to_struct_k30(mforms,mainform,word,spword,data)
                add_to_struct_k30(mfs2,word,mainform,spword,data)
    
def analyze_main_forms_1_generic(mforms,pretree,posttree,roottree):
    for mf in mforms:
        for word in mforms[mf][1]:
            wordrate = 0.0
            for spword in mforms[mf][1][word][1]:
                root = spword[0]
                postfix = spword[1]
                nonrootlen = 10-len(root)
                if nonrootlen<0: nonrootlen = 0
                rootrank = search_codetree(root,roottree)
                if postfix=="":
                    postfixrank = 0
                else:
                    postfixrank = search_codetree(postfix[::-1],posttree)
                wr = 1/(rootrank+postfixrank+1) * ROOTLENCOEF**nonrootlen
                for spscheme in mforms[mf][1][word][1][spword]:
                    if spscheme[-1]=='PREF':
                        wr *= PREPENALTY
                    break
                wordrate = max(wordrate,wr)
            mforms[mf][0][0] += wordrate
            mforms[mf][1][word][0][0] = wordrate

def analyze_main_forms_2(mforms,mfs2):
    # write basic mainrates to mfs2
    for mf in mforms:
        for word in mforms[mf][1]:
            mfs2[word][1][mf][0][0] = mforms[mf][0][0]
            mfs2[word][0][0] = max(mfs2[word][0][0],mfs2[word][1][mf][0][0])
            
def join_tuple_str(data):
    if isinstance(data,str):
        return data
    else:
        return ' '.join(data)

def save_main_forms(repo,fout,tech=False):
    lopen = False
    if isinstance(fout,str): 
        fout = codecs.open(fout, 'w', encoding='utf-8')
        lopen = True
    for e1 in sorted(repo):
        if tech:
            fout.write("* {} {}\n".format(join_tuple_str(e1),repo[e1][0][0]))
        else:
            fout.write("* {} [{:.2f}]\n".format(e1,repo[e1][0][0]))
        for e2 in repo[e1][1]:
            if tech:
                fout.write("  ** {} {}\n".format(join_tuple_str(e2),repo[e1][1][e2][0][0]))
            else:
                fout.write("  ** {} <{:.2f}>\n".format(e2,repo[e1][1][e2][0][0]))
            for e3 in repo[e1][1][e2][1]:
                if tech:
                    fout.write("      - {}\n".format(join_tuple_str([f3+'-' for f3 in e3])))
                else:
                    fout.write("      - {}\n".format(e3))
                for ee in repo[e1][1][e2][1][e3]:
                    if tech:
                        fout.write("        + {}\n".format(join_tuple_str([ff+'-' for ff in ee])))
                    else:
                        fout.write("        + {}\n".format(ee))
    if lopen:
        fout.close()
                
def register_subwords(vocab,rawprefixfile=None,rawpostfixfile=None,freqnotrank=False):
    rawprecodetree = {}
    rawpostcodetree = {}
    rawprevocab = Counter()
    rawpostvocab = Counter()
    for item in vocab.items():
        word = item[0]
        freq = item[1]
        preword =word[:MAXROOT+2]
        add_to_vocab_multi(preword,rawprevocab,freq)
        add_to_vocab_multi_reverse(word[::-1],rawpostvocab,MAXPOSTFIX,MINROOT,freq)
    prevfreq = -1
    num = 0
    for item in sorted(rawprevocab.items(),key=lambda x: x[1],reverse=True):
        word = item[0]
        freq = item[1]
        if freqnotrank:
            num = freq
        else:
            if freq!=prevfreq: num+=1
        add_to_codetree_terminal(word,rawprecodetree,num)
        if rawprefixfile:
            rawprefixfile.write(" {0} {1}\n".format(word,num))
        prevfreq = freq
    prevfreq = -1
    num = 0
    for item in sorted(rawpostvocab.items(),key=lambda x: x[1],reverse=True):
        word = item[0]
        freq = item[1]
        if freqnotrank:
            num = freq
        else:
            if freq!=prevfreq: num+=1
        add_to_codetree_terminal(word,rawpostcodetree,num)
        if rawpostfixfile:
            rawpostfixfile.write(" {0} {1}\n".format(word,num))
        prevfreq = freq
        
    return rawprecodetree,rawpostcodetree,rawprevocab

def analyze_prefixes_generic(prefsource,rootsource,vocab,rawprevocab,preffile=None,loadfile=False):
    """ Collect candidate prefixes
    """
    lopen = False
    if isinstance(preffile,str): 
        preffile = codecs.open(preffile, 'w', encoding='utf-8')
        lopen = True
    prefixes = Counter()
    if loadfile:
        if preffile is not None:
            for line in preffile:
                entry = line.split()
                prefixes[entry[0]] = int(entry[1])
    else:
        preflen1 = 1
        preflen2 = MAXPREFIX
        rootlen1 = 4
        rootlen2 = 7
        for item in vocab.items():
            word = item[0]
            preftree = prefsource
            for p in range(1,preflen2+1):
                if p+rootlen1>len(word): break
                ps = word[p-1]
                if ps not in preftree: break
                elif preftree[ps][0]>0 and p>=preflen1:
                    prefix = word[:p]
                    roottree = rootsource
                    for r in range(1,rootlen2+1):
                        pr = p+r
                        if pr>len(word): break
                        prs = word[pr-1]
                        if prs not in roottree: break
                        root=word[p:pr]
                        if r>=rootlen1 and roottree[prs][0]>0:
                            prefixes[prefix]+=rawprevocab[root]
                        roottree = roottree[prs][1]
                preftree = preftree[ps][1]
        if preffile is not None:
            for item in sorted(prefixes.items(),key=lambda x: x[1],reverse=True):
                preffile.write(" {0} {1}\n".format(item[0],item[1]))
    if lopen:
        preffile.close()
    return prefixes

def analyze_postfixes_generic(rootsource,postsource,vocab,rawprevocab,postfile=None,loadfile=False):
    """ Collect candidate postfixes, suffixes, endings
    """
    lopen = False
    if isinstance(postfile,str): 
        postfile = codecs.open(postfile, 'w', encoding='utf-8')
        lopen = True
    postfixes = Counter()
    if loadfile:
        if postfile is not None:
            for line in postfile:
                entry = line.split()
                postfixes[entry[0]] = int(entry[1])
    else:
        postlen2 = 7
        rootlen1 = 4
        rootlen2 = 7
        for item in vocab.items():
            word = item[0]
#            freq = item[1]
            posttree = postsource
            for p in range(1,postlen2+1):
                if p+rootlen1>len(word): break
                ps = word[-p]
                if ps not in posttree: break
                elif posttree[ps][0]>0:
                    postfix = word[-p:]
                    for rootlen in range(rootlen1,1+min(rootlen2,len(word)-p)):
                        roottree = rootsource
                        for r in range(rootlen,0,-1):
                            pr = p+r
                            prs = word[-pr]
                            if prs not in roottree: break
                            root=word[-p-rootlen:-p]
                            if r==1 and roottree[prs][0]>0: # frequence
                                postfixes[postfix]+=rawprevocab[root]
                            roottree = roottree[prs][1]
                posttree = posttree[ps][1]
        # print to files
        if postfile is not None:
            for item in sorted(postfixes.items(),key=lambda x: x[1],reverse=True):
                postfile.write(" {0} {1}\n".format(item[0],item[1]))
    if lopen:
        postfile.close()
    return postfixes

def build_codetree_best(ppvocab,rate,reverse,datafile=None):
    """ Collect best prefixes (reverse=False) or postfixes (reverse=True)
    """
    codetree = {}
    icount = len(ppvocab.items())
    if rate>1.0: bestcount=int(rate)
    else: bestcount = int(round(icount * rate))
    prevfreq = 0
    numx = 0
    num = 0
    for item in sorted(ppvocab.items(),key=lambda x: x[1],reverse=True):
        if numx>=bestcount: break
        freq = int(item[1])
        if freq!=prevfreq: num+=1
        word = item[0]
        numout = num    
        if datafile is not None:
            datafile.write(u" {0} {1}\n".format(word,numout))
        if reverse: word=word[::-1]
        add_to_codetree_terminal(word,codetree,numout)
        prevfreq = freq
        numx += 1
    return codetree

def extract_root(precodetree,bestprecodetree,bestpostcodetree,word,minrootlen,bestcount):
    # create candidate list of prefixes, with a prefix denoted as its length
    prestore = explore_codetree_plus(bestprecodetree,word,0,True)
    # create candidate list of postfixes, with a postfix denoted as its length
    poststore = explore_codetree_plus(bestpostcodetree,word[::-1],0,True)
    roots = Counter()
    wlen = len(word)
    for xpos in prestore.items(): # all available prefixes
        pos = xpos[0]
        for ypos in poststore.items(): # all available postfixes
            pos2rev = ypos[0]
            if pos+pos2rev+minrootlen<=wlen:
                pos2 = wlen-pos2rev
                root=word[pos:pos2]
                if (search_codetree(root,precodetree)>0):
                    prerank=xpos[1]
                    rootrank = search_codetree(root,precodetree)
                    postrank=ypos[1]
                    rootrate = prerank+rootrank+postrank
#                    nonrootlen = len(word)-len(root)
                    roots[root]=rootrate*ROOTLENCOEF**len(root)
    minroots=[]
    if len(roots)>0:
        cnt=0
        for root in sorted(roots,key=lambda x: roots[x]):
            minroots.append(root)
#            print(root,roots[root])
            cnt+=1
            if cnt>=bestcount: break
    return minroots #,roots[minroot]
    
longenoughrootlen = 5
rootregbase = 4
minrootfreq = 1

def collect_roots(vocab,rawprecodetree,bestprecodetree,bestpostcodetree,datafile=None,bestcount=1):
    roottree = {}
    roots = Counter()
    for word in vocab:
        minroots = extract_root(rawprecodetree,bestprecodetree,bestpostcodetree,word,MINROOT,bestcount)
#        if word=='action' or word=='actions':
#            print("ARR",word,minroots)
        cnt=0
        for root in minroots:
            freq = search_codetree(word,rawprecodetree)
            if freq>0:
                roots[root] += vocab[word]
            cnt+=1
    for root in roots:
        if len(root)<longenoughrootlen: # longer roots are better
            expo = longenoughrootlen - len(root)
            roots[root] = roots[root] // round(rootregbase**expo)
    prevfreq = 0
    numx = 0
    num = 0
    for root in sorted(roots,key=lambda x: roots[x], reverse=True):
#        if root=='action':
#            print('AAAAAAACTION')
        freq = roots[root]
        if freq<minrootfreq: break
        if freq!=prevfreq: num+=1
        if datafile:
            datafile.write(u" {0} {1}\n".format(root,num))
        add_to_codetree_terminal(root,roottree,num)
        numx += 1
        prevfreq = freq
    return roottree

def process_spword_generic(spscheme0,spw):
    if spscheme0[-1]=='PREF':
        spw = ('@'+spw[-1],)+spw[:-1]
    return spw

def analyze_spwords_1_generic(mfs2):
    sprates = {}
    for word in mfs2:
        if word not in sprates:
            sprates[word] = {}
        for mf in mfs2[word][1]:
            for spword in mfs2[word][1][mf][1]:
                spscheme0 = mfs2[word][1][mf][1][spword][0]
                spw2 = process_spword_generic(spscheme0,spword)
                mfrate = mfs2[word][1][mf][0][0]
                if spw2 not in sprates[word]:
                    sprates[word][spw2] = 0.0
                if mfrate>sprates[word][spw2]:
                    sprates[word][spw2] = mfrate
                break
    return sprates

def analyze_main_forms(mforms,mfs2,bestprecodetree,bestpostcodetree,roottree,fspw="",mstr="",fspr=""):
    analyze_main_forms_1_generic(mforms,bestprecodetree,bestpostcodetree,roottree)
    analyze_main_forms_2(mforms,mfs2)
    sprates = analyze_spwords_1_generic(mfs2)
    spwords = analyze_spwords_2(sprates)
    if isinstance(mstr,str)==False or mstr!="":
        save_main_forms(mforms,mstr,True)
    if isinstance(fspw,str)==False or fspw!="":
        save_spwords(spwords,fspw,True)
    if isinstance(fspr,str)==False or fspr!="":
        save_sprates(sprates,fspr,True)
    return spwords

def save_sprates_entry(entry,fout,tech=False):
    for e2all in sorted(entry.items(), key=lambda x: x[1], reverse=True):
        e2 = e2all[0]
        if tech:
            fout.write("  ** {} {}\n".format(" ".join(e2).rstrip(),entry[e2]))
        else:
            fout.write("  ** {} <{:.2f}>\n".format(e2,entry[e2]))

def save_sprates(repo,fout,tech=False):
    lopen = False
    if isinstance(fout,str): 
        fout = codecs.open(fout, 'w', encoding='utf-8')
        lopen = True
    for e1 in sorted(repo):
        fout.write("* {} ".format(e1))
        mval = 0.0
        for e2 in repo[e1]:
            if repo[e1][e2]>mval:
                mval = repo[e1][e2]
        if tech:
            fout.write("{}\n".format(mval))
        else:
            fout.write("[{:.2f}]\n".format(mval))
        save_sprates_entry(repo[e1],fout,tech)
    if lopen:
        fout.close()
 
def save_spwords(repo,fout,tech=False):
    lopen = False
    if isinstance(fout,str): 
        fout = codecs.open(fout, 'w', encoding='utf-8')
        lopen = True
    for e1 in sorted(repo):
        if tech:
            fout.write("{} {}\n".format(e1," ".join(repo[e1])))
        else:
            fout.write("{}\n  {}\n".format(e1,repo[e1]))
    if lopen:
        fout.close()
                    
def analyze_spwords_2(sprates):
    sps2 = {}
    for word in sprates:
        rate = 0.0
        sp = ''
        for spword in sprates[word]:
            if sprates[word][spword]>rate:
                rate = sprates[word][spword]
                sp = spword
        if sp[-1]=='': sp = sp[:-1]
        sps2[word] = sp
    return sps2

def extract_main_forms_final(mforms,mfs2,corpus,mstr="",
        rootextrcoef=-1,minroot=-1,maxroot=-1,rootlencoef=-1,maxprefix=-1,prerate=-1,maxpostfix=-1,postrate=-1,prepenalty=-1,premax0=1):
    global ROOTEXTRACTEXTENT
    global MINROOT
    global MAXROOT
    global ROOTLENCOEF
    global MAXPREFIX
    global PREVALIDRATE
    global MAXPOSTFIX
    global POSTVALIDRATE
    global PREPENALTY
    if rootextrcoef>0: ROOTEXTRACTEXTENT = rootextrcoef
    if minroot>0: MINROOT = minroot
    if maxroot>0: MAXROOT = maxroot
    if rootlencoef>0: ROOTLENCOEF = rootlencoef
    if maxprefix>0: MAXPREFIX = maxprefix
    if prerate>0: PREVALIDRATE = prerate
    if maxpostfix>0: MAXPOSTFIX = maxpostfix
    if postrate>0: POSTVALIDRATE = postrate
    if prepenalty>0: PREPENALTY = prepenalty
    fvocab2 = extract_frequent_vocabulary(corpus,0,True,False)
    rawprecodetree,rawpostcodetree,rawprevocab = register_subwords(fvocab2)
    prefixes = analyze_prefixes_generic(rawprecodetree,rawprecodetree,fvocab2,rawprevocab)
    postfixes = analyze_postfixes_generic(rawprecodetree,rawpostcodetree,fvocab2,rawprevocab)
    bestprecodetree = build_codetree_best(prefixes,rate=PREVALIDRATE,reverse=False)
    bestpostcodetree = build_codetree_best(postfixes,rate=POSTVALIDRATE,reverse=True)
    roottree=collect_roots(fvocab2,rawprecodetree,bestprecodetree,bestpostcodetree,bestcount=ROOTEXTRACTEXTENT)
    extract_main_forms_generic(mforms,mfs2,fvocab2,bestprecodetree,bestpostcodetree,roottree,premax0=premax0)
    if isinstance(mstr,str)==False or mstr!="":
        save_main_forms(mforms,mstr,True)
    return bestprecodetree,bestpostcodetree,roottree
        