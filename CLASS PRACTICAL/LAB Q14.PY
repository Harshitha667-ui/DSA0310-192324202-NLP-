grammar = {"S": [["NP_sg","VP_sg"], ["NP_pl","VP_pl"]],
  "NP_sg": [["Det","N_sg"]], "NP_pl": [["Det","N_pl"]],
  "VP_sg": [["V_sg"], ["V_sg","NP_sg"], ["V_sg","NP_pl"]],
  "VP_pl": [["V_pl"], ["V_pl","NP_sg"], ["V_pl","NP_pl"]],
  "Det": [["the"]], "N_sg": [["dog"], ["cat"]], "N_pl": [["dogs"], ["cats"]],
  "V_sg": [["barks"], ["chases"]], "V_pl": [["bark"], ["chase"]]}
def derive(sym, words, i):
    if sym not in grammar:
        return [i + 1] if i < len(words) and words[i] == sym else []
    ends = []
    for prod in grammar[sym]:
        pos = [i]
        for s in prod:
            pos = [e for p in pos for e in derive(s, words, p)]
        ends += pos
    return ends
def agrees(sentence):
    w = sentence.lower().split()
    return len(w) in derive("S", w, 0)
for s in ["the dog barks", "the dogs bark", "the dog bark", "the dogs barks",
          "the cat chases the dogs", "the cats chases the dog"]:
    print(f"{s!r:30} -> {'Agreement OK' if agrees(s) else 'Agreement ERROR'}")
