# GRC & Security Audit Logger with Risk Scoring
# Purpose: Demonstrate automated risk calculation for GRC/SOC roles
# Ratings match the risk matrix used in my GRC investigations:
# https://github.com/atoz-guy/Cybersecurity-Technical-Portfolio/blob/main/GRC-Labs/Analysis-After-It-Happens/risk-matrix.md
import datetime


def ask_score(prompt):
    """Keep asking until the user enters a whole number from 1 to 5."""
    while True:
        answer = input(prompt)
        if answer.isdigit() and 1 <= int(answer) <= 5:
            return int(answer)
        print("Please enter a number from 1 to 5.")


def rate_risk(risk_score):
    """Turn a Likelihood x Impact score into a rating."""
    if risk_score >= 20:
        return "CRITICAL"
    elif risk_score >= 15:
        return "HIGH"
    elif risk_score >= 8:
        return "MEDIUM"
    else:
        return "LOW"


def log_audit_finding():
    print("--- AtoZ Security Risk Assessment Tool ---")

    control_id = input("Enter Security Control ID (e.g., AC-2): ")
    finding = input("Describe the Finding: ")

    # Risk Scoring Logic (1-5 Scale)
    print("\nScale: 1 (Low) to 5 (Critical)")
    likelihood = ask_score("Likelihood of occurrence (1-5): ")
    impact = ask_score("Business impact if exploited (1-5): ")

    # Formula: Risk Score = Likelihood * Impact
    risk_score = likelihood * impact
    rating = rate_risk(risk_score)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open("security_audit_log.txt", "a") as audit_file:
            entry = (f"[{timestamp}] [SCORE: {risk_score}] [RATING: {rating}] "
                     f"[ID: {control_id}] - {finding}\n")
            audit_file.write(entry)
        print(f"\n✅ Audit saved. Calculated Risk Score: {risk_score} ({rating})")
    except Exception as e:
        print(f"❌ System Error: {e}")


if __name__ == "__main__":
    log_audit_finding()
