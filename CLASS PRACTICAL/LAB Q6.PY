import random
from collections import defaultdict
corpus = ("the cat sat on the mat . the dog sat on the rug . "
          "the cat chased the dog . the dog chased the cat .")
words = corpus.split()
model = defaultdict(list)
for w1, w2 in zip(words, words[1:]):
    model[w1].append(w2)
print("Next words after 'the':", model["the"])
random.seed(42)
def generate(start, n=10):
    out = [start]
    for _ in range(n - 1):
        out.append(random.choice(model[out[-1]]))
    return " ".join(out)
for i in range(3):
    print(f"Generated {i+1}:", generate("the"))
