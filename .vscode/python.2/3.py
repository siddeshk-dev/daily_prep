# AI-Like Text Plagiarism Checker
import string

def clean_text(text):
    text = text.lower()
    for ch in string.punctuation:
        text = text.replace(ch, "")
    return text

def get_ngrams(words, n=3):
    return {" ".join(words[i:i+n]) for i in range(len(words) - n + 1)}

def plagiarism_score(text1, text2):
    words1 = clean_text(text1).split()
    words2 = clean_text(text2).split()

    if len(words1) < 3 or len(words2) < 3:
        return 0, set()

    ngrams1 = get_ngrams(words1)
    ngrams2 = get_ngrams(words2)

    common = ngrams1.intersection(ngrams2)
    score = (len(common) / len(ngrams1)) * 100

    return round(score, 2), common

def verdict(score):
    if score >= 60:
        return "HIGH PLAGIARISM"
    elif score >= 30:
        return "MODERATE PLAGIARISM"
    elif score > 0:
        return "LOW PLAGIARISM"
    else:
        return "NO PLAGIARISM"

def main():
    print("AI-Like Text Plagiarism Checker\n")

    print("Enter Original Text (type END to finish):")
    original = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        original.append(line)

    print("\nEnter Suspected Text (type END to finish):")
    suspect = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        suspect.append(line)

    text1 = " ".join(original)
    text2 = " ".join(suspect)

    score, common_phrases = plagiarism_score(text1, text2)

    print("\n--- PLAGIARISM REPORT ---")
    print("Similarity Score:", score, "%")
    print("Verdict:", verdict(score))

    if common_phrases:
        print("\nCommon Phrases Detected:")
        for phrase in list(common_phrases)[:5]:
            print("-", phrase)
    else:
        print("\nNo common phrases found")

main()
