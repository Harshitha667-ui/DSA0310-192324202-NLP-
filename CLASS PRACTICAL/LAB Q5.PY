from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["running", "flies", "happily", "caresses", "ponies", "cats",
         "agreed", "plastered", "motoring", "generalization"]
for w in words:
    print(f"{w:15} -> {ps.stem(w)}")

