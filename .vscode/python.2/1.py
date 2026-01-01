# PII Detection and Masking Script
import re
from datetime import datetime

def mask_email(email):
    name, domain = email.split("@")
    if len(name) <= 2:
        return name[0] + "***@" + domain
    return name[0] + "***" + name[-1] + "@" + domain

def mask_phone(phone):
    return phone[:2] + "******" + phone[-2:]

def mask_aadhaar(aadhaar):
    return "XXXX-XXXX-" + aadhaar[-4:]

def mask_card(card):
    return "XXXX-XXXX-XXXX-" + card[-4:]

def detect_and_mask(text):
    report = []
    detected = set()   # prevents double masking

    emails = re.findall(r"\b[\w\.-]+@[\w\.-]+\.\w+\b", text)
    for e in emails:
        if e not in detected:
            masked = mask_email(e)
            text = text.replace(e, masked)
            report.append(f"Email masked: {masked}")
            detected.add(e)

    phones = re.findall(r"\b\d{10}\b", text)
    for p in phones:
        if p not in detected:
            masked = mask_phone(p)
            text = text.replace(p, masked)
            report.append(f"Phone masked: {masked}")

