# AI-Like Text Analyzer its not taken from any ai sevices its my own project.
import string

positive_words = {
    "good", "great", "excellent", "happy", "love", "awesome",
    "fantastic", "nice", "amazing", "positive", "success"
}

negative_words = {
    "bad", "worst", "sad", "hate", "terrible", "awful",
    "poor", "negative", "fail", "angry", "pain"
}

def clean_text(text):
    text = text.lower()
    for ch in string.punctuation:
        text = text.replace(ch, "")
    return text

def analyze_sentiment(words):
    pos = sum(1 for w in words if w in positive_words)
    neg = sum(1 for w in words if w in negative_words)

    if pos > neg:
        return "Positive", pos, neg
    elif neg > pos:
        return "Negative", pos, neg
    else:
        return "Neutral", pos, neg

def extract_keywords(words):
    freq = {}
    for w in words:
        if len(w) > 4:
            freq[w] = freq.get(w, 0) + 1

    keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return keywords[:5]

def readability_score(words, sentences):
    if sentences == 0:
        return 0
    avg_words = len(words) / sentences

    if avg_words <= 12:
        return "Easy"
    elif avg_words <= 20:
        return "Medium"
    else:
        return "Hard"

def ai_feedback(sentiment, readability):
    if sentiment == "Positive" and readability == "Easy":
        return "Text is friendly and easy to understand."
    elif sentiment == "Negative":
        return "Text expresses strong negative emotions."
    elif readability == "Hard":
        return "Text may be difficult for general readers."
    else:
        return "Text is neutral and informative."

def analyze_text(text):
    sentences = text.count(".") + text.count("!") + text.count("?")
    clean = clean_text(text)
    words = clean.split()

    sentiment, pos, neg = analyze_sentiment(words)
    keywords = extract_keywords(words)
    readability = readability_score(words, sentences)
    feedback = ai_feedback(sentiment, readability)

    print("\n--- AI TEXT ANALYSIS REPORT ---")
    print("Total Words:", len(words))
    print("Total Sentences:", sentences)
    print("Sentiment:", sentiment)
    print("Positive Words:", pos)
    print("Negative Words:", neg)
    print("Readability Level:", readability)

    print("\nTop Keywords:")
    for word, count in keywords:
        print(f"{word} ({count})")

    print("\nAI Feedback:")
    print(feedback)

def main():
    print("AI-Like Text Analyzer")
    print("Enter text (type END on new line to finish):\n")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    text = " ".join(lines)
    analyze_text(text)

main()

