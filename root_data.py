    #!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Janis Zuters

# ================================== C1A =====================================
# inf, p1, p2, p3, past, fut, dams, šana, is(pircis), oš (kliedzošs), usi(pirkusi), um(lūgums), lūdz(īgs)
shpres1ca = {}
shpres1ca['ū']=[("ū","ūst","ūst","ūst","uv","ū","ū","ū","uv","ūst","uv","uv","ūst")] # pūt
shpres1ca['bū']=[("bū","esm","es","ir","bij","bū","bū","bū","bij","es","bij","bij","bij")] # būt

shpres1ca['__RTYPES__'] = [["RINF-C1","RPASSPAST-C1"],
         ["RPC1-P1","RPC1-P1-AMIES"], # pūstu, pūstam, pūstat
         ["RPC1-P2-I","RPC1-P2-IET"], # pūsti
         ["RPC1-P3-0"], # viņš pūst, ir
         ["RPAST"],["RFUTA","RFUTAS"], # past, future
         ["RDAMA"],["RŠANA"], # dams, šana
         ["RCIS","ROJ"],["ROS",'RAM','RAMAIS'], # pirc(is), pērk(ošs)
         ["RKUS","ROJ"],["RK"],["RC"]] # pirk(usi), pirk(ums), pirc(īgs)

		 
shpres1ca20 = {}
shpres1ca20['ī']=[("ī","in","in","in","in","ī","ī","ī","in","in","in","in","in"), # pīt
         ("ī","en","en","en","in","ī","ī","ī","in","en","in","in","en"), # dzīt
         ("ī","ij","ij","ij","ij","ī","ī","ī","ij","ij","ij","ij","ij")] # vīt
shpres1ca20['ie']=[("ie","ien","ien","ien","ēj","ie","ie","ie","ēj","ej","ēj","ēj","ien"), # siet
         ("ie","ej","ej","ej","ej","ie","ie","ie","ej","ej","ej","ej","ej"), # diet
         ("ie","ej","ej","iet","gāj","ie","ie","ie","gāj","ej","gāj","gāj","ej"), # iet
         ("ie","ej","ej","ej","ēj","ie","ie","ie","ēj","ēj","ēj","ēj","ēj")] # liet
shpres1ca20['au']=[("aut","auj","auj","auj","āv","au","au","au","āv","auj","āv","āv","auj")]
shpres1ca20['do']=[("do","dod","dod","dod","dev","do","do","do","dev","dod","dev","dev","dev")] # dot

shpres1ca20['__RTYPES__'] = [["RINF-C1","RPASSPAST-C1"],
         ["RPC1-P1","RPC1-P1-AMIES"], # krāju, krājam, krājat
         ["RPC1-P2-0"], # tu krāj
         ["RPC1-P3-0"], # viņš krāj, krājas
         ["RPAST","RPASTOJ"],["RFUTA","RFUTAS"], # past, future
         ["RDAMA"],["RŠANA"], # dams, šana
         ["RCIS","ROJ"],["ROS",'RAM','RAMAIS'], # pirc(is), pērk(ošs)
         ["RKUS","ROJ"],["RK"],["RC"]] # pirk(usi), pirk(ums), pirc(īgs)

		 
shpres1ca20j = {}
shpres1ca20j['ā']=[("ā","āj","āj","āj","āj","ā","ā","ā","āj","āj","āj","āj","āj")] # krāt
shpres1ca20j['ē']=[("ē","ēj","ēj","ēj","ēj","ē","ē","ē","ēj","ēj","ēj","ēj","ēj")] # spēt, dēt
shpres1ca20j['__RTYPES__'] = [["RINF-C1","RPASSPAST-C1"],
         ["RPC1-P1","RPC1-P1-AMIES"], # krāju, krājam, krājat
         ["RPC1-P2-0"], # tu krāj
         ["RPC1-P3-0"], # viņš krāj, krājas
         ["RPASTOJ"],["RFUTA","RFUTAS"], # past, future
         ["RDAMA"],["RŠANA"], # dams, šana
         ["ROJ"],["ROJ"], # pirc(is), pērk(ošs)
         ["ROJ"],["RK"],["RC"]] # pirk(usi), pirk(ums), pirc(īgs)

