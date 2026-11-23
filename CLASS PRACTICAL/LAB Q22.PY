import re
entities = {"Mary": ("f","sg"), "John": ("m","sg"), "library": ("n","sg"), "book": ("n","sg"), "history": ("n","sg")}
pronouns = {"she": ("f","sg"), "he": ("m","sg"), "her": ("f","sg"), "him": ("m","sg"), "it": ("n","sg")}
text = "Mary met John at the library. She gave him a book. It was about history."
mentions = []
for tok in re.findall(r"[A-Za-z]+", text):
    if tok in entities:
        mentions.append((tok, entities[tok]))
    elif tok.lower() in pronouns:
        feat = pronouns[tok.lower()]
        ref = next((m for m, f in reversed(mentions) if f == feat), None)
        print(f"{tok:4} -> {ref}")
