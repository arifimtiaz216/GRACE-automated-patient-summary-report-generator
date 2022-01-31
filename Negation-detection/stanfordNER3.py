# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division

# =============================================================================
# from nltk.tokenize import word_tokenize
# from nltk.tag import pos_tag
# from nltk.tag import StanfordNERTagger
# from collections import Counter
# 
# st3=StanfordNERTagger('/home/arif/Desktop/stanfordNER/stanford-ner-2018-02-27/classifiers/english.all.3class.distsim.crf.ser.gz',
#                     '/home/arif/Desktop/stanfordNER/stanford-ner-2018-02-27/stanford-ner.jar',
#                     encoding='utf-8')
# st4=StanfordNERTagger('/home/arif/Desktop/stanfordNER/stanford-ner-2018-02-27/classifiers/english.conll.4class.distsim.crf.ser.gz',
#                     '/home/arif/Desktop/stanfordNER/stanford-ner-2018-02-27/stanford-ner.jar',
#                     encoding='utf-8')
# st7=StanfordNERTagger('/home/arif/Desktop/stanfordNER/stanford-ner-2018-02-27/classifiers/english.muc.7class.distsim.crf.ser.gz',
#                     '/home/arif/Desktop/stanfordNER/stanford-ner-2018-02-27/stanford-ner.jar',
#                     encoding='utf-8')
# #print(st.tag('Rami Eid is studying at Stony Brook University in NYC'.split())[0][1])
# text="That's not bad."
# 
# tokenizedText=word_tokenize(text)
# #print(tokenizedText)
# 
# #classifiedText=st7.tag(tokenizedText)
# #print(classifiedText)
# #print(classifiedText[4][0] +"->"+ classifiedText[4][1])
# 
# posText=pos_tag(tokenizedText)
# print('\n')
# print(posText)
# print('\n')
# counts=Counter(tag for word,tag in posText)
# print(counts)
# #print(counts['NNP'])
# =============================================================================
import os
from nltk.corpus import treebank
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk import chunk
from nltk.parse.stanford import StanfordParser
from nltk.parse.stanford import StanfordDependencyParser


def negDetector(sentence):
    path_to_jar='/home/arif/Desktop/stannfordPARSER/stanford-parser-full-2018-02-27/stanford-parser.jar'
    path_to_models_jar='/home/arif/Desktop/stannfordPARSER/stanford-parser-full-2018-02-27/stanford-parser-3.9.1-models.jar'
    path_to_english_models_ser_gz='/home/arif/Desktop/stannfordPARSER/stanford-parser-full-2018-02-27/stanford-parser-3.9.1-models/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz'
    
    
    os.environ['STANFORD_PARSER']=path_to_jar
    os.environ['STANFORD_MODELS']=path_to_models_jar
    
    parser=StanfordParser(model_path=path_to_english_models_ser_gz)
    dependency_parser=StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)
    
    #sentence="I have not been able to paint in years."
    #print("\n"+sentence+"\n")
    
    treeParsed=list(parser.raw_parse(sentence))
    #print(treeParsed[0])
    #print("\n")
    
    wordTokenized=word_tokenize(sentence)
    posTagged=pos_tag(wordTokenized)
    #print(wordTokenized)
    #print(posTagged)
    
    #tree=chunk.ne_chunk(list(treeParsed)[0])
    tree=chunk.ne_chunk(posTagged)
    #print(tree)
    #tree.draw()
    
    result=dependency_parser.raw_parse(sentence)
    dep=result.next()
    
    #print("\n")
    
# =============================================================================
#     for i in range (len(list(dep.triples()))):
#         print(list(dep.triples())[i])
# =============================================================================
    
    #print(list(dep.triples())[2][1])
    
    return treeParsed[0], list(dep.triples())