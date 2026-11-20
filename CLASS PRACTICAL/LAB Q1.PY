import re
text = "Contact: support@example.com, sales@test.org. Call 98765-43210 on 12/05/2024."
print("Emails :", re.findall(r"[\w.]+@[\w.]+\.\w+", text))
print("Phone  :", re.search(r"\d{5}-\d{5}", text).group())
print("Dates  :", re.findall(r"\d{2}/\d{2}/\d{4}", text))
print("Starts with 'Contact':", bool(re.match(r"Contact", text)))
print("Masked :", re.sub(r"\d", "#", text))
print("Words (5+ letters):", re.findall(r"\b[A-Za-z]{5,}\b", text))