# ================================== C1B =====================================
shpres1cb = {}
shpres1cb['aig']=[("aig","aigst","aigst","aigst","aig","aig","aig","aig","aidz","aigst","aig","aig","aidz")] # maigt
shpres1cb['ais']=[("ais","aist","aist","aist","ais","aisī","ais","ai","ais","aist","ais","ais","ais")] # gaist
shpres1cb['als']=[("als","alst","alst","alst","alt","altī","alz","al","alt","alst","alt","alt","alt")] # kalst
shpres1cb['ilp']=[("ilp","ilpst","ilspt","ilspt","ilp","ilp","ilp","ilp","ilp","ilpst","ilp","ilp","ilp")] # tilpt
shpres1cb['irk']=[("irk","irkst","irkst","irkst","irk","irk","irk","irk","irc","irkst","irk","irk","irk")] # mirkt

shpres1cb['ab']=[("ab","abst","abst","abst","ab","ab","ab","ab","ab","abst","ab","ab","ab")] # atlabt
shpres1cb['as']=[("as","ot","ot","ot","at","atī","az","a","at","ot","at","at","at")] # prast
shpres1cb['il']=[("il","ilst","ilst","ilst","il","il","il","il","il","ilst","il","il","il")] # silt
shpres1cb['im']=[("im","imst","imst","imst","im","im","im","im","im","imst","im","im","im")] # rimt
shpres1cb['ir']=[("ir","irst","irst","irst","ir","ir","ir","ir","ir","irst","ir","ir","ir")] # irt
shpres1cb['is']=[("is","iest","iest","iest","is","isī","is","i","is","iest","is","is","is"), # dzist
         ("is","īt","īt","īt","it","itī","iz","i","it","īt","it","it","it")] # mist
shpres1cb['īk']=[("īk","īkst","īkst","īkst","īk","īk","īk","īk","īc","īkst","īk","īk","īc")] # līkt
shpres1cb['īs']=[("īs","īst","īst","īst","īd","īdī","īz","ī","īd","īst","īd","īd","īd"),  # nīst
         ("īs","īst","īst","īst","īt","ītī","īz","ī","īt","īst","īt","īt","īt")] # vīst
shpres1cb['us']=[("us","ūst","ūst","ūst","us","usī","us","u","us","ūst","us","us","us"), # kust
         ("us","ūd","ūd","ūd","ud","udī","uz","u","ud","ūd","ud","ud","ud"), # zust
         ("us","ūt","ūt","ūt","ut","utī","uz","u","ut","ūt","ut","ut","ut")] # just
shpres1cb['ūg']=[("ūg","ūgst","ūgst","ūgst","ūg","ūg","ūg","ūg","ūdz","ūgst","ūg","ūg","ūdz")] # rūgt
shpres1cb['ūs']=[("ūs","ūst","ūst","ūst","us","usī","us","u","us","ūst","us","us","us")] # kūst
shpres1cb['ūz']=[("ūz","ūst","ūst","ūst","ūz","ūzī","ūz","ū","ūz","ūst","ūz","ūz","ūz")] # lūzt

shpres1cb['__RTYPES__'] = [["RINF-C1-C","RPASSPAST-C1-C"],
         ["RPC1-P1","RPC1-P1-AMIES"], # protu
         ["RPC1-P2-I","RPC1-P2-IET"], # proti
         ["RPC1-P3-0"], # prot
         ["RPAST"],["RFUT","RFUTS"], # past, future
         ["RDAM"],["RŠAN"], # dams, šana
         ["RCIS"],["ROS",'RAM','RAMAIS'], # pirc(is), pērk(ošs)
         ["RKUS"],["RK"],["RC"]] # pirk(usi), pirk(ums), pirc(īgs)

shpres1cb20 = {}
shpres1cb20['ais']=[("ais","aiž","aid","aiž","aid","aidī","aiz","ai","aid","aiž","aid","aid","aid")] # laist
shpres1cb20['aug']=[("aug","aug","audz","aug","aug","aug","aug","aug","audz","aug","aug","aud","aud")] # augt
shpres1cb20['auk']=[("auk","auc","auc","auc","auc","auk","auk","auk","auc","auc","auk","auk","auk")] # saukt
shpres1cb20['aus']=[("aus","aust","aust","aust","aus","ausī","aus","au","aus","aust","aus","aus","aus"), # aust (ausma)
         ("aus","auž","aud","auž","aud","audī","auz","au","aud","auž","aud","aud","aud")] # aust (audums)
