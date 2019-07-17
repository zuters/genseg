    #!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Janis Zuters

#from verbroot_data import mm

vowels_lv=u"aāeēiīoōuū";
vowdict_lv={}
for v in vowels_lv:
    vowdict_lv[v]=1

def is_lv_noun_m(word):
    word = word.lower()
    if len(word)>=3 and word[-1]=="s" and word[-2] not in vowdict_lv: return True
    else: return False

vowels=u"aāeēiīoōuūy";
vowdict={}
for v in vowels:
    vowdict[v]=1

sgstart = {}
sgstart["br"] = 1
sgstart["sk"] = 1
sgstart["st"] = 1
sgstart["sp"] = 1
sgstart["pr"] = 1
sgstart["gr"] = 1
sgstart["kl"] = 1
sgstart["kr"] = 1
sgstart["skr"] = 1
sgstart["spr"] = 1
sgstart["str"] = 1

prefixes = {}
prefixes["pa"] = 1
prefixes["sa"] = 1
prefixes["no"] = 1
prefixes["ne"] = 1
prefixes["ie"] = 1
prefixes["at"] = 1
prefixes["iz"] = 1
prefixes["pie"] = 1
prefixes["pār"] = 1
prefixes["ap"] = 1
prefixes["uz"] = 1
prefixes["aiz"] = 1

prefixes2 = {} # without 'ne'
prefixes2["pa"] = 1
prefixes2["sa"] = 1
prefixes2["no"] = 1
prefixes2["ie"] = 1
prefixes2["at"] = 1
prefixes2["iz"] = 1
prefixes2["pie"] = 1
prefixes2["piepa"] = 1
prefixes2["pār"] = 1
prefixes2["ap"] = 1
prefixes2["uz"] = 1
prefixes2["aiz"] = 1

prefixes3 = {}
prefixes3["ne"] = 1
for p in prefixes2:
    prefixes3["ne"+p] = 1
    prefixes3[p] = 1
    


def sounds_good_start(w):
    if len(w)==1 or w in sgstart:
        return True
    else: return False

def get_right_tuple(word):
    ret = ["","","",""]
    if word[-1:] in vowdict_lv:
        pos = 1
        if word[-2:-1] in vowdict_lv:
            pos = 2
        ret[3] = word[-pos:]
        pos0 = pos
        pos += 1
        if len(word)>=pos:
            while len(word)>=pos and word[-pos:-pos+1] not in vowdict_lv:
                pos +=1
            ret[2] = word[-pos+1:-pos0]
            pos0 = pos-1
            if word[-pos:-pos+1] in vowdict_lv:
                if word[-pos-1:-pos] in vowdict_lv:
                    pos += 1
                ret[1] = word[-pos:-pos0]
                ret[0] = word[:-pos]
    return tuple(ret)

def tuple_prefix(t):
    if t[1] in prefixes and sounds_good_start(t[2]): return True
    if t[1]+t[2][:1] in prefixes and sounds_good_start(t[2][1:]): return True
    if t[1]+t[2][:1] in prefixes and t[2][1:]=="" and len(t[3])==2: return True # uziet, uzaut
    if t[0][-1:]+t[1]+t[2][:1] in prefixes and sounds_good_start(t[2][1:]): return True
    if t[0][-1:]+t[1] in prefixes and sounds_good_start(t[2]): return True
    if t[0][-1:]+t[1] in prefixes and t[2]=="" and len(t[3])==2: return True # paiet pieiet
    return False
    
def containsvowel(word):
    for s in word:
        if s in vowdict: return True
    return False

def is_good_part_generic(part):
    return (
        part.isalpha()
        and part.islower()
        and containsvowel(part)
    )
    
def is_good_root_lv(word):
    if len(word)<2: return False
    if word[-1:] in vowdict: return False
    if word[-2:] in ['jš','ss','šs','zd','sd']: return False
    if word[-3:] in ['ieš']: return False
    if word[-4:] in ['nieč','tājs','tāju','ītāj','otāj']: return False
    if word[-5:] in ['ietis','ietim',"iešus","iešos","ietēm","ietēs",'tājam']: return False
    if word[-5:] in ['tājus','tājām','tājas','tājās','amies','iniek']: return False
    if word[-6:] in ['iešiem','tājiem','inieks']: return False
    return is_good_part_generic(word)

