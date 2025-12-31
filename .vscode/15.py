# AI-Like Fake News Detector
import string

fake_keywords = {
    "shocking", "breaking", "you won't believe", "secret",
    "exposed", "miracle", "guaranteed", "click here",
    "viral", "unbelievable", "truth revealed"
}

trusted_sources = {
    "bbc", "cnn", "reuters", "the hindu", "ndtv",
    "times of india", "associated press"
}

def clean_text(text):
    text = text.lower()
    for ch in string.punctuation:
        text = text.replace(ch, "")
    return text

def keyword_score(text):
    score = 0
    reasons = []

    for word in fake_keywords:
        if word in text:
            score += 2
            reasons.append(f"Fake keyword detected: '{word}'")

    return score, reasons

def source_check(text):
    for source in trusted_sources:
        if source in text:
            return -3, f"Trusted source mentioned: {source}"
    return 0, "No trusted source mentioned"

def style_check(text):
    score = 0
    reasons = []

    if text.count("!") >= 3:
        score += 2
        reasons.append("Too many exclamation marks")

    if text.isupper():
        score += 3
        reasons.append("Text written fully in capital letters")

    return score, reasons

def ai_decision(total_score):
    if total_score >= 5:
        return "FAKE NEWS"
    elif total_score >= 2:
        return "SUSPICIOUS"
    else:
        return "LIKELY REAL"

def analyze_news(news):
    clean = clean_text(news)

    total_score = 0
    explanations = []

    k_score, k_reasons = keyword_score(clean)
    total_score += k_score
    explanations.extend(k_reasons)

    s_score, s_reason = source_check(clean)
    total_score += s_score
    explanations.append(s_reason)

    st_score, st_reasons = style_check(news)
    total_score += st_score
    explanations.extend(st_reasons)

    decision = ai_decision(total_score)

    print("\n--- AI FAKE NEWS ANALYSIS REPORT ---")
    print("Final Score:", total_score)
    print("Verdict:", decision)

    print("\nReasons:")
    if explanations:
        for e in explanations:
            print("-", e)
    else:
        print("- No suspicious patterns found")

def main():
    print("AI-Like Fake News Detector")
    print("Paste news text below (type END to finish):\n")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    news = " ".join(lines)
    analyze_news(news)

main()

