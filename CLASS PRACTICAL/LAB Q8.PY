from collections import defaultdict, Counter
train = [[("the","DT"),("dog","NN"),("barks","VBZ")],
         [("the","DT"),("cat","NN"),("sleeps","VBZ")],
         [("a","DT"),("dog","NN"),("chased","VBD"),("the","DT"),("cat","NN")],
         [("the","DT"),("cat","NN"),("chased","VBD"),("a","DT"),("dog","NN")]]
emit, trans, tagcount = defaultdict(Counter), defaultdict(Counter), Counter()
for sent in train:
    prev = "<s>"
    for w, t in sent:
        emit[t][w] += 1; trans[prev][t] += 1; tagcount[t] += 1; prev = t
tags = list(tagcount)
def p_trans(a, b): return (trans[a][b] + 0.01) / (sum(trans[a].values()) + 0.01 * len(tags))
def p_emit(t, w):  return (emit[t][w] + 0.01) / (tagcount[t] + 0.5)
def viterbi(words):
    V = [{t: (p_trans("<s>", t) * p_emit(t, words[0]), None) for t in tags}]
    for w in words[1:]:
        row = {}
        for t in tags:
            best = max(tags, key=lambda s: V[-1][s][0] * p_trans(s, t))
            row[t] = (V[-1][best][0] * p_trans(best, t) * p_emit(t, w), best)
        V.append(row)
    t = max(tags, key=lambda s: V[-1][s][0]); path = [t]
    for row in reversed(V[1:]):
        t = row[t][1]; path.append(t)
    return list(zip(words, reversed(path)))
for s in ["the dog chased a cat", "a cat sleeps", "the dog barks"]:
    print(viterbi(s.split()))