def is_good_verb_root_lv(root):
    if len(root)<2: return False
    if root[-1:] in vowdict: return False
    if root[-2:] in ["aj","šs","ām","am"]: return False
    if root[-2:] in ("āj","ēj","īj","oj","ūj"): return False
    if root[-2:] in ['jš','ss','šs','zd']: return False
    if root[-3:] in ["ūgs"]: return False
    if root[-3:] in ['ieš']: return False
    if root[-4:] in ["ējam","ējat"]: return False
    if root[-4:] in ['nieč','tājs','tāju','ītāj','otāj']: return False
    if root[-5:] in ['ietis','ietim',"iešus","iešos","ietēm","ietēs",'tājam']: return False
    if root[-5:] in ['tājus','tājām','tājas','tājās','amies','iniek']: return False
    if root[-6:] in ['iešiem','tājiem','inieks']: return False
    return is_good_part_generic(root)

def is_good_verb_root_present_lv(root):
    if len(root)<2: return False
    if root[-5:] in ['kremt']: return True
    if root[-1:] in vowdict: return False
    if root[-1:] in ['ķ','ņ']: return False
    if root[-2:] in ["aj","šs","lt","bt","gt","kt","pt","mt","rt","ūm","ām","or","ār",
           "um",'īg','ūv','āv','ut','ag','ēs','uv','eb','āp','kd','gd','īd']: return False
    if root[-2:] in ['ik','ig','id','im'] and root[-3:-2] not in ['a','e']: return False
    if root[-2:] in ['up','uš','us','ud'] and root[-3:-2] not in ['a']: return False
    if root[-2:] in ("īj","oj","ūj"): return False
    if root[-3:] in ['aun','jus','juš','jis','ilk','irk','irp','iez','irs','dam']: return False
    if root[-4:] in ["ējam","ējat","dams"]: return False
    return is_good_part_generic(root)

def check_root_general_lv(word):
    if word[-2:] in ['jš','ss','šs','zd']: return False
    if word[-3:] in ['ieš']: return False
    if word[-4:] in ['nieč','tājs','tāju','ītāj','otāj']: return False
    if word[-5:] in ['ietis','ietim',"iešus","iešos","ietēm","ietēs",'tājam']: return False
    if word[-5:] in ['tājus','tājām','tājas','tājās','amies','iniek']: return False
    if word[-6:] in ['iešiem','tājiem','inieks']: return False
    return True

def root_check(word,key):
# ================================== NOUN ============================
    if key in ['RC']: # is_good_root_lv
        if word[-1:] in ['k','g']: return False
        if word[-2:] in ['ss']: return False
        if is_good_root_lv(word):
            if check_root_general_lv(word):
                return True
    elif key in ['RK','R10']: # is_good_root_lv
        if len(word)<2: return False
        if word[-1:] in ['ķ']: return False
        if word[-2:] in ['bj','pj','mj','vj']: return False
        if word[-2:] in ['ss']: return False
        if is_good_part_generic(word)==False: return False
        if is_good_root_lv(word):
            if check_root_general_lv(word):
                return True
    elif key=='R2specx': # akmen
        if check_root_general_lv(word):
            if word[-3:] in ["sun"]: return True
            if word[-4:] in ["ūden"]: return True
            if word[-5:] in ["asmen","akmen","ruden","ziben","mēnes"]: return True
    elif key=='REN': # īlen(tiņš), degun(tiņš)
        if check_root_general_lv(word):
            if word[-1:] in ["n"]: return True
            if word[-2:] in ["es"]: return True
    elif key=='R20': # brāl! akmen! mēnes!
        if word[-3:] in ["ais","īgs"]: return False
        if word[-4:] in ["isks"]: return False
        if is_good_root_lv(word):
            if (word[-1:] in ['l','n','s'] and
                check_root_general_lv(word)):
                return True
    elif key in ['R2x','R5x']: # loc(is), bried(is)
        if word[-3:] in ["ais","īgs"]: return False
        if word[-4:] in ["isks"]: return False
        if is_good_root_lv(word):
            if (word[-1:] not in ['č','ž','g','j','k','ļ','ņ','š','ž'] and
                check_root_general_lv(word)):
                return True
    elif key in ['R2y','R5y','RČ']: # loč(a), briež(a)
        if word[-3:] in ["ais","īgs"]: return False
        if word[-4:] in ["isks"]: return False
        if is_good_root_lv(word):
            if (word[-1:] not in ['b','c','g','k','l','m','n','p','s','v','z'] and
                (word[-1:] not in ['j'] or word[-2:] in ['bj','mj','pj','vj']) and
                word[-2:] not in ['kt'] and
                check_root_general_lv(word)):
                return True
    elif key=='R6x': # krāsn(s), dzelz(s)
        if word[-3:] in ["ais","īgs"]: return False
        if word[-4:] in ["isks"]: return False
        if is_good_root_lv(word):
            if (word[-1:] in ['c','n','s','v','t','z','l','d'] and
                check_root_general_lv(word)):
                return True
    elif key=='R6y': # krāšņ(u), dzelž(u)
        if word[-3:] in ["ais","īgs"]: return False
        if word[-4:] in ["isks"]: return False
        if len(word)<2: return False
        if word[-1:] in ['ķ']: return False
        if word[-2:] in ['bj','pj','mj','vj']: return False
        if is_good_part_generic(word)==False: return False
        if is_good_root_lv(word):
            if (word[-1:] in ['c','ņ','s','š','j','t','ž','ļ'] and
                check_root_general_lv(word)):
                return True
    elif key=='R7': # Eriā, guru
        if len(word)>=2 and word[-1:] in ['ā','ē','i','ī','o','u','ū']:
            return True