shpres1cb20['eig']=[("eig","eidz","eidz","eidz","eidz","eig","eig","eig","eidz","eidz","eig","eig","eidz")] # steigt
shpres1cb20['eik']=[("eik","eic","eic","eic","eic","eik","eik","eik","eic","eic","eik","eik","eic")] # teikt
shpres1cb20['ieg']=[("ieg","iedz","iedz","iedz","iedz","ieg","ieg","ieg","iedz","iedz","ieg","ieg","iedz")] # sniegt
shpres1cb20['ies']=[("ies","iež","ied","iež","ied","iedī","iez","ie","ied","iež","ied","ied","ied"), # ziest
         ("ies","ieš","iet","ieš","iet","ietī","ies","ie","iet","ieš","iet","iet","iet")] # ciest
shpres1cb20['iez']=[("iez","iež","iez","iež","iez","iezī","iez","ie","iez","iez","iez","iez","iez")] # bliezt
shpres1cb20['ilk']=[("ilk","elk","elc","elk","ilk","ilk","ilk","ilk","ilc","elk","ilk","ilk","ilc")] # vilkt
#shpres1cb20['ilp']=[("ilp","ilpj","ilp","ilpj","ilp","ilp","ilp","ilp","ilp","ilpj","ilp","ilp","ilp")] # svilpt
shpres1cb20['ims']=[("imst","emt","emt","emt","imt","im","ims","im","imt","emt","imt","imt","imt")] # krimst
shpres1cb20['irk']=[("irk","ērk","ērc","ērk","irk","irk","irk","irk","irc","ērk","irk","irk","irc")] # pirkt
shpres1cb20['irp']=[("irp","ērp","ērp","ērp","irp","irp","irp","irp","irp","ērp","irp","irp","irp")] # cirpt
shpres1cb20['ag']=[("ag","og","odz","og","ag","ag","ag","ag","adz","og","ag","ag","adz")] # zagt
shpres1cb20['ak']=[("ak","ok","oc","ok","ak","ak","ak","ak","ac","ok","ak","ak","ac")] # rakt
shpres1cb20['as']=[("as","od","od","od","ad","adī","az","a","ad","ad","ad","ad","ad")] # rast
shpres1cb20['āb']=[("āb","ābj","āb","ābj","āb","āb","āb","āb","āb","ābj","āb","āb","āb")] # grābt
shpres1cb20['āp']=[("āp","āpj","āp","āpj","āp","āp","āp","āp","āp","āpj","āp","āp","āp")] # kāpt
shpres1cb20['eb']=[("eb","ebj","eb","ebj","eb","eb","eb","eb","eb","ebj","eb","eb","eb")] # grebt
shpres1cb20['ēb']=[("ēb","ēbj","ēb","ēbj","ēb","ēb","ēb","ēb","ēb","ēbj","ēb","ēb","ēb")] # strēbt
#shpres1cb20['al']=[("al","aļ","al","aļ","ēl","al","al","al","ēl","aļ","ēl","al","al")] # kalt
shpres1cb20['el']=[("el","eļ","el","eļ","ēl","el","el","el","ēl","eļ","ēl","el","el")] # celt
shpres1cb20['em']=[("em","em","em","em","ēm","em","em","em","ēm","em","ēm","ēm","ēm"), # ņemt
         ("em","emj","em","emj","ēm","em","em","em","ēm","emj","ēm","ēm","ēm")] # vemt
shpres1cb20['es']=[("es","es","es","es","es","esī","ez","e","es","es","es","es","es")] # nest
shpres1cb20['ēg']=[("ēg","ēg","ēdz","ēg","ēg","ēg","ēg","ēg","ēdz","ēg","ēg","ēg","ēdz")] # bēgt, slēgt, jēgt
shpres1cb20['ēk']=[("ēk","ēc","ēc","ēc","ēc","ēk","ēk","ēk","ēc","ēc","ēk","ēk","ēc")] # lēkt
shpres1cb20['ēr']=[("ēr","eru","er","er","ēr","ēr","ēr","ēr","ēr","er","ēr","ēr","ēr")] # bērt
shpres1cb20['ēs']=[("ēs","ēš","ēs","ēš","ēs","ēsī","ēz","ē","ēs","ēš","ēs","ēs","ēs"), # tēst
         ("ēs","ēd","ēd","ēd","ēd","ēdī","ēz","ē","ēd","ēd","ēd","ēd","ēd")] # ēst
