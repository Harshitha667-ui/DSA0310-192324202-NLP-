lex = {"the":"DT","a":"DT","big":"JJ","red":"JJ","old":"JJ","dog":"NN","ball":"NN","garden":"NN",
       "chased":"VB","in":"IN"}
meaning = {"dog": "a domesticated carnivorous mammal", "ball": "a round object used in games",
           "garden": "a piece of land for growing plants"}
def noun_phrases(words):
    nps, cur = [], []
    for w in words + ["<end>"]:
        if lex.get(w) in ("DT", "JJ", "NN"): cur.append(w)
        else:
            if any(lex[x] == "NN" for x in cur): nps.append(cur)
            cur = []
    return nps
sentence = "the big dog chased a red ball in the old garden"
for np_ in noun_phrases(sentence.split()):
    head = [w for w in np_ if lex[w] == "NN"][-1]
    mods = [w for w in np_ if lex[w] == "JJ"]
    print(f"NP: {' '.join(np_):<14} head={head:<7} modifiers={mods}  meaning: {meaning[head]}")
    print(f"    semantic form: {head}(x) " + "".join(f"& {m}(x) " for m in mods))
