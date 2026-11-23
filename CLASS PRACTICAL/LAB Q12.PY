grammar = {"S": [["NP","VP"]], "NP": [["Det","N"]], "VP": [["V","NP"], ["V"]],
           "Det": [["the"], ["a"]], "N": [["dog"], ["cat"]], "V": [["chased"], ["sleeps"]]}
def earley(words):
    chart = [[] for _ in range(len(words) + 1)]
    def add(i, st):
        if st not in chart[i]: chart[i].append(st)
    add(0, ("GAMMA", ("S",), 0, 0))
    for i in range(len(words) + 1):
        for lhs, rhs, dot, origin in chart[i]:
            if dot < len(rhs):
                nxt = rhs[dot]
                if nxt in grammar:                                   # PREDICT
                    for prod in grammar[nxt]: add(i, (nxt, tuple(prod), 0, i))
                elif i < len(words) and words[i] == nxt:             # SCAN
                    add(i + 1, (lhs, rhs, dot + 1, origin))
            else:                                                    # COMPLETE
                for l2, r2, d2, o2 in list(chart[origin]):
                    if d2 < len(r2) and r2[d2] == lhs: add(i, (l2, r2, d2 + 1, o2))
    return chart
for s in ["the dog chased a cat", "the cat sleeps", "cat the sleeps"]:
    w = s.split(); chart = earley(w)
    ok = ("GAMMA", ("S",), 1, 0) in chart[-1]
    print(f"{s!r}: chart sizes {[len(c) for c in chart]} -> {'ACCEPTED' if ok else 'REJECTED'}")
