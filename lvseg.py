#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Janis Zuters

import codecs
from collections import Counter
from root_tools import root_check, is_good_part_generic, prefixes3
from root_data import shift,vrtypes,shiftn,nrtypes,shiftnum,numrtypes,nonseg

from voc_tools import extract_frequent_vocabulary

def create_morpho_struct_lv():
    s = {}
    
    s["infinitive"] = [["t","ties"],["RINF-C1-C","RINF-C1","RINF-C2","RINF-C3"]]
    s["present-c1-p1"] = [["u","am","os","as"],["RPC1-P1"]]
    s["present-c1-p1-amies"] = [["at","amies","aties"],["RPC1-P1-AMIES"]]
    s["present-c1-p2-i"] = [["i"],["RPC1-P2-I"]]
    s["present-c1-p2-iet"] = [["iet"],["RPC1-P2-IET"]]
    s["present-c1-p2-0"] = [[""],["RPC1-P2-0"]]
    s["present-c1-p3-0"] = [[""],["RPC1-P3-0"]]
    
    s["present-c2-p1"] = [["u","am","os"],["RPC2-OJ"]]
    s["present-c2-p1-amies"] = [["at","amies","aties","iet"],["RPC2-OJAMIES"]]
    s["present-c2-p23-ras"] = [["as"],["RPC2-OJ"]]
    s["present-c2-p23-ries"] = [["ies"],["RPC2-OJAMIES"]]
    s["present-c2-p23-base"] = [[""],["RPC2-P23-A"]]
    
    s["present-c3-p12-am"] = [["am","as"],["RPC3-AM"]]
    s["present-c3-p12-ām"] = [["ām","ās"],["RPC3-ĀM"]]
    s["present-c3-p12-amies"] = [["at","amies","aties"],["RPC3-AMIES"]]
    s["present-c3-p12-āmies"] = [["āt","āmies","āties"],["RPC3-ĀMIES"]]
    s["present-c3-p12-s"] = [["u","i","os"],["RPC3-P12-S"]]
    s["present-c3-p12-ies"] = [["ies","iet"],["RPC3-P12-IES"]]
    s["present-c3-p3-a"] = [["a"],["RPC3-P3-A"]]
    s["present-c3-p3-0"] = [[""],["RPC3-P3-0"]]
    s["present"] = [[None],["present-c1-p1","present-c1-p1-amies",
      "present-c1-p2-i","present-c1-p2-iet","present-c1-p2-0","present-c1-p3-0",
      "present-c2-p1","present-c2-p1-amies","present-c2-p23-base","present-c2-p23-ras","present-c2-p23-ries",
      "present-c3-p12-am","present-c3-p12-ām","present-c3-p12-amies","present-c3-p12-āmies",
      "present-c3-p12-s","present-c3-p12-ies","present-c3-p3-a","present-c3-p3-0"]]
    
    s["past"] = [["u","i","a","ām","āt","os","ies","ās","āmies","āties"],["RPAST","RPASTOJ"]]
    # lokāms dar.k. pagātnes divdabis 1: mētājušies, radījuši, redzējušākajiem, dziestošākajai
    s["activepast1uš"] = [["uš"],["RKUS","ROJ"]] # braukuši, strādājuši
    s["activepast2us"] = [["us"],["RKUS","ROJ"]] # braukusi
    s["activepast2usi"] = [["i","ies"],["activepast2us"]] # braukusi
    s["activepast1oš"] = [["oš"],["ROS","ROJ"]] # braucoši, strādājoši
    # lokāms dar.k. pagātnes divdabis 2: raudājusi, mācījusies, mētājies, studējis
    s["activepast2i"] = [["ies","is"],["RCIS","ROJ"]] # braucis
    # nelokāms divdabis: darot/daroties, ejam/ejamies, skatām/skatāmies
    s["pinflexa"] = [["am","amies"],["RAM","ROJ"]]
    s["pinflexā"] = [["ām","āmies"],["RĀM"]]
    # ciešamās kārtas tagadnes divdabis: lasāms, redzams, skatāmais, redzamais
    s["passivepresenta"] = [["am"],["RAMAIS","ROJ"]]
    s["passivepresentā"] = [["ām"],["RĀMAIS","ROJ"]]
    # ciešamās kārtas pagātnes divdabis: lasīts, redzēts, skatīts
    s["passivepast"] = [["t"],["RPASSPAST-C1-C","RPASSPAST-C1","RPASSPAST-C2","RPASSPAST-C3"]]
    # daļēji lokāmais divdabis: rakdams,rakdama,rakdamies,rakdamās
    s["dam"] = [["dam"],["RDAM","RDAMA"]]
    s["dams"] = [["s","i","a","as","ies","ās"],["dam"]]
    # nākotne: nākšu, darīsit, mācīsieties
    s["future"] = [["šu","šos","si","sim","siet","sies","simies","sieties","sit"],["RFUTA","RFUT"]]
    s["futures"] = [["s"],["RFUTAS","RFUTS"]]
    s["relativefut"] = [["šot"],["RFUTA","RFUT"]]
    s["relativepres"] = [["ot","oties"],["ROS","ROJ"]]
    # vēlamā: nāktu, nāktos, mācītos, mācīšoties
    s["conditional"] = [["tu","tos","šoties"],["RFUTA","RFUT"]]
    s["verb"] = [[None],["present","past","infinitive","future","futures","relativefut","relativepres","conditional"]]
    s["adjparticiple"] = [[None],["activepast2usi","activepast2i","pinflexa","pinflexā","def","dams"]]
    s["adverb"] = [["āk","atā"],["RK"]] # labāk, divatā
    s["adverbšus"] = [["šus"],["RŠANA","RŠAN"]] # līšus, braukšus
    s["adverbtin"] = [["tin"],["RINF-C1"]] # tērptin
    s["adverbin"] = [["in"],["RPAST"]] # laidin

    s["padsmit"] = [["padsmit"],["NUM19"]]
    s["desmit"] = [["desmit"],["NUM29"]]
    s["simt"] = [["simt"],["NUM29"]]
    s["tūkstoš"] = [["tūkstoš"],["NUM29"]]
    s["numeral"] = [[None],["padsmit","desmit","simt","tūkstoš"]]

    s["anbase"] = [[None],["passivepast","passivepresenta","passivepresentā",
      "activepast1uš","activepast1oš","īg","isk","en","ēj","nēj","ain","um","RK"]]
    s["acomp"] = [["āk"],["anbase"]]
    # noteiktā galotne (īp. v./divdabis): radošais, radošā, ..., radošajos, radošākajos; labais
    s["def1s"] = [["ais","ā","ajam","o","ajā"],["acomp","anbase","numeral"]]
    s["def1p"] = [["ie","o","ajiem","os","ajos"],["acomp","anbase","numeral"]]
    s["def4s"] = [["ā","ās","ajai","o","ajā"],["acomp","anbase","numeral"]]
    s["def4p"] = [["ās","o","ajām","ajās"],["acomp","anbase","numeral"]]
    s["def"] = [[None],["def1s","def1p","def4s","def4p"]]
    
    s["noun1"] = [[None],["noun1s","noun1se","noun1šs","noun1šš","noun1ss","noun1š","noun1p"]]
    s["noun1s"] = [["s","a","am","u","ā"],["acomp"]]
    s["noun1se"] = [[""],["R10"]]
    s["noun1š"] = [["š","a","am","u","ā"],["iņ","tiņ"]]
    s["noun1šs"] = [["a","am","u","ā"],["anbase"]]
    s["noun1šš"] = [["š"],["anbase"]]
    s["noun1ss"] = [["s"],["anbase"]]
    s["noun1p"] = [("i","u","iem","us","os"),["acomp","anbase","RK"]]

    s["noun2"] = [[None],["noun2se","noun2sx","noun2sy","noun2p","noun2sxx"]]
    s["noun2se"] = [[""],["R20","īt"]]
    s["noun2sx"] = [["is","im","i","ī"],["R2x","īt","īkl","ekl"]]
    s["noun2sy"] = [["a"],["R2y","īš","īkļ","ekļ"]]
    s["noun2p"] = [["i","u","iem","us","os"],["R2y","īš","īkļ","ekļ"]]
    s["noun2sxx"] = [["s"],["R2specx"]]
    
    s["noun3"] = [[None],["noun3s","noun3p","noun3fs","noun3fp"]]
    s["noun3s"] = [["us","um","u","ū"],["RK"]]
    s["noun3p"] = [["i","u","iem","us","os"],["RK"]]
    s["noun3fs"] = [["us","ui","u","ū"],["RK"]]
    s["noun3fp"] = [["us","ūm","os"],["RK"]]
    
    s["noun4"] = [[None],["noun4s","noun4ms","noun4fs","noun4p"]]
    s["noun4s"] = [("a","as","u","ā"),["acomp","anbase","iņ","tiņ","RK"]]
    s["noun4ms"] = [["am"],["RK"]]
    s["noun4fs"] = [["ai"],["RK"]]
    s["noun4p"] = [["as","u","ām","ās"],["acomp","anbase","iņ","tiņ","RK"]]
    
    s["noun5"] = [[None],["noun5s","noun5ms","noun5fs","noun5px","noun5py"]]
    s["noun5s"] = [["e","es","i","ē"],["R5x","īt","ekl"]]
    s["noun5ms"] = [["em"],["R5x"]]
    s["noun5fs"] = [["ei"],["R5x","īt","ekl"]]
    s["noun5px"] = [["es","ēm","ēs"],["R5x","īt","ekl"]]
    s["noun5py"] = [["u"],["R5y","īš","ekļ"]]
    
    s["noun6"] = [[None],["noun6s","noun6px","noun6py"]]
    s["noun6s"] = [["s","ij","i","ī"],["R6x"]]
    s["noun6px"] = [["is","u","īm","īs"],["R6x"]]
    s["noun6py"] = [["u"],["R6y"]]

    s["īgsn"] = [["īgsn"],["RC"]]
    s["īg"] = [["īg"],["RC"]]
    s["isk"] = [["isk"],["RC"]]
    s["en"] = [["en"],["RC"]]
    s["ēj"] = [["ēj"],["RC","īgsn"]]
    s["nēj"] = [["nēj"],["RK"]]
    s["ain"] = [["ain"],["RK"]]
    s["um"] = [["um"],["RKUS","ROJ","RK"]]

    s["ekl"] = [["ekl"],["RC"]]
    s["ekļ"] = [["ekļ"],["RC"]]
    s["īkl"] = [["īkl"],["RC"]]
    s["īkļ"] = [["īkļ"],["RC"]]
    s["īš"] = [["īš"],["RC"]]
    s["īt"] = [["īt"],["RC"]]
    s["iņ"] = [["iņ"],["RC"]]
    s["tiņ"] = [["tiņ"],["REN","R2specx","R6x","en"]]

    s["šan"] = [["šan"],["RŠANA","RŠAN"]]
    s["šana4s"] = [("a","as","ai","u","ā"),["šan"]]
    s["šana4pr"] = [["ās","os"],["šan"]]
    s["šana"] = [[None],["šana4s","šana4pr"]]
    
    s["ēn+"] = [["ēn","ēniņ","iniek"],["RC"]]
    s["uk"] = [["uk"],["RČ"]]
    s["niek"] = [["niek"],["RK"]]
    s["uk1s+"] = [("s","a","am","u","ā",""),["uk","niek","ēn+"]]
    s["uk1p+"] = [("i","u","iem","us","os"),["uk","niek","ēn+"]]
    s["uks+"] = [[None],["uk1s+","uk1p+"]]

    s["īb+"] = [["īb","ībiņ"],["RC"]]
    s["nīc"] = [["nīc"],["RK"]]
    s["aļ"] = [["aļ"],["RK"]]
    s["av"] = [["av"],["RK"]]
    s["oņ"] = [["oņ"],["RK"]]
    s["nīca4s+"] = [("a","as","ai","u","ā"),["nīc","aļ","av","oņ","īb+"]]
    s["nīca4p+"] = [["as","u","ām","ās"],["nīc","aļ","av","oņ","īb+"]]
    s["nīca+"] = [[None],["nīca4s+","nīca4p+"]]

    s["ēj+"] = [["ēj"],["ROJ","RCIS"]]
    s["āj+"] = [["āj"],["RPAST"]]
    s["tāj+"] = [["tāj"],["RINF-C2","RINF-C3"]]
    s["tājs1s+"] = [("s","a","am","u","ā",""),["tāj+","āj+","ēj+"]]
    s["tājs1p+"] = [("i","u","iem","us","os"),["tāj+","āj+","ēj+"]]
    s["tājs4s+"] = [("a","as","ai","u","ā"),["tāj+","āj+","ēj+"]]
    s["tājs4p+"] = [["as","u","ām","ās"],["tāj+","āj+","ēj+"]]
    s["tājs+"] = [[None],["tājs1s+","tājs1p+","tājs4s+","tājs4p+"]]

    s["ien+"] = [["ien","en","iniec"],["RC"]]
    s["ieņ+"] = [["ieņ","eņ","inieč"],["RC"]]
    s["niec+"] = [["niec"],["RK"]]
    s["nieč+"] = [["nieč"],["RK"]]
    s["iene5s+"] = [["e","es","i","ei","ē"],["ien+","niec+"]]
    s["iene5px+"] = [["es","ēm","ēs"],["ien+","niec+"]]
    s["iene5py+"] = [["u"],["ieņ+","nieč+"]]
    s["iene+"] = [[None],["iene5s+","iene5px+","iene5py+"]]

    s["iet+"] = [["iet","iķ"],["RC"]]
    s["ieš+"] = [["ieš","iķ"],["RC"]]
    s["ietis2sx+"] = [["is","im","i","ī"],["iet+"]]
    s["ietis2sy+"] = [["a"],["ieš+"]]
    s["ietis2p+"] = [["i","u","iem","us","os"],["ieš+"]]
    s["ietis5s+"] = [["e","es","i","ei","ē"],["iet+"]]
    s["ietis5px+"] = [["es","ēm","ēs"],["iet+"]]
    s["ietis5py+"] = [["u"],["ieš+"]]
    s["ietis+"] = [[None],["ietis2sx+","ietis2sy+","ietis2p+","ietis5s+","ietis5px+","ietis5py+"]]

    s["noun7"] = [[''],["R7"]]

    s["noun"] = [[None],["noun1","noun2","noun3","noun4","noun5","noun6","noun7",
      "šana","uks+","nīca+","iene+","ietis+","tājs+"]]

    s["__START__"] = [[None],["noun","verb","adjparticiple","numeral",
      "adverb","adverbšus","adverbtin","adverbin"]]

    return s

