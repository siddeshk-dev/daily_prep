# AI-Like Intrusion Detection System
from datetime import datetime

FAILED_LIMIT = 3
ODD_HOURS = range(0, 6)

def analyze_logs(logs):
    report = {}
    alerts = set()   # prevent duplicate alerts

    for entry in logs:
        user, ip, status, time = entry
        hour = int(time.split(":")[0])

        if user not in report:
            report[user] = {
                "failed": 0,
                "ips": set(),
                "risk": 0,
                "times": []
            }

        report[user]["times"].append(time)
        report[user]["ips"].add(ip)

        if status == "FAILED":
            report[user]["failed"] += 1
            report[user]["risk"] += 2

            if report[user]["failed"] == FAILED_LIMIT:
                report[user]["risk"] += 3
                alerts.add(f"Brute force attack suspected for user '{user}'")

        if hour in ODD_HOURS:
            report[user]["risk"] += 1
            alerts.add(f"Odd-hour login activity for user '{user}'")

        if len(report[user]["ips"]) == 3:
            report[user]["risk"] += 2
            alerts.add(f"Multiple IP access detected for user '{user}'")

    return report, alerts

def final_decision(risk):
    if risk >= 7:
        return "HIGH RISK"
    elif risk >= 4:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"

def main():
    print("AI-Like Intrusion Detection System")
    print("Scan Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "\n")

    logs = [
        ("admin", "192.168.1.2", "FAILED", "01:20"),
        ("admin", "192.168.1.2", "FAILED", "01:21"),
        ("admin", "192.168.1.3", "FAILED", "01:22"),
        ("admin", "192.168.1.4", "SUCCESS", "01:23"),
        ("user1", "10.0.0.5", "SUCCESS", "14:30")
    ]

    report, alerts = analyze_logs(logs)

    print("--- USER RISK REPORT ---")
    for user, data in report.items():
        level = final_decision(data["risk"])
        print(f"\nUser: {user}")
        print("Failed Attempts:", data["failed"])
        print("Login Times:", data["times"])
        print("IP Addresses:", list(data["ips"]))
        print("Risk Score:", data["risk"])
        print("Risk Level:", level)

    print("\n--- SECURITY ALERTS ---")
    if alerts:
        for alert in alerts:
            print("-", alert)
    else:
        print("No alerts detected")

main()

