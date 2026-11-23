import nltk
from nltk.parse import ViterbiParser
grammar = nltk.PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [1.0]
VP -> V NP [0.5] | V [0.5]
Det -> 'the' [0.5] | 'a' [0.5]
N -> 'dog' [0.5] | 'cat' [0.5]
V -> 'chased' [0.5] | 'saw' [0.5]
""")
parser = ViterbiParser(grammar)
for tree in parser.parse("the dog chased a cat".split()):
    print(tree)