ignorelist1={}
ignorelist1["noun4ms"] = 1
ignorelist1["noun5ms"] = 1
ignorelist1["noun3fs"] = 1

ignorelist2={}
ignorelist2["NUM19"] = 1
ignorelist2["NUM29"] = 1

def append_parse_data(morpho,word0,data,attr=[0,0,0]):
    if attr[0]==1 and data[1][-1]=='': # empty endings not saved
        return
    if word0 not in morpho:
        morpho[word0] = {}
    woutput = morpho[word0]
    if data[1] not in woutput:
        woutput[data[1]] = []
    xoutput = woutput[data[1]]
    if data[0] not in xoutput:
        xoutput.append(data[0])

def parse_word_struct(word,key,vstruct,output,attr=[0,0,0],track=tuple(),wordtrack=tuple(),word0=None,prefix=""):
    if word0 is None:
        word0 = word
    if len(word)>30:
        return
    elif key=='E': # no symbol (until word start)
        if len(word)==0:
            if prefix!="":
                track = track + ("PREF",)
                wordtrack = wordtrack + (prefix,)
            append_parse_data(output,prefix+word0,[track,wordtrack],attr)
    elif key[:1].isupper():
        if attr[2]==1 and key in ignorelist2: # morphokeys to ignore
            pass
        elif root_check(word,key):
            if prefix!="":
                track = track + ("PREF",)
                wordtrack = wordtrack + (prefix,)
            append_parse_data(output,prefix+word0,[(key,)+track,(word,)+wordtrack],attr)
    elif key in vstruct:
        value = vstruct[key]
        seqs = value[0]
        nextkeys = value[1]
        for seq in seqs:
            if seq==None or len(seq)==0 or word[-len(seq):]==seq:
                if seq==None or len(seq)==0:
                    nextword = word
                else:
                    nextword = word[:-len(seq)]
                for nextkey in nextkeys:
                    if attr[1]==1 and nextkey in ignorelist1: # morphokeys to ignore
                        pass
                    else:
                        if seq==None:
                            parse_word_struct(nextword,nextkey,vstruct,output,attr,track,wordtrack,word0,prefix=prefix)
                        else:
                            parse_word_struct(nextword,nextkey,vstruct,output,attr,(key,)+track,(seq,)+wordtrack,word0,prefix=prefix)
    else:
        print('key not found:',key)