shpres1cb20['ēz']=[("ēz","ēž","ēz","ēž","ēz","ēzī","ēz","ē","ēz","ēž","ēz","ēz","ēz")] # mēzt
shpres1cb20['ig']=[("ig","ieg","iedz","iedz","iedz","ieg","ieg","ieg","iedz","iedz","ig","ig","idz"), # migt
         ("ig","ieg","idz","ieg","ig","ig","ig","ig","idz","ieg","ig","ig","idz")] # snigt
shpres1cb20['ik']=[("ik","iek","iec","iek","ik","ik","ik","ik","ic","iek","ik","ik","ic")] # likt
shpres1cb20['il']=[("il","iļ","il","iļ","īl","il","il","il","īl","iļ","īl","īl","īl")] # vilt
shpres1cb20['ip']=[("ip","īp","īp","īp","ip","ip","ip","ip","ip","īp","ip","ip","ip")] # lipt
shpres1cb20['ir']=[("ir","ir","ir","ir","īr","ir","ir","ir","īr","ir","īr","īr","ir")] # šķirt
shpres1cb20['is']=[("is","it","it","it","it","itī","iz","i","it","it","it","it","it"), # sist
         ("is","iš","is","iš","is","isī","is","i","is","is","is","is","is"),
         ("is","īt","īt","īt","it","itī","iz","i","it","it","it","it","it")] # knist
shpres1cb20['īs']=[("īs","ien","ien","ien","īd","īdī","īz","ī","īd","ien","īd","īd","īd")] # līst (lien)
shpres1cb20['os']=[("os","ož","od","ož","od","odī","oz","o","od","ož","od","od","od"), # kost
         ("os","oš","os","oš","os","osī","oz","o","os","os","os","os","os")] #post
shpres1cb20['rb']=[("rb","rbj","rb","rbj","rb","rb","rb","rb","rb","rbj","rb","rb","rb")]
shpres1cb20['um']=[("um","umj","um","umj","ūm","um","um","um","ūm","umj","ūm","ūm","ūm")]
shpres1cb20['up']=[("up","ūp","ūp","ūp","up","up","up","up","up","ūp","up","up","up")]
shpres1cb20['ūg']=[("ūg","ūdz","ūdz","ūdz","ūdz","ūg","ūg","ūg","ūdz","ūdz","ūg","ūg","ūdz")] # lūgt
shpres1cb20['ūk']=[("ūk","ūc","ūc","ūc","ūc","ūk","ūk","ūk","ūc","ūc","ūk","ūk","ūc")] # rūkt
shpres1cb20['ūs']=[("ūs","ūš","ūt","ūš","ūt","ūtī","ūz","ū","ūt","ūš","ūt","ūt","ūt"), # pūst (pūtiens)
         ("ūs","ūž","ūd","ūž","ūd","ūdī","ūz","ū","ūd","ūž","ūd","ūd","ūd")] # grūst

shpres1cb20['p']=[("p","bj","p","bj","p","p","p","p","p","bj","p","p","p")] # kampt
shpres1cb20['m']=[("m","mj","m","mj","m","m","m","m","m","mj","m","m","m")]
shpres1cb20['l']=[("l","ļ","l","ļ","l","l","l","l","l","ļ","l","l","l"),
           ("l","lst","lst","lst","l","l","l","l","l","lst","l","l","l")]

shpres1cb20['__RTYPES__'] = [["RINF-C1-C","RPASSPAST-C1-C"],
         ["RPC1-P1","RPC1-P1-AMIES"], # augu
         ["RPC1-P2-0"], # audz
         ["RPC1-P3-0"], # aug
         ["RPAST"],["RFUTA","RFUTAS"], # past, future
         ["RDAM"],["RŠAN"], # dams, šana
         ["RCIS"],["ROS",'RAM','RAMAIS'], # pirc(is), pērk(ošs)
         ["RKUS"],["RK"],["RC"]] # pirk(usi), pirk(ums), pirc(īgs)
         
