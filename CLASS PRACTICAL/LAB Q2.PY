delta = {("q0","a"):"q1", ("q0","b"):"q0",
         ("q1","a"):"q1", ("q1","b"):"q2",
         ("q2","a"):"q1", ("q2","b"):"q0"}
def accepts(s):
    state = "q0"
    for ch in s:
        if (state, ch) not in delta:
            return False
        state = delta[(state, ch)]
    return state == "q2"
for w in ["ab", "aab", "abab", "ba", "abb", "bbab", "aba", ""]:
    print(f"{w!r:8} ->", "Accepted" if accepts(w) else "Rejected")
