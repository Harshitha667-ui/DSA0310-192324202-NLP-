def pluralize(noun):
    state = "q0"
    for ch in noun[::-1][:2]:          # FSM reads the word from the end
        if state == "q0":
            state = "SIB" if ch in "sxz" else "H" if ch == "h" else "Y" if ch == "y" else "DEFAULT"
        elif state == "H":
            state = "SIB" if ch in "cs" else "DEFAULT"
        elif state == "Y":
            state = "DEFAULT" if ch in "aeiou" else "IES"
        if state in ("SIB", "DEFAULT", "IES"):
            break
    if state == "H": state = "DEFAULT"
    if state == "Y": state = "DEFAULT"
    return {"SIB": noun + "es", "IES": noun[:-1] + "ies", "DEFAULT": noun + "s"}[state]
for n in ["cat", "bus", "box", "church", "dish", "baby", "boy", "city", "dog"]:
    print(f"{n:8} -> {pluralize(n)}")
