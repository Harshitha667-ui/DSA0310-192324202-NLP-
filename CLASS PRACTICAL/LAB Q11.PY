grammar = {"S": [["NP","VP"]], "NP": [["Det","N"]], "VP": [["V","NP"], ["V"]],
           "Det": [["the"], ["a"]], "N": [["dog"], ["cat"]], "V": [["chased"], ["sleeps"]]}
def parse(sym, words, pos):
    if sym not in grammar:                       # terminal symbol
        if pos < len(words) and words[pos] == sym:
            yield sym, pos + 1
        return
    for prod in grammar[sym]:                    # try each production top-down
        def rec(i, p, kids):
            if i == len(prod):
                yield (sym, kids), p; return
            for t, np_ in parse(prod[i], words, p):
                yield from rec(i + 1, np_, kids + [t])
        yield from rec(0, pos, [])
def show(t):
    return t if isinstance(t, str) else "(" + t[0] + " " + " ".join(show(k) for k in t[1]) + ")"
for s in ["the dog chased a cat", "the cat sleeps", "dog the chased"]:
    w = s.split()
    res = [t for t, p in parse("S", w, 0) if p == len(w)]
    print(f"{s!r}:", show(res[0]) if res else "No parse (rejected)")
