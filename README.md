
# GENSEG Segmenter

This repository contains Python 3 text segmentation scripts for machine translation.

## The main principles

  - Performs close-to-morphological segmentation
  - Has two sub-tools:
  -- generic segmenter (for any language)
  -- Latvian-specific segmenter (performs Latvian morphological analysis for better results)
  - to support open-vocabulary (in machine translation), segmented texts should be post-processed (e.g., using [BPE])

## Usage instructions

GENSEG is used in the following way:
  - Learning phase (files of potential segments produced): [learn_genseg.py], [learn_lvseg.py]
  - Segmentation phase (using produced file of the previous phase): [apply_genseg.py], [apply_lvseg.py]
  - Removing segmentation: [unprocess_seg.py]

### Phase #1. Learning ([learn_genseg.py], [learn_lvseg.py])

During this phase, segmentation vocabulary {svoc} produced from the {corpus}. Segmentation vocabulary contains information about words how they should be segmented into three parts (Latvian segmenter): {prefix} root {postfix}, or two parts (generic segmenter): root {postfix}.

**Running the generic learning script**:

```sh
learn_genseg.py -i {corpus} -o {svoc}
```

**Running the Latvian learning script**:

```sh
learn_lvseg.py -i {corpus} -o {svoc}
```

**Additional optional parameters for the learning script**:
  - mode: 0-segmentation vocabulary produced (default), 1-extended segmentation vocabulary produced (just for analysis) - several segmentation variants for each word with validity rates
  - prefignore (generic segmentation only): generic segmenter is bad at splitting prefixes correctly, so this paramter is 1 by default
  - several parameters for the generic learning script: rootextent, minroot, maxroot, rootlencoef, maxprefix, prerate, maxpostfix, postrate, prepenalty (described in [learn_genseg.py]).

Just for a brief insight 1, small excerpt of English segmentation vocabulary (in file {svoc}):
  - abducted abduct ed
  - abductee abduct ee
  - abductees abduct ees
  - abducting abduct ing
  - abduction abduct ion
  - abductions abduct ions
  - abductor abduct or
  - abductors abduct ors
  - abilities abilit ies
  - ability abilit y

Just for a brief insight 2, small excerpt of Latvian segmentation vocabulary (in file {svoc}), '@' indicates prefix:
  - pats pat s
  - patur @pa tur
  - paturot @pa tur ot
  - paturēt @pa tur ēt
  - patvērumu patvērumu
  - patānī patānī
  - patēriņa @pa tēr iņa
  - patēriņu @pa tēr iņu
  - patērētiem @pa tēr ētiem
  - patērētāji @pa tēr ētāji
  - patīk patīk
  - patīkamas patīkam as
  - patīkami patīkam i

Just for a brief insight 3, small excerpt of Russian segmentation vocabulary (in file {svoc}):
  - канцерогенные канцероген ные
  - канцерогенных канцероген ных
  - канцерогенов канцероген ов
  - канцлер канцлер
  - канцлера канцлер а
  - канцлере канцлер е
  - канцлеров канцлер ов
  - канцлером канцлер ом

Just for a brief insight 4, small excerpt of German segmentation vocabulary (in file {svoc}):
  - logistisch logistisch
  - logistische logistisch e
  - logistischen logistisch en
  - logistischer logistisch er
  - logistisches logistisch es
  - lokalisieren lokalisier en
  - lokalisiert lokalisier t
  - lokalisierte lokalisier te
  - lokalisierten lokalisier ten
  - lokalisierter lokalisier ter
  - lokalisiertes lokalisier tes
  - lokalisierung lokalisier ung


### 2. Segmentation ([apply_genseg.py], [apply_lvseg.py])

During this phase, {input text} is segmented using segmentation vocabulary {svoc} produced in the learning phase.

**Running the generic segmentation script**:

```sh
apply_genseg.py -i {input text} -j {svoc} -o {output text}
```

**Running the Latvian segmentation script**:

```sh
apply_lvseg.py -i {input text} -j {svoc} -o {output text}
```

**Additional optional parameters for the segmentation script**:

  - mode - extent of segmentation, 0-segmented according the segmentation vocabulary, 1 (default) - prefixes not segmented or almost not segmented even if they are in the segmentation vocabulary
  - segmentation marker (marker1) -- a character or sequence of character to mark segments to constitute words (if sequence of digits, then is converted to the character represented by that number, default '9474')
  - uppercase marker (marker2) -- a character or sequence of character to mark next word as starting with uppercase (if sequence of digits, then is converted to the character represented by that number, default '9553')

##### Example of segmentation

if segmentation mark is '@', uppercase mark is '$', and word 'accounting' is segmented in dictionary as ac-count-ing, the word 'Accounting' will appear in the final text the following way:
  - $ ac@ count @ing (if mode  = 0)
  - $ account @ing (if mode = 1)


### 3. Removing segmentation ([unprocess_seg.py])

During this operation, a segmented text is converted back to a normal text:

```sh
unprocess_genseg.py -i {input text} -o {output text}
```

**Additional optional parameters for removing segmentation (only if specified in the segmentation phase)**:

  - segmentation marker (marker1)
  - uppercase marker (marker2)


## Publications

Jānis Zuters and Gus Strazds. Subword Segmentation for Machine Translation Based on Grouping Words by Potential Roots.
To appear.

## Acknowledgements

The research has been supported by the European Regional Development Fund within the research project ”Neural Network Modelling for Inflected Natural Languages” No. 1.1.1.1/16/A/215, and the Faculty of Computing, University of Latvia.

   [BPE]: <https://github.com/rsennrich/subword-nmt>
   [learn_genseg.py]: <https://github.com/zuters/genseg/learn_genseg.py>
   [learn_lvseg.py]: <https://github.com/zuters/genseg/learn_lvseg.py>
   [apply_genseg.py]: <https://github.com/zuters/genseg/apply_genseg.py>
   [apply_lvseg.py]: <https://github.com/zuters/genseg/apply_lvseg.py>
   [unprocess_seg.py]: <https://github.com/zuters/genseg/unprocess_seg.py>
