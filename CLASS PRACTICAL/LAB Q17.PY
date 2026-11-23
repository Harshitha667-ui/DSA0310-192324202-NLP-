import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
for s in wn.synsets('bank')[:3]:
    print(s.name(), '-', s.definition())
dog = wn.synset('dog.n.01')
print('Lemmas:', dog.lemma_names())
print('Hypernyms:', dog.hypernyms())
print('Similarity dog/cat:', dog.path_similarity(wn.synset('cat.n.01')))
