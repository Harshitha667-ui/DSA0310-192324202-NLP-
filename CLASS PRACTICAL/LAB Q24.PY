import re
rules = [("GREETING", r"^(hi|hello|hey|good (morning|evening))\b"),
         ("GOODBYE", r"\b(bye|goodbye|see you)\b"),
         ("THANKS", r"\b(thanks|thank you)\b"),
         ("REQUEST", r"^(please|can you|could you|would you)\b"),
         ("YES-NO-QUESTION", r"^(is|are|do|does|did|can|will|have|has)\b.*\?$"),
         ("WH-QUESTION", r"^(what|when|where|who|why|how)\b"),
         ("ACCEPT", r"^(yes|yeah|sure|okay|ok)\b"),
         ("REJECT", r"^(no|nope|never)\b")]
def dialog_act(utt):
    for act, pat in rules:
        if re.search(pat, utt.lower().strip()): return act
    return "STATEMENT"
dialog = [("User","Hello!"), ("Bot","Hi! How can I help you?"),
          ("User","Can you book a table for two tonight?"), ("Bot","What time would you prefer?"),
          ("User","Around 8 pm."), ("Bot","Is Italian food okay?"),
          ("User","Yes, that works."), ("User","Thank you!"), ("Bot","Goodbye!")]
for who, u in dialog:
    print(f"{who:4}: {u:<40} -> {dialog_act(u)}")