def save_morpho(morpho,foutname):
    with codecs.open(foutname, 'w', encoding='utf-8') as fout:
        for word in sorted(morpho):
            fout.write("* {}\n".format(word))
            woutput = morpho[word]
            for word1 in woutput:
                fout.write(" ** ")
                for word2 in word1:
                    fout.write("{}- ".format(word2))
                fout.write("\n")
                description = woutput[word1]
                for descr in description:
#                    dlen[len(descr)]+=1
#                    if len(descr)==4:
                    fout.write("      ")
                    for d in descr:
                        fout.write("{} ".format(d))
                    fout.write("\n")

def save_morpho_root(morphoroots,foutname):
    with codecs.open(foutname, 'w', encoding='utf-8') as fout:
        for root in sorted(morphoroots):
            fout.write("* {}\n".format(root))
            routput = morphoroots[root]
            for rtype in routput:
                fout.write(" ** {}\n".format(rtype))
                words = routput[rtype]
                for w in words:
                    fout.write("      {0}\n".format(w,words[w]))

def save_morpho_shifts(morphoshifts,foutname):
    with codecs.open(foutname, 'w', encoding='utf-8') as fout:
        for root in sorted(morphoshifts):
            fout.write("* {}\n".format(root))
            routput = morphoshifts[root]
            fout.write("    ")
            for rootplus in routput:
                fout.write("{} ".format(rootplus))
            fout.write("\n")

