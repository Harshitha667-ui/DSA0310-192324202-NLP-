import nltk
for pkg in ['punkt', 'punkt_tab', 'averaged_perceptron_tagger', 'averaged_perceptron_tagger_eng']:
    nltk.download(pkg)

text = "The quick brown fox jumps over the lazy dog"
tokens = nltk.word_tokenize(text)
print(nltk.pos_tag(tokens))
