import re
patterns = [(r"^(the|a|an)$", "DT"), (r"^(in|on|at|of|with)$", "IN"),
            (r"^(is|are|am)$", "VBZ"), (r"^(was|were)$", "VBD"),
            (r"^-?\d+(\.\d+)?$", "CD"), (r".*ing$", "VBG"), (r".*ed$", "VBD"),
            (r".*ly$", "RB"), (r".*'s$", "NN$"), (r".*s$", "NNS")]
def tag(word):
    for pat, t in patterns:
        if re.match(pat, word.lower()):
            return t
    return "NN"
for s in ["The cats were running quickly in 2024", "A dog walked on the road"]:
    print([(w, tag(w)) for w in s.split()])
