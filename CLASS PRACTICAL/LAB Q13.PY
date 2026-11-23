import nltk
grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP | V
Det -> 'the' | 'a'
N -> 'dog' | 'cat'
V -> 'chased' | 'sleeps'
""")
parser = nltk.ChartParser(grammar)
for tree in parser.parse("the dog chased a cat".split()):
    print(tree)
    print("Leaves:", tree.leaves())
    print("Height:", tree.height())