# ================================== NUMERIC ================================
    elif key=='NUM19':
        if word in ["vien","div","trīs","četr","piec","seš","septiņ","astoņ","deviņ"]:
            return True
    elif key=='NUM29':
        if word in ["div","trīs","četr","piec","seš","septiņ","astoņ","deviņ"]:
            return True

# ================================== VERB INF ================================
    elif key=='RINF-C1-C' or key=='RPASSPAST-C1-C':
        if is_good_verb_root_lv(word):
            return True
    elif key=='RINF-C1' or key=='RPASSPAST-C1':
#        return True
        if len(word)<=1: return False
        t = get_right_tuple(word)
#        print(t)
        if t[3] not in ("ie","au","ā","ē","ī","o","ū"): return False
        if t[1] in ['a','ā','e','i','o','u','ai','ie'] and tuple_prefix(t)==False: return False
        if t[1] in ['ē','ī','ū']: return False
        if len(t[1])>1 and tuple_prefix(t)==False: return False
        if word in ["tā","tē","lā","pē","šī"]: return False
        if word[-2:-1] in ["h"]: return False
        if word[-3:-1] in ["oj","tp"]: return False
        if word[-2:] in ["lē","jū","kī","mī","mē","mū","sī","šā","zē","vē","rī","cī","vā","vē"]: return False
        if word[-3:] in ["jie","vie","tie","cie","īnā","kvā","blū","grē","jau","krī","kvī","lau","prā","spī","tau","tvī","nie"]: return False
        if word[-4:] in ["amie","atie","usie","šķie"]: return False
        return True
    elif key=='RINF-C2' or key=='RPASSPAST-C2':
        if len(word)<=1: return False
        t = get_right_tuple(word)
        if t[1]=='ai' and t[3]=='ē' and tuple_prefix(t)==True: return False
        if t[1]=='a' and t[3]=='ī': return False # 3C
        if t[1]=='ā' and t[3]=='ī': return False # 3C
        if t[1]=='a' and t[3]=='ā' and tuple_prefix(t)==True: return False # 12C
        if t[1]=='a' and t[3]=='ē' and tuple_prefix(t)==True: return False # 1C
        if t[1]=='i' and t[3]=='ā': return False # 3C
        for sw in ("ā","ē","ī","o"):
            if sw==word or len(word)>len(sw) and (sw==word[-len(sw):] 
            and word[-3:-1] not in ["oj","tp"]
            and word[-3:] not in ["jie","vie","cie","īnā","kvā","blū","ino"]
            and word[-4:] not in ["āmie","ātie","amie","atie","usie"]
            and word[-5:] not in ["jamie","jatie"]):
                return True
    elif key=='RINF-C3' or key=='RPASSPAST-C3':
        if len(word)<=1: return False
        t = get_right_tuple(word)
        if t[1]=='ai' and t[3]=='ē': return False
        if t[1]=='a' and t[3]=='ī' and tuple_prefix(t)==True: return False # 3C
        if t[1]=='ē' and t[3]=='ē': return False # 2C
        if t[1]=='a' and t[3]=='ē': return False # 12C
        for sw in ("ā","ē","ī"):
            if sw==word or len(word)>len(sw) and (sw==word[-len(sw):] 
            and word[-3:] not in ["vie","cie","ojo","īnā","kvā"]
            and word[-4:] not in ["āmie","ātie","amie","atie","usie"]
            and word[-5:] not in ["jamie","jatie"]):
                return True

# ================================== VERB PRESENT ============================
    elif key in ['RPC1-P1','RPC1-P1-AMIES']:
        if word[-2:] in ["ab","ap","av","am"]: return False
