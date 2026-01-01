import re
from datetime import datetime

def mask_email(email):
    name, domain = email.split("@")
    return name[0] + "***@" + domain

def mask_phone(phone):
    return phone[:2] + "******" + phone[-2:]

def mask_aadhaar(aadhaar):
    return "XXXX-XXXX-" + aadhaar[-4:]

def mask_card(card):
    return "XXXX-XXXX-XXXX-" + card[-4:]

def detect_and_mask(text):
    report = []

    emails = re.findall(r"\b[\w\.-]+@[\w\.-]+\.\w+\b", text)
    for e in emails:
        masked = mask_email(e)
        text = text.replace(e, masked)
        report.append(f"Email masked: {masked}")

    phones = re.findall(r"\b\d{10}\b", text)
    for p in phones:
        masked = mask_phone(p)
        text = text.replace(p, masked)
        report.append(f"Phone masked: {masked}")

    aadhaar = re.findall(r"\b\d{12}\b", text)
    for a in aadhaar:
        masked = mask_aadhaar(a)
        text = text.replace(a, masked)
        report.append(f"Aadhaar masked: {masked}")

    cards = re.findall(r"\b\d{16}\b", text)
    for c in cards:
        masked = mask_card(c)
        text = text.replace(c, masked)
        report.append(f"Card masked: {masked}")

    return text, report

def main():
    print("Secure Data Masking Tool")
    print("Enter text containing sensitive data (type END to finish):\n")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    original_text = " ".join(lines)
    masked_text, report = detect_and_mask(original_text)

    print("\n--- SECURITY REPORT ---")
    print("Scan Time:", datetime.now())
    print("\nOriginal Text:")
    print(original_text)

    print("\nMasked Text:")
    print(masked_text)

    print("\nDetected Risks:")
    if report:
        for r in report:
            print("-", r)
    else:
        print("- No sensitive data detected")

main()