def save_morpho_rwords(morphorwords2,foutname):
    with codecs.open(foutname, 'w', encoding='utf-8') as fout:
        for root in sorted(morphorwords2):
            fout.write("* {}\n".format(root))
            routput = morphorwords2[root]
            for rw in routput:
                fout.write(" ** {}\n".format(rw))
                fout.write("      ")
                for d in morphorwords2[root][rw]:
                    fout.write("{} ".format(d))
                fout.write("\n")

def load_morpho(finname):
    morpho = {}
    with codecs.open(finname, 'r', encoding='utf-8') as fin:
        for line in fin:
            s = line.split()
            if s[0]=='*':
                word = s[1]
                if word not in morpho:
                    morpho[word] = {}
                woutput = morpho[word]
            elif s[0]=='**':
                word1 = tuple([x[:-1] for x in s[1:]])
                if word1 not in woutput:
                    woutput[word1] = []
                xoutput = woutput[word1]
            else:
                descr = tuple(s)
                xoutput.append(descr)
    return morpho
  
def extract_morpho(words,vstruct,attr):              
    morpho = {}
    for word in words:  
        if word.isalpha():
            parse_word_struct(word.lower(),"__START__",vstruct,morpho,attr)
    return morpho

def add_to_struct_d2(sh,k1,k2):
    if k1 not in sh:
        sh[k1] = {}
    sh[k1][k2] = 1

def extract_morpho_prefixes(words,vstruct,attr=[0,0,0]):              
    morpho = {}
    vocp = {}
    for word in words:  
        add_to_struct_d2(vocp,word,"")
        word = word.lower()
        if word.isalpha():
            parse_word_struct(word.lower(),"__START__",vstruct,morpho,attr)
            for p in prefixes3:
                if word[:len(p)]==p:
                    parse_word_struct(word[len(p):],"__START__",vstruct,morpho,attr,prefix=p)
                    add_to_struct_d2(vocp,word[len(p):],p)
    return morpho,vocp

def extract_morpho_root(morpho):              
    mr = {}
    mrw = {}
    for word in morpho:
        woutput = morpho[word]
        for word1 in woutput:
            description = woutput[word1]
            root = word1[0]
            for descr in description:
                d = descr[0]
                if d[0]=='R' or d[:3]=='NUM':
                    if root not in mr:
                        mr[root] = {}
                        mrw[root] = {}
                    if d not in mr[root]:
                        mr[root][d] = Counter()
                    if word not in mrw[root]:
                        mrw[root][word] = Counter()
                    mr[root][d][word]+=1
                    mrw[root][word][d]+=1
    return mr,mrw

def extract_morpho_shifts(morphoroots,rtypes,shf,spos):              
    msh = {}
    for root in morphoroots:
        rootok = False
        for rt in rtypes:
            if rt in morphoroots[root]:
                rootok = True
                break
        if rootok:
            found = False
            for num in range (shf['__MAX_LEN__'],-1,-1):
                if num==0: c = ""
                else: c = root[-num:]
                if c in shf:
                    if len(c)==num:
                        for scheme in shf[c]:
                            cplus = scheme[spos]
                            if num==0: rootplus = root+cplus
                            else: rootplus = root[:-num]+cplus
                            if is_good_part_generic(rootplus):
                                if root not in msh:
                                    msh[root] = {}
                                msh[root][rootplus] = 1
                                found = True
                if found: break
    return msh

def add_to_struct_k3(sh,k1,k2,k3,data):
    if k1 not in sh:
        sh[k1] = {}
    if k2 not in sh[k1]:    
        sh[k1][k2] = {}
    if k3 not in sh[k1][k2]:
        sh[k1][k2][k3] = []    
    if data not in sh[k1][k2][k3]:
        sh[k1][k2][k3].append(data)

def add_to_struct_k2(sh,k1,k2,data):
    if k1 not in sh:
        sh[k1] = {}
    if k2 not in sh[k1]:    
        sh[k1][k2] = []
    if data not in sh[k1][k2]:
        sh[k1][k2].append(data)

#def add_to_struct_k20(sh,k1,k2,data,k10=[0.0,0.0,0],k20=[0.0,0.0,0.0,{}]):
#    if k1 not in sh:
#        k10a = tuple(k10)
#        sh[k1] = [list(k10a),{}]
#    if k2 not in sh[k1][1]:    
#        k20a = tuple(k20)
#        sh[k1][1][k2] = [list(k20a),[]]
#    if data not in sh[k1][1][k2][1]:
#        sh[k1][1][k2][1].append(data)

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

def add_to_struct_k1(sh,k1,data):
    if k1 not in sh:
        sh[k1] = []
    if data not in sh[k1]:
        sh[k1].append(data)

def extract_main_root0(mainroots,mrs2,root,roottype,bigscheme,mainposes):
    # bigscheme(all) -> specscheme(C1A) -> posscheme(C1A[0..n-1]) -> keyscheme -> linescheme
#    print("root",root)
    for shname in bigscheme: # C1AI, C1A0, ...
#        if shname!='C2': continue # @@@@@@@@@@@@@@
        specscheme = bigscheme[shname]
        shtypes = specscheme[0]['__RTYPES__']
        rtposs = {}
        for shpos in range(len(shtypes)):
#            print(shtypes)
            if roottype in shtypes[shpos]:
                rtposs[shpos]=1
