import json
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
import csv
import re
import pandas as pd
with open('viettat.json') as file:
    data = json.load(file)
with open('dataset_raw.csv') as fraw:
    raw=pd.read_csv(fraw)
raw.columns=['Label','Content']
sent=raw['Content'].loc[6].upper()
print(sent)
#sent=str(sent).
sent=nltk.word_tokenize(sent)
for i,v in enumerate(sent):
    if v in data.keys():
        new_v=v.replace(v,data[v].upper())
        #new_v=nltk.word_tokenize(new_v)
        sent[i]=new_v
sent=TreebankWordDetokenizer().detokenize(sent)
print(sent)