#        return True
        if is_good_verb_root_present_lv(word):
            return True
    elif key=='RPC1-P2-0':
        if word[-1:] in ['ļ','g']: return False
        if word[-2:] in ["aj","šs","lt","bt","gt","kt","pt","mt","rt","ūm","ām","ēt","ks","āt","ts",
               "bj","pj","mj","ot"]: return False
        if word[-3:] in ['tīt','jis','jam','ies','jas','aut','dam','cis','jot','kot']: return False
        if word[-4:] in ['ikas','dams','ošas']: return False
        if word[-5:] in ['ušiem','damas','kremt']: return False
        return is_good_verb_root_lv(word)
    elif key in ['RPC1-P3-0']:
        if word[-1:] in ['l']: return False
        if word[-2:] in ["aj","šs","lt","bt","gt","kt","pt","mt","rt","ūm","ām","ēt","ks","āt","ts",
               "dz",'ēl','īl','bj','pj','mj','vj','ēm']: return False
        if word[-3:] in ['tīt','jis','jam','ies','jas','aut','dam','cis','jot','kot','ilp']: return False
        if word[-4:] in ['ikas','dams','ošas']: return False
        if word[-5:] in ['ušiem','damas','kremt']: return False
        if (is_good_verb_root_lv(word)):
            return True
    elif key in ['RPC1-P2-I','RPC1-P2-IET']:
        if word[-1:] in ['z','š']: return False
        if word[-2:] in ['ēl','bj','pj','mj','vj','ēm']: return False
        if word[-3:] in ['ilp']: return False
        return is_good_verb_root_present_lv(word)

    elif key in ['RPC2-P23-A']:
        t = get_right_tuple(word)
        if t[1]=='ai' and t[3]=='ē' and tuple_prefix(t)==True: return False
        if t[1]=='a' and t[3]=='ī': return False # 3C
        if t[1]=='ā' and t[3]=='ī': return False # 3C
        if t[1]=='a' and t[3]=='ā' and tuple_prefix(t)==True: return False # 12C
        if t[1]=='a' and t[3]=='ē' and tuple_prefix(t)==True: return False # 1C
        if t[1]=='i' and t[3]=='ā': return False # 3C
        for sw in ("ā","ē","ī","o"):
            if sw==word or len(word)>len(sw) and (sw==word[-len(sw):] 
            and word[-3:-1] not in ["oj","tp"]
            and word[-3:] not in ["jie","vie","cie","īnā","kvā","blū"]
            and word[-4:] not in ["āmie","ātie","amie","atie","usie"]
            and word[-5:] not in ["jamie","jatie"]):
                return True
    elif key in ['RPC2-OJ','RPC2-OJAMIES']:
        if word[-1:]=='j':
            word=word[:-1]
            t = get_right_tuple(word)
            if t[1]=='ai' and t[3]=='ē' and tuple_prefix(t)==True: return False
            if t[1]=='a' and t[3]=='ī': return False # 3C
            if t[1]=='ā' and t[3]=='ī': return False # 3C
            if t[1]=='a' and t[3]=='ā' and tuple_prefix(t)==True: return False # 12C
            if t[1]=='a' and t[3]=='ē' and tuple_prefix(t)==True: return False # 1C
            if t[1]=='i' and t[3]=='ā': return False # 3C
            for sw in ("ā","ē","ī","o"):
                if sw==word or len(word)>len(sw) and (sw==word[-len(sw):] 
                and word[-3:-1] not in ["oj","tp"]
                and word[-3:] not in ["jie","vie","cie","īnā","kvā","blū"]
                and word[-4:] not in ["āmie","ātie","amie","atie","usie"]
                and word[-5:] not in ["jamie","jatie"]):
                    return True

    elif key in ['RPC3-AM','RPC3-AMIES']:
        if word[-2:] in ["ab"]: return False
        return is_good_verb_root_present_lv(word)
    elif key in ['RPC3-ĀM','RPC3-ĀMIES']:
        return is_good_verb_root_present_lv(word)
    elif key in ['RPC3-P12-S','RPC3-P12-IES']:
        if word[-2:] in ["ab"]: return False
        return is_good_verb_root_present_lv(word)
    elif key=='RPC3-P3-0':
        if word[-2:] in ["ot"]: return False
        if word[-2:] in ["aj","šs","lt","bt","gt","kt","pt","mt","rt","ūm","ām","ēt","ks","āt","ts","dz"]: return False
        if word[-3:] in ['tīt','jis','jam','ies','jas','aut','dam','cis','jot','kot']: return False
        if word[-4:] in ['ikas','dams','ošas']: return False
        if word[-5:] in ['ušiem','damas','kremt']: return False
        if (is_good_verb_root_lv(word)):
            return True
    elif key=='RPC3-P3-A':
        if word[-1:] in ['z']: return False
        if word[-2:] in ['ēl','īl','bj','pj','mj','vj','ēm']: return False
        if word[-3:] in ['ilp','auc','ēc','iec']: return False
        return is_good_verb_root_present_lv(word)