#        print("rtposs",roottype,rtposs,shpos)
        for shpos in rtposs: # scheme positions, containing roottype
            posscheme = specscheme[shpos] # scheme, relative to pos
#            print("=/////=posscheme KEYS",list(posscheme.keys()))
#            print("==__MAX_LEN__",posscheme['__MAX_LEN__'])
            for klen in range (posscheme['__MAX_LEN__'],-1,-1):
                sfound = False # if found with n characters, won't check for n-1 characters
                if klen==0: shkey = ""
                else: shkey = root[-klen:] # pattern
                if shkey in posscheme: # forall pattern scheme lists
                    if len(shkey)==klen:
                        for linescheme in posscheme[shkey]: # old characters
                            mainrootvalid = True
                            rootmain = tuple([])
#                            print("@",root,mainposes,shname)
                            for mainpos in mainposes:
                                shkeymain = linescheme[mainpos] # new characters for main form
                                if klen==0: rootmain0 = root+shkeymain
                                else: rootmain0 = root[:-klen]+shkeymain # hypothetic main form
#                                print("###",root,rootmain0)
                                mainrootvalid0 = False
                                for rts in shtypes[mainpos]: # main position
#                                    print("CHECK",rootmain0,rts)
                                    if root_check(rootmain0,rts):
                                        mainrootvalid0 = True
                                        break
                                if mainrootvalid0 == False:
                                    mainrootvalid = False
                                    break
                                rootmain+=(rootmain0,)
                            if len(rootmain)<=1:
                                if roottype in nrtypes:
                                    rootmain+=('N',)
                                elif roottype in numrtypes:
                                    rootmain+=('NUM',)
                            if mainrootvalid:
                                sfound = True
#                                print(" * found",root,rootmain,klen)
                                add_to_struct_k3(mainroots,root,rootmain,(shname,shpos),roottype)
                                add_to_struct_k3(mrs2,rootmain,root,(shname,shpos),roottype)
                if sfound: break

def extract_main_roots(mainroots,mrs2,morphoroots,bigscheme,rtstartlist,
        zeroroots=True,present=True,
        exlist=[],forcelist=[],mainposes=(4,)):              
    for root in morphoroots:
        rdata = morphoroots[root]
        for roottype in rdata:
            if (roottype in forcelist or
                (zeroroots or roottype[-1:]!="0") and 
                (present or roottype[:3]!="RPC") and
                 roottype not in exlist):
                if roottype in rtstartlist:
                    extract_main_root0(mainroots,mrs2,root,roottype,bigscheme,mainposes)
    return mainroots,mrs2

def extract_main_roots_all(roots,shift,shiftn,shiftnum,vrtypes,nrtypes,numrtypes):
    mainroots = {}
    mrs2 = {}
    # extract_main_roots: generates potential main-roots for each root regarding schemes
    extract_main_roots(mainroots,mrs2,roots,shift,vrtypes,exlist=[],zeroroots=True,mainposes=(0,4)) # verbs
    extract_main_roots(mainroots,mrs2,roots,shiftn,nrtypes,zeroroots=True,mainposes=(0,)) # nouns+adjectgives
    extract_main_roots(mainroots,mrs2,roots,shiftnum,numrtypes,zeroroots=False,mainposes=(0,)) # numerals
    return mainroots,mrs2

def save_morpho_cross(morphoroots,foutname):
    with codecs.open(foutname, 'w', encoding='utf-8') as fout:
        for root in sorted(morphoroots):
            fout.write("* {}\n".format(root))
            routput = morphoroots[root]
            for rtype in routput:
                fout.write(" ** {}\n".format(rtype))
                words = routput[rtype]
                for w in words:
                    fout.write("      {0} {1} {2}\n".format(w[0],w[1],words[w]))
                    
def extract_main_forms(mforms,mfs2,morpho,mainroots,voc,wholew=True):   
    # morpho - potential split-schemes; cmsh - potential main forms by roots
    for word in morpho: # raw word
        woutput = morpho[word]
        for spword in woutput: # word, split into parts
            root = spword[0]
            morpho_rtypes = {} # root types and split-schemes for concrete split-word in morpho
            if root in mainroots:
                for spscheme in morpho[word][spword]:
                    roottype = spscheme[0]
                    if roottype not in morpho_rtypes:
                        morpho_rtypes[roottype]=[]
                    if spscheme not in morpho_rtypes[roottype]:
                        morpho_rtypes[roottype].append(spscheme)
                for mainroot in mainroots[root]: # main form
                    # for each mainroot for root:
                    # collect rootypes which are both in morpho_rtypes and mainroots[root][mainroot]
                    # and add split-info and shift-info
                    rtypesplus = {} # root types, mainroots and shift-schemes
                    for shinfo in mainroots[root][mainroot]:
                        rtypeslist=mainroots[root][mainroot][shinfo]
                        for roottype in rtypeslist:
                            if roottype in morpho_rtypes:
                                splitschemes=morpho_rtypes[roottype]
                                rtypesplus[roottype]=(splitschemes,shinfo)
                    for roottype in rtypesplus:
                        splitschemes = rtypesplus[roottype][0]
                        schinfo = rtypesplus[roottype][1]
                        shname = schinfo[0]
                        rgspschemes = {} # local (word/spword/root/main-root/roottype) root-group-split-schemes
                        if mainroot[1]=='NUM': # numeral
                            for spscheme in splitschemes:
                                if len(spscheme)>1:
                                    add_to_struct_k1(rgspschemes,'NUM',spscheme)
                                    add_to_struct_k1(rgspschemes,'R1',spscheme)
                                    add_to_struct_k1(rgspschemes,'R4',spscheme)
                        elif mainroot[1]=='N': # noun+
                            if roottype in ["RK","RC","RČ","REN"]:
                                for spscheme in splitschemes:
                                    if len(spscheme)>1:
                                        if spscheme[1] in ["noun1šs","noun1ss","noun1š","noun1šš","noun1s","noun1p"]:
                                            add_to_struct_k1(rgspschemes,'R1',spscheme)
                                        elif spscheme[-1] in ["noun1šs","noun1ss","noun1š","noun1šš","noun1s","noun1p"]:
                                            add_to_struct_k1(rgspschemes,'R1',spscheme)
                                            add_to_struct_k1(rgspschemes,'R3',spscheme)
                                        elif spscheme[1] in ["noun3s","noun3p"]:
                                            add_to_struct_k1(rgspschemes,'R3',spscheme)
                                        elif spscheme[1] in ["noun3fs","noun3fp"]:
                                            add_to_struct_k1(rgspschemes,'R3f',spscheme)
                                        elif spscheme[1] in ["noun4ms","noun4fs","noun4s","noun4p"]:
                                            add_to_struct_k1(rgspschemes,'R4',spscheme)
                                        elif spscheme[-1] in ["noun4ms","noun4fs","noun4s","noun4p",]:
                                            add_to_struct_k1(rgspschemes,'R4',spscheme)
                                            add_to_struct_k1(rgspschemes,'R6',spscheme)
                                        elif spscheme[-1] in ["noun2se","noun2sx","noun2sy","noun2p","noun2sxx"]:
                                            add_to_struct_k1(rgspschemes,'R2',spscheme)
                                        elif spscheme[-1] in ["noun5s","noun5ms","noun5fs","noun5px","noun5py"]:
                                            add_to_struct_k1(rgspschemes,'R5',spscheme)
                                        elif spscheme[1][:4]=="def1":
                                            add_to_struct_k1(rgspschemes,'A',spscheme)
                                            add_to_struct_k1(rgspschemes,'R1',spscheme)
                                            add_to_struct_k1(rgspschemes,'R4',spscheme)
                                        elif spscheme[1][:4]=="def4":
                                            add_to_struct_k1(rgspschemes,'A',spscheme)
                                            add_to_struct_k1(rgspschemes,'R1',spscheme)
                                            add_to_struct_k1(rgspschemes,'R4',spscheme)
                                if len(rgspschemes)==0:
                                    add_to_struct_k1(rgspschemes,'R1',spscheme)
                                    add_to_struct_k1(rgspschemes,'R2',spscheme)
                                    add_to_struct_k1(rgspschemes,'R3',spscheme)
                                    add_to_struct_k1(rgspschemes,'R4',spscheme)
                                    add_to_struct_k1(rgspschemes,'R5',spscheme)
                                    add_to_struct_k1(rgspschemes,'R6',spscheme)
                            elif roottype=="R10":
                                for spscheme in splitschemes:
                                    add_to_struct_k1(rgspschemes,'R1',spscheme)
                            elif roottype in ["R20","R2x","R2specx","R2y"]:
                                for spscheme in splitschemes:
                                    add_to_struct_k1(rgspschemes,'R2',spscheme)
                            elif roottype in ["R5x","R5y"]:
                                for spscheme in splitschemes:
                                    add_to_struct_k1(rgspschemes,'R5',spscheme)
                            elif roottype in ["R6x","R6y"]:
                                for spscheme in splitschemes:
                                    add_to_struct_k1(rgspschemes,'R6',spscheme)
                            elif roottype=="R7":
                                for spscheme in splitschemes:
                                    add_to_struct_k1(rgspschemes,'R7',spscheme)
                            else:
                                print('No such roottype',roottype)
                                for spscheme in splitschemes:
                                    add_to_struct_k1(rgspschemes,'RK',spscheme)
                        else: # verb
                           for spscheme in splitschemes:
                               add_to_struct_k1(rgspschemes,shname,spscheme)
                        for rgroup in rgspschemes:
                            if shname[0]=='C': # verb
                                mainform=(mainroot[0],mainroot[1],rgroup)
                            else: # not verb (noun, num)
                                mainform=(mainroot[0],"*",rgroup)
                            data = rgspschemes[rgroup]
                            add_to_struct_k30(mforms,mainform,word,spword,data)
                            add_to_struct_k30(mfs2,word,mainform,spword,data)
    # whole word adding to mainroots
    if wholew:
        if len(mfs2)<100: wordtmprepo = mfs2 # just for testing
        else: wordtmprepo = voc # default case: some of the words of voc not found in wrepo (e.g. 'i')
        for word in wordtmprepo: # adding whole words to the structure
            if word.isalpha():
                mainform = (word,"*","W")
                spword = (word,'')
                splitschemes = [('W','')]
                data = splitschemes
                add_to_struct_k30(mforms,mainform,word,spword,data)
                add_to_struct_k30(mfs2,word,mainform,spword,data)
    return mforms,mfs2

def analyze_main_forms_1(mforms):
    for mf in mforms:
        if mf[1]=='*' and mf[2]=="W": # Whole word (kas, ko, kāpēc, laikam, jeb)
            wordrate = 1.6
            word = mf[0]
            mforms[mf][1][word][0][0] = wordrate
            mforms[mf][0][0] = wordrate
        else:
            for word in mforms[mf][1]:
                wordrate = 0.0
                for spword in mforms[mf][1][word][1]:
                    for spscheme in mforms[mf][1][word][1][spword]:
                        roottype = spscheme[0]
                        if mf[1]!='*': # verb
                            if roottype in ["RK","RC"]: # connection to nouns
                                wr0 = 0.1
                            elif roottype[-1] == "0": # no ending (2nd, 3rd person, present)
                                wr0 = 0.1
                            elif roottype == "RPAST":
                                wr0 = 0.2
                            elif roottype[:9] == "RPASSPAST":
                                wr0 = 0.1
                            elif roottype in ["RFUTAS","RFUTS"]:
                                wr0 = 0.1
                            elif roottype in ["RPC2-P23-A"]:
                                wr0 = 0.1
                            elif roottype in ["RPC3-AM","RPC3-AM","RPC3-P12-S","RPC3-P3-A"]:
                                wr0 = 0.1
                            else: # verb form with ending
                                wr0 = 0.5
                        elif mf[2][0]=='A': # adjective
                            wr0 = 1.0
                        elif mf[2]=='R7': # foreign inflective noun
                            wr0 = 1.85
                        elif mf[2] in ["R1","R2","R3","R3f","R4","R5","R6"]: # other (flective) nouns
                            if roottype[-1] == "0":
                                wr0 = 0.05
                            else:
                                wr0 = 1.0
                        elif mf[2]=='NUM': # numerals
                            wr0 = 1.0
                        else:
                            print("No such root-group",mf[2])
                        wordrate = max(wordrate,wr0)
                mforms[mf][1][word][0][0] = wordrate
                mforms[mf][0][0] += wordrate

def analyze_main_forms_2(mforms,mfs2):
    # write basic mainrates to mfs2
    for mf in mforms:
        for word in mforms[mf][1]:
            mfs2[word][1][mf][0][0] = mforms[mf][0][0]
            mfs2[word][0][0] = max(mfs2[word][0][0],mfs2[word][1][mf][0][0])
            
def process_spword(spscheme0,spw):
    # mācī-ja => māc-īja
    if (spscheme0[0][-2:]=='OJ'
        and is_good_part_generic(spw[0][:-2])
        and len(spscheme0)>=2 and spscheme0[1]!='PREF'):
        spw = (spw[0][:-2],spw[0][-2:]+spw[1]) + spw[2:]
    # mācī-t => māc-īt
    elif (spscheme0[0] in ["RPASSPAST-C2","RPASSPAST-C3","RINF-C2","RINF-C3","RFUTA","RFUTAS","RŠANA","RDAMA"]
          and is_good_part_generic(spw[0][:-1])
          and spw[0][-2:] not in ["ie","au"]
          and len(spscheme0)>=2 and spscheme0[1]!='PREF'):
        spw = (spw[0][:-1],spw[0][-1:]+spw[1]) + spw[2:]
    rpos = 0
    if spscheme0[-1]=='PREF':
        spw = ('@'+spw[-1],)+spw[:-1]
        rpos=1
    if len(spw)>rpos+1:
        spw = spw[:rpos+1] + (''.join(spw[rpos+1:]),)
    
    return spw

def analyze_spwords_1(mfs2):
    sprates = {}
    for word in mfs2:
        if word not in sprates:
            sprates[word] = {}
        for mf in mfs2[word][1]:
            for spword in mfs2[word][1][mf][1]:
                spscheme0 = mfs2[word][1][mf][1][spword][0]
                spw2 = process_spword(spscheme0,spword)
                mfrate = mfs2[word][1][mf][0][0] + 0.01*len(spw2[-1])
                if spw2 not in sprates[word]:
                    sprates[word][spw2] = 0.0
                if mfrate>sprates[word][spw2]:
                    sprates[word][spw2] = mfrate
                break
    return sprates

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
                
def load_main_forms_from_struct_reverse(repo):
    repo2 = {}
    for e1 in repo:
        for e2 in repo[e1][1]:
            for e3 in repo[e1][1][e2][1]:
                for ee in repo[e1][1][e2][1][e3]:
                    add_to_struct_k30(repo2,e2,e1,e3,[ee])
    return repo2
                
def load_main_forms(fin,reverse=False):
    lopen = False
    if isinstance(fin,str): 
        fin = codecs.open(fin, 'r', encoding='utf-8')
        lopen = True
    repo = {}
    k1 = ''
    k2 = ''
    k3 = ''
    data = ''
    k10 = [0.0]
    k20 = [0.0]
#    with codecs.open(finname, 'r', encoding='utf-8') as fin:
    for line in fin:
        s = line.split()
        if s[0]=='*':
            if len(s)==3:
                k1=s[1]
            else:
                k1 = tuple(s[1:-1])
            k10[0]=float(s[-1])
        elif s[0]=='**':
            if len(s)==3:
                k2=s[1]
            else:
                k2 = tuple(s[1:-1])
            k20[0]=float(s[-1])
        elif s[0]=='-':
            k3 = tuple([f[:-1] for f in s[1:]])
        elif s[0]=='+':
            data = [tuple([f[:-1] for f in s[1:]])]
            if reverse:
                add_to_struct_k30(repo,k2,k1,k3,data,k10,k20)
            else:
                add_to_struct_k30(repo,k1,k2,k3,data,k10,k20)
    if lopen:
        fin.close()
    return repo

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
#        for e2all in sorted(repo[e1].items(), key=lambda x: x[1], reverse=True):
#            e2 = e2all[0]
#            if tech:
#                fout.write("  ** {} {}\n".format(" ".join(e2).rstrip(),repo[e1][e2]))
#            else:
#                fout.write("  ** {} <{:.2f}>\n".format(e2,repo[e1][e2]))
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
                    
def load_spwords(fin):
    repo = {}
    lopen = False
    if isinstance(fin,str): 
        fin = codecs.open(fin, 'r', encoding='utf-8')
        lopen = True
    for line in fin:
        s = line.split()
        repo[s[0]] = tuple(s[1:])
    if lopen:
        fin.close()
    return repo

def load_sprates(fin):
    repo = {}
    lopen = False
    k1 = ''
    if isinstance(fin,str): 
        fin = codecs.open(fin, 'r', encoding='utf-8')
        lopen = True
    for line in fin:
        s = line.split()
        if s[0]=='*':
            k1=s[1]
            if k1 not in repo:
                repo[k1] = {}
        elif s[0]=='**':
            k2=tuple(s[1:-1])
            v2 = float(s[-1])
            repo[k1][k2] = v2
    if lopen:
        fin.close()
    return repo

def check_rtypes(vrt,vs):
    vrtmain = {}
    for k in vs:
        for rt in vs[k][1]:
            vrtmain[rt]=1
    for k in vrt:
        if k not in vrtmain:
            print("Root type specified in scheme not found in structure",k)

