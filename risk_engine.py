import re

def calculate_risk(result, text):

    category_match = re.search(r"Case Category:\s*(.*)", result)
    category = category_match.group(1).strip() if category_match else "Informational"

    score = 0

    if "breach" in text.lower():
        score += 25

    if "arrest" in text.lower():
        score += 30

    if "fraud" in text.lower():
        score += 20

    if "Article" in result:
        score += 20

    return min(score, 100), category