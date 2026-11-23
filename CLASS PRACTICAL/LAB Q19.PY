import re
STOP = {"the","a","an","to","of","in","at","on","and","is","was","with","i","he","it","out","that","by","for","get"}
def tokens(text):
    out = set()
    for w in re.findall(r"[a-z]+", text.lower()):
        if w in STOP: continue
        if len(w) > 4: w = re.sub(r"(ed|ing|s)$", "", w)
        out.add(w)
    return out
senses = {
 "bank": {"financial institution": "an institution that accepts deposits and lends money to customers",
          "river side": "sloping land beside a river or stream"},
 "bat":  {"animal": "a nocturnal flying mammal that hangs upside down in caves",
          "sports equipment": "a wooden club used to hit the ball in cricket or baseball"}}
def lesk(word, sentence):
    ctx = tokens(sentence) - {word}
    best, best_ov = None, (-1, set())
    for sense, gloss in senses[word].items():
        ov = ctx & tokens(gloss)
        if len(ov) > best_ov[0]: best, best_ov = sense, (len(ov), ov)
    return best, best_ov
for w, s in [("bank", "I deposited money at the bank to get a loan"),
             ("bank", "The fisherman sat on the bank of the river"),
             ("bat",  "The bat flew out of the cave at night"),
             ("bat",  "He hit the ball with a bat in the cricket match")]:
    sense, (n, ov) = lesk(w, s)
    print(f"{s!r}\n   '{w}' -> {sense}  (overlap={n}: {sorted(ov)})")

