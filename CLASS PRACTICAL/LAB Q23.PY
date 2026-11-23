import re
STOP = {"the","a","an","is","are","was","has","for","on","in","at","of","to","my","he","it","and","with"}
def content(s):
    out = set()
    for w in re.findall(r"[a-z]+", s.lower()):
        if w in STOP: continue
        out.add(w[:-1] if w.endswith("s") and len(w) > 4 else w)
    return out
def coherence(text):
    sents = [s.strip() for s in re.split(r"[.!?]", text) if s.strip()]
    sims = []
    for a, b in zip(sents, sents[1:]):
        A, B = content(a), content(b)
        sims.append(len(A & B) / len(A | B))
    return sims, sum(sims) / len(sims)
texts = {"Text 1": "Rahul bought a new laptop yesterday. The laptop has a fast processor. He uses the laptop for programming. Programming on a fast laptop saves time.",
         "Text 2": "The weather is sunny today. Bananas are rich in potassium. My train leaves at noon. Cricket needs a bat."}
for name, t in texts.items():
    sims, avg = coherence(t)
    print(f"{name}: sentence-pair similarity = {[round(x, 2) for x in sims]}, average = {avg:.2f} ->",
          "COHERENT" if avg >= 0.1 else "INCOHERENT")
