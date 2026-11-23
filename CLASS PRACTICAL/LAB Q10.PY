lexicon = {"I":"PRP","want":"VBP","to":"TO","and":"CC","they":"PRP","are":"VBP"}
rules = [("NN", "VB",  "previous tag is TO",  lambda i, tg: i > 0 and tg[i-1][1] == "TO"),
         ("NN", "VBG", "word ends with -ing", lambda i, tg: tg[i][0].endswith("ing"))]
words = "I want to run and they are running".split()
tagged = [(w, lexicon.get(w, "NN")) for w in words]
print("Initial :", tagged)
for frm, to, desc, cond in rules:
    for i, (w, t) in enumerate(tagged):
        if t == frm and cond(i, tagged):
            tagged[i] = (w, to)
            print(f"Rule [{frm}->{to} if {desc}] changed '{w}'")
print("Final   :", tagged)