# ================================== VERB OTHER ============================
    elif key=='RDAM':
        if is_good_verb_root_lv(word):
            return True
    elif key=='RŠAN': # brauk-šana, strādā-šana
        if is_good_verb_root_lv(word):
            return True
    elif key=='RKUS': # brau-K-uši, li-K-uši
        if is_good_verb_root_lv(word)==False: return False
        if word[-1:] in ['c']: return False
        if word[-2:] in ['dz']: return False
        return is_good_verb_root_lv(word)
    elif key=='RCIS': # brau-C-is, li-C-is
        if is_good_verb_root_lv(word)==False: return False
        if word[-1:] in ['k','g']: return False
        return is_good_verb_root_lv(word)
    elif key in ['ROS','RAM','RĀM','RAMAIS','RĀMAIS']: # brauc-OŠi, liek-OŠi
        if is_good_verb_root_lv(word)==False: return False
        if word[-1:] in ['k','g']: return False
        return is_good_verb_root_lv(word)
    elif key=='RŠANA':
        for sw in ("ie","au","ā","ē","ī","o","ū","a","e","i","u"):
            if sw==word or len(word)>len(sw) and (sw==word[-len(sw):] 
            and word[-3:] not in ["ojo"]
            and word[-4:] not in ["āmie","ātie","amie","atie","usie"]
            and word[-5:] not in ["jamie","jatie"]):
                return True
    elif key=='ROJ':
        for sw in ("āj","ēj","īj","oj","ūj"):
            if len(word)>len(sw) and sw==word[-len(sw):]:
                wordx = word[:-len(sw)]
                if wordx[-1:] not in vowdict_lv:
                    return True
    elif key in ['RFUT','RFUTS']:
        if word[-1:] not in ['p','r','k','l','m','b','g']: return False
        if word[-2:] in ['am','al']: return False
        if word[-3:] in ['jum']: return False
        return is_good_verb_root_lv(word)
    elif key in ['RFUTA','RFUTAS','RDAMA']:
        t = get_right_tuple(word)
        for sw in ("ā","ē","ī","o","ū","ie","au"):
            if sw==word or len(word)>len(sw) and (sw==word[-len(sw):] 
            and word[-3:-1] not in ["oj","tp"]
            and word[-3:] not in ["jie","vie","cie","īnā","kvā","blū"]
            and word[-4:] not in ["āmie","ātie","amie","atie","usie"]
            and word[-5:] not in ["jamie","jatie"]):
                return True
    elif key=='RPAST':
        if len(word)<2: return False
        if word[-5:] in ['krimt']: return True
        if word in ['ain','ak']: return False
        if word[-1:] in vowdict: return False
        if word[-1:] in ['š','ķ','ņ','ļ','ž']: return False
        if word[-2:]=='ej' and word[-3:]!='dej': return False
        if word[-2:] in ['lt','bj','pj','mj','vj','un',"bt","gt","kt","pt","mt","rt","er","or","rd",
               'īg','ūv','ēt','ēj','āj','īj','oj','ūj','ām','um','īp','st','ok','og','ūp']: return False
#        if word[-2:-1]=='a' and word[-1] not in ['k','g','d','k','r','l','b']: return False
        if word[-3:] in ['auk','auj','ien','ērp','iek','ērk','ieg','elk','ait']: return False
        if word[-3:] in ['cij','nij','cin','sij']: return False
        if word[-4:] in ["ājus","ojus","ējus"]: return False
        if word[-5:] in ["āciet"]: return False
        return is_good_part_generic(word)
    elif key=='RPASTOJ':
#        return True
        if word[-1:]=='j':
            ww=word[:-1]
            t = get_right_tuple(ww)
            if word[-3:] in ["jēj","jīj","joj","jūj"]: return False
            if word[-4:] in ["ājāj","ojāj","ējāj","ījāj"]: return False
            if word[-4:] in ["āsāj","āsēj","āsīj","āsoj","āsūj","ācāj"]: return False
            for sw in ("āj","ēj","īj","oj","ūj"):
                if len(word)>len(sw) and sw==word[-len(sw):]:
                    wordx = word[:-len(sw)]
                    if wordx[-1:] not in vowdict_lv:
                        return True
    else: print('No such key defined in root_check',key)
    return False