# ================================== C2 ======================================
shpres2c = {}
shpres2c['ā']=[("ā","āj","ā","ā","āj","ā","ā","ā","āj","","āj","","")] # strādāt
shpres2c['ē']=[("ē","ēj","ē","ē","ēj","ē","ē","ē","ēj","","ēj","","")] # tērēt
shpres2c['ī']=[("ī","īj","ī","ī","īj","ī","ī","ī","īj","","īj","","")] # medīt
shpres2c['o']=[("o","oj","o","o","oj","o","o","o","oj","","oj","","")] # slēpot

shpres2c['cā']=[("cā","cāj","cā","cā","cāj","cā","cā","cā","cāj","c","cāj","c","c")] # dancāt
shpres2c['gā']=[("gā","gāj","gā","gā","gāj","gā","gā","gā","gāj","g","gāj","g","dz")] # klaigāt
shpres2c['kā']=[("kā","kāj","kā","kā","kāj","kā","kā","kā","kāj","k","kāj","k","c")] # valkāt
shpres2c['co']=[("co","coj","co","co","coj","co","co","co","coj","c","coj","c","c")] # dancot
shpres2c['go']=[("go","goj","go","go","goj","go","go","go","goj","g","goj","g","dz")] # zirgoties
shpres2c['ko']=[("ko","koj","ko","ko","koj","ko","ko","ko","koj","k","koj","k","c")] # malkot

shpres2c['__RTYPES__'] = [["RINF-C2","RPASSPAST-C2"], # infinite
         ["RPC2-OJ"], # pres1: eju, ejam, ejat, ejos, ejamies, ejaties, ejies
         ["RPC2-P23-A","RPC2-OJ","RPC2-OJAMIES"], # pres2: tu strādā strādājies
         ["RPC2-P23-A","RPC2-OJ","RPC2-OJAMIES"], # pres3: viņš strādā strādājas
         ["RPASTOJ"],["RFUTA","RFUTAS"], # past, future
         ["RDAMA"],["RŠANA"], # dams, šana
         ["ROJ"],["ROJ"], # pirc(is), pērk(ošs)
         ["ROJ"],["RK"],["RC"]] # pirk(usi), pirk(ums), pirc(īgs)

# ================================== C3 ======================================
shpres3c = {}
shpres3c['inā']=[("inā","in","in","in","ināj","inā","inā","inā","ināj","in","ināj","in","in")] # valdzināt
shpres3c['ī']=[("ī","","","","īj","ī","ī","ī","īj","","īj","","")] # mācīt

#shpres3c['ocī']=[("ocī","ok","ok","ok","ocīj","ocī","ocī","ocī","ocīj","ok","cīj","ok","oc")] # locīt
shpres3c['cī']=[("cī","k","k","k","cīj","cī","cī","cī","cīj","k","cīj","k","c")] # locīt, slacīt, braucīt

shpres3c['__RTYPES__'] = [["RINF-C3","RPASSPAST-C3"],
         ["RPC3-ĀM","RPC3-ĀMIES","RPC3-P12-S","RPC3-P12-IES"], # darīt zināt
         ["RPC3-ĀM","RPC3-ĀMIES","RPC3-P12-S","RPC3-P12-IES"], # dari zini
         ["RPC3-P3-A"], # dara, zina, zin
         ["RPASTOJ"],["RFUTA","RFUTAS"], # past, future
         ["RDAMA"],["RŠANA"], # dams, šana
         ["ROJ"],["ROS",'RĀM','RĀMAIS'], # pirc(is), pērk(ošs)
         ["ROJ"],["RK"],["RC"]] # pirk(usi), pirk(ums), pirc(īgs)

shpres3cz = {}
shpres3cz['zinā']=[("zinā","zin","zin","zin","zināj","zinā","zinā","zinā","zināj","zin","zināj","zin","zin")] # zināt

shpres3cz['__RTYPES__'] = [["RINF-C3","RPASSPAST-C3"],
         ["RPC3-ĀM","RPC3-ĀMIES","RPC3-P12-S","RPC3-P12-IES"], # darīt zināt
         ["RPC3-ĀM","RPC3-ĀMIES","RPC3-P12-S","RPC3-P12-IES"], # dari zini
         ["RPC3-P3-A","RPC3-P3-0"], # dara, zina, zin
         ["RPASTOJ"],["RFUTA","RFUTAS"], # past, future
         ["RDAMA"],["RŠANA"], # dams, šana
         ["ROJ"],["ROS",'RĀM','RĀMAIS'], # pirc(is), pērk(ošs)
         ["ROJ"],["RK"],["RC"]] # pirk(usi), pirk(ums), pirc(īgs)