def extract_main_forms_final(mforms,mfs2,corpus,mstr=""):
    fvocab = extract_frequent_vocabulary(corpus,0,True,False)
    vstruct = create_morpho_struct_lv()
    check_rtypes(vrtypes,vstruct)
    check_rtypes(nrtypes,vstruct)
    check_rtypes(numrtypes,vstruct)
    words = list(fvocab.keys())
    morpho,vocp = extract_morpho_prefixes(words,vstruct)
    roots,roots2 = extract_morpho_root(morpho)
    mainroots,mrs2 = extract_main_roots_all(roots,shift,shiftn,shiftnum,vrtypes,nrtypes,numrtypes)
    extract_main_forms(mforms,mfs2,morpho,mainroots,fvocab)
    if isinstance(mstr,str)==False or mstr!="":
        save_main_forms(mforms,mstr,True)
        
def load_learned_forms(mstr):
    mforms = load_main_forms(mstr)                
    mfs2 = load_main_forms_from_struct_reverse(mforms)
    return mforms,mfs2

def load_learned_and_extract_main_forms(mstr,corpus):
    if isinstance(mstr,str)==True and mstr=="":
        mforms = {}
        mfs2 = {}
    else:
        mforms,mfs2 = load_learned_forms(mstr)
    extract_main_forms_final(mforms,mfs2,corpus)
    return mforms,mfs2

def analyze_main_forms(mforms,mfs2,fspw="",mstr="",fspr=""):
    analyze_main_forms_1(mforms)
    analyze_main_forms_2(mforms,mfs2)
    sprates = analyze_spwords_1(mfs2)
    spwords = analyze_spwords_2(sprates)
    if isinstance(mstr,str)==False or mstr!="":
        save_main_forms(mforms,mstr,True)
    if isinstance(fspw,str)==False or fspw!="":
        save_spwords(spwords,fspw,True)
    if isinstance(fspr,str)==False or fspr!="":
        save_sprates(sprates,fspr,True)
    return spwords

def load_learned_and_analyze_main_forms(mstr,corpus,fspw=""):
    mforms,mfs2=load_learned_and_extract_main_forms(mstr,corpus)
    spwords = analyze_main_forms(mforms,mfs2,fspw=fspw)
    return spwords

def load_learned_and_analyze_main_forms_self(mstr,fspw=""):
    mforms,mfs2=load_learned_forms(mstr)
    spwords = analyze_main_forms(mforms,mfs2,fspw=fspw)
    return spwords

def isUlower(word):
    return len(word)>=2 and word[0:1].isupper() and word[1:].islower()

def segment_word(spwords,word,marker1,marker2,prefspecial=0,generic=False):
    lword = word.lower()
    if word.isalpha() == False:
        spw = [word]
    elif lword in nonseg:
        spw = [word]
    elif word.islower()==False and isUlower(word)==False:
        spw = [word]
    elif word.lower() in spwords:
        spw = list(spwords[lword])
        suffnum = 1
        if spw[0][0]=='@': # prefix
            if prefspecial==2: # prefix added to root
                spw[1] = spw[0][1:] + spw[1]
                spw = spw[1:]
            elif prefspecial==1 and generic: # prefix added to root
                spw[1] = spw[0][1:] + spw[1]
                spw = spw[1:]
            elif prefspecial==1: # only 'ne'/'jā' is splitted away, the rest is added to the root
                if spw[0] in ["@ne","@jā"]:
                    spw[0] = spw[0][1:]+marker1
                    suffnum = 2
                elif spw[0][:3] in ["@ne","@jā"]: # 'ne'/'jā'+another prefix
                    spw[0] = spw[0][1:3]+marker1
                    spw[1] = spw[0][3:]+spw[1]
                    suffnum = 2
                else: # prefix added to root
                    spw[1] = spw[0][1:] + spw[1]
                    spw = spw[1:]
            else:
                spw[0] = spw[0][1:]+marker1
                suffnum = 2
        if len(spw)>=suffnum+1:
            spw[suffnum] = marker1+spw[suffnum]
        if isUlower(word):
            spw = [marker2] + spw
    else:
        if isUlower(word):
            spw = [marker2,word.lower()]
        else:
            spw = [lword]
    return spw
def segment_line(spwords,sentence,marker1,marker2,prefspecial=False,generic=False):
    sseg = []
    for word in sentence.split():
        sseg += segment_word(spwords,word,marker1,marker2,prefspecial,generic)
    return " ".join(sseg)

def segment_document(fin,fout,spwords,marker1,marker2,prefspecial=False,generic=False):
    if marker1.isdigit(): marker1 = chr(int(marker1))
    if marker2.isdigit(): marker2 = chr(int(marker2))
    lopenin = False
    lopenout = False
    if isinstance(fin,str): 
        fin = codecs.open(fin, 'r', encoding='utf-8')
        lopenin = True
    if isinstance(fout,str): 
        fout = codecs.open(fout, 'w', encoding='utf-8')
        lopenout = True
    for s in fin:
        fout.write("{}\n".format(segment_line(spwords,s,marker1,marker2,prefspecial,generic)))
    if lopenin:
        fin.close()
    if lopenout:
        fout.close()
        
def unprocess_line(sentence,marker1,marker2):
    output = []
    len1 = len(marker1)
    upper = False
    prev = ""
    for word in sentence.split():
        # uppercase marking
        if word==marker2:
            upper=True
            continue
        elif upper:
            word = word[0].upper() + word[1:]
            upper = False
        if word[-len1:]==marker1: # prefix
            prev = word[:-len1]
        elif word[:len1]==marker1: # postfix
            output[len(output)-1] += word[len1:]
        else:
            output.append(prev+word)
            prev = ""
    return ' '.join(output)

# code 9474: '│'; code 9553: '║'
def unprocess_doc(infile,outfile,marker1="9474",marker2="9553"):
    if marker1.isdigit(): marker1 = chr(int(marker1))
    if marker2.isdigit(): marker2 = chr(int(marker2))
    for line in infile:
        outfile.write(unprocess_line(line,marker1,marker2).strip())
        outfile.write(' \n')
