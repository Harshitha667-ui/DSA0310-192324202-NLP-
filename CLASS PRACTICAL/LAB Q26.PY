from transformers import pipeline
translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")
sentences = ["Hello, how are you?",
             "Machine translation is fascinating.",
             "I love learning natural language processing."]
for s in sentences:
    out = translator(s)[0]["translation_text"]
    print(s, "->", out)