shpres3c0 = {}
shpres3c0['ā']=[("ā","","","","āj","ā","ā","ā","āj","","āj","","")] # dziedāt
shpres3c0['ē']=[("ē","","","","ēj","ē","ē","ē","ēj","","ēj","","")] # gulēt

shpres3c0['lē']=[("lē","l","l","l","lēj","lē","lē","lē","lēj","l","lēj","l","l")] # pilēt, mīlēt

shpres3c0['ecē']=[("ecē","ek","ec","ek","ecēj","ecē","ecē","ecē","ecēj","ek","ecēj","ek","ec")] # tecēt
shpres3c0['ācē']=[("ācē","āk","āk","āk","ācēj","ācē","ācē","ācē","ācēj","āk","cēj","āk","āc")] # mācēt
shpres3c0['ulē']=[("ulē","uļ","ul","uļ","ulēj","ulē","ulē","ulē","ulēj","uļ","ulēj","uļ","ul")] # gulēt

shpres3c0['__RTYPES__'] = [["RINF-C3","RPASSPAST-C3"],
         ["RPC3-AM","RPC3-AMIES","RPC3-P12-S","RPC3-P12-IES"], # guļam dziedat
         ["RPC3-AM","RPC3-AMIES","RPC3-P12-S","RPC3-P12-IES"], # guli dziedi
         ["RPC3-P3-0"], # dzied, guļ
         ["RPASTOJ"],["RFUTA","RFUTAS"], # past, future
         ["RDAMA"],["RŠANA"], # dams, šana
         ["ROJ"],["ROS",'RAM','RAMAIS'], # pirc(is), pērk(ošs)
         ["ROJ"],["RK"],["RC"]] # pirk(usi), pirk(ums), pirc(īgs)
		 # ["ROS",'RAM','RĀM','RAMAIS','RĀMAIS',"ROJ"]

# =============================== NOUNS ======================================
shnoun1 = {}
# logs, palodze, palodžu
shnoun1['']=[("","","")]

shnoun1['b']=[("b","b","bj")]
shnoun1['c']=[("c","c","č")]
shnoun1['č']=[("č","č","č")]
shnoun1['d']=[("d","d","ž"),("d","d","d")]
shnoun1['g']=[("g","dz","dž")]
shnoun1['k']=[("k","c","č")]
shnoun1['l']=[("l","l","ļ")]
shnoun1['m']=[("m","m","mj")]
shnoun1['n']=[("n","n","ņ")]
shnoun1['p']=[("p","p","pj")]
shnoun1['s']=[("s","s","š")]
shnoun1['t']=[("t","t","š"),("t","t","t")]
shnoun1['v']=[("v","v","vj")]
shnoun1['z']=[("z","z","ž")]

shnoun1['dz']=[("dz","dz","dž")]
shnoun1['dž']=[("dž","dž","dž")]
shnoun1['sn']=[("sn","sn","šņ")]

shnoun1['__RTYPES__'] = [["RK","R10","REN"], # zirgs
         ["RC"], # zirdziņš
         ["RČ"]] # zirdžuks

shnoun2 = {}
for k in shnoun1:
    shnoun2[k] = shnoun1[k]
shnoun2['__RTYPES__'] = [["R2x","R2specx","R20"], # kurmis
         ["RC"], # kurmiņš
         ["R2y"]] # kurmju
		 
shnoun5 = {}
for k in shnoun1:
    shnoun5[k] = shnoun1[k]
shnoun5['__RTYPES__'] = [["R5x"], # vēlme
         ["RC"], # vēlmiņa
         ["R5y"]] # vēlmju
		 
shnoun6 = {}
for k in shnoun1:
    shnoun6[k] = shnoun1[k]
shnoun6['__RTYPES__'] = [["R6x"], # vēlme
         ["RC"], # vēlmiņa
         ["R6y"]] # vēlmju

shnoun7 = {}
# Eriā, guru, Bari
shnoun7['']=[("","-","-")]
shnoun7['__RTYPES__']=[["R7"],["R7"],["R7"]]

