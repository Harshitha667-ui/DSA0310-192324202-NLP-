from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
docs = ["Machine learning is a field of artificial intelligence",
        "Deep learning uses neural networks for machine learning tasks",
        "Cricket is a popular sport in India",
        "The Indian cricket team won the match",
        "Natural language processing is a part of artificial intelligence"]
query = "artificial intelligence and machine learning"
vec = TfidfVectorizer(stop_words="english")
X = vec.fit_transform(docs)
scores = cosine_similarity(vec.transform([query]), X).ravel()
print("Query:", query)
for rank, i in enumerate(scores.argsort()[::-1], 1):
    print(f"Rank {rank} | score={scores[i]:.4f} | Doc{i+1}: {docs[i]}")
