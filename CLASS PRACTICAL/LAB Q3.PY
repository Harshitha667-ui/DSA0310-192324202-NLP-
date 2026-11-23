import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')

words = ['running', 'flies', 'happily', 'better', 'cats', 'studies']
stemmer, lemmatizer = PorterStemmer(), WordNetLemmatizer()
print(f"{'Word':<10}{'Stem':<10}{'Lemma(noun)':<14}{'Lemma(verb)':<12}")
for w in words:
    print(f"{w:<10}{stemmer.stem(w):<10}{lemmatizer.lemmatize(w):<14}{lemmatizer.lemmatize(w, pos='v'):<12}")