# =============================== NUMERALS ===================================
shnum = {}
# četr(padsmit), piec(desmit)
shnum['']=[("",)]
shnum['__RTYPES__']=[["NUM19","NUM29"]]

# ========================== PROCESSING ======================================

def create_schemes(s1,spos):
    s2 = {}
    mlen = 0
    for k in s1:
        if k[:1]!="_":
            slist = s1[k]
            for s in slist:
                k2 = s[spos]
                if len(k2)>mlen: mlen=len(k2)
                if k2 not in s2:
                    s2[k2] = []
                s2[k2].append(s)
    s2['__MAX_LEN__'] = mlen
    if "__RTYPES__" in s1:
        s2['__RTYPES__'] = s1['__RTYPES__']
    return s2

# ========================== proc. verbs ======================================

shift = {}

flexcount = 13

shift['C1AI'] = {} # pūsti, esi
for spos in range(flexcount):
    shift['C1AI'][spos] = create_schemes(shpres1ca,spos)

shift['C1A0'] = {} # pin
for spos in range(flexcount):
    shift['C1A0'][spos] = create_schemes(shpres1ca20,spos)

shift['C1A0J'] = {} # krāj
for spos in range(flexcount):
    shift['C1A0J'][spos] = create_schemes(shpres1ca20j,spos)

shift['C1BI'] = {} # mirksti
for spos in range(flexcount):
    shift['C1BI'][spos] = create_schemes(shpres1cb,spos)
	
shift['C1B0'] = {} # laid, skaud
for spos in range(flexcount):
    shift['C1B0'][spos] = create_schemes(shpres1cb20,spos)
	
shift['C2'] = {}
for spos in range(flexcount):
    shift['C2'][spos] = create_schemes(shpres2c,spos)
	
shift['C3'] = {}
for spos in range(flexcount):
    shift['C3'][spos] = create_schemes(shpres3c,spos)

shift['C3Z'] = {}
for spos in range(flexcount):
    shift['C3Z'][spos] = create_schemes(shpres3cz,spos)

shift['C30'] = {}
for spos in range(flexcount):
    shift['C30'][spos] = create_schemes(shpres3c0,spos)

vrtypes = {}
for k in shift:
    if "__RTYPES__" in shift[k][0]:
        for rpos in shift[k][0]["__RTYPES__"]:
            for rt in rpos:
                vrtypes[rt] = 1
vrtypes0 = {}
for rt in vrtypes:
    if rt[-1:]=="0":
        vrtypes0[rt] = 1

# ========================== proc. nouns ======================================

shiftn = {}

flexcountn = 3

shiftn['N1'] = {}
for spos in range(flexcountn):
    shiftn['N1'][spos] = create_schemes(shnoun1,spos)

shiftn['N2'] = {}
for spos in range(flexcountn):
    shiftn['N2'][spos] = create_schemes(shnoun2,spos)

shiftn['N5'] = {}
for spos in range(flexcountn):
    shiftn['N5'][spos] = create_schemes(shnoun5,spos)

shiftn['N6'] = {}
for spos in range(flexcountn):
    shiftn['N6'][spos] = create_schemes(shnoun6,spos)

shiftn['N7'] = {}
for spos in range(flexcountn):
    shiftn['N7'][spos] = create_schemes(shnoun7,spos)

nrtypes = {}
for k in shiftn:
    if "__RTYPES__" in shiftn[k][0]:
        for rpos in shiftn[k][0]["__RTYPES__"]:
            for rt in rpos:
                nrtypes[rt] = 1
nrtypes0 = {}
for rt in nrtypes:
    if rt[-1:]=="0":
        nrtypes0[rt] = 1

# ========================== proc. nums ======================================

shiftnum = {}

flexcountnum = 1

shiftnum['NUM'] = {}
for spos in range(flexcountnum):
    shiftnum['NUM'][spos] = create_schemes(shnum,spos)

numrtypes = {}
for k in shiftnum:
    if "__RTYPES__" in shiftnum[k][0]:
        for rpos in shiftnum[k][0]["__RTYPES__"]:
            for rt in rpos:
                numrtypes[rt] = 1
numrtypes0 = {}
for rt in numrtypes:
    if rt[-1:]=="0":
        numrtypes0[rt] = 1

# ========================== non-segmentable ======================================

nonseg = {}
nonseg["arī"] = 1
nonseg["mēs"] = 1
nonseg["nekā"] = 1
