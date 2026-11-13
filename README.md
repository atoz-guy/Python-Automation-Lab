# Python Automation Lab

Small Python tools I built for GRC and IT support work. They're simple on purpose: each one takes a manual task (logging a finding, scoring a risk, opening a ticket) and makes it consistent and repeatable.

These scripts are used in my real investigations, so you can see them in action in [Cybersecurity-Technical-Portfolio](https://github.com/atoz-guy/Cybersecurity-Technical-Portfolio).

---

## GRC tools

### [grc_audit_logger_w-risk-scoring.py](grc_audit_logger_w-risk-scoring.py)
Logs a finding against a NIST control ID and scores it with **Risk = Likelihood x Impact** (1 to 5 each).

| Score | Rating |
|---|---|
| 20 to 25 | CRITICAL |
| 15 to 19 | HIGH |
| 8 to 14 | MEDIUM |
| 1 to 7 | LOW |

The ratings match my [risk matrix](https://github.com/atoz-guy/Cybersecurity-Technical-Portfolio/blob/main/GRC-Labs/Analysis-After-It-Happens/risk-matrix.md), so the tool, the matrix and the write-ups always agree.

**Used in:** [Lab 002: Phishing and BEC Investigation](https://github.com/atoz-guy/Cybersecurity-Technical-Portfolio/blob/main/GRC-Labs/Analysis-After-It-Happens/Lab-002-Phishing-Investigation.md)

**Sample output:** [audit_results_demo.txt](audit_results_demo.txt)
```
[2026-05-11 14:00:00] [SCORE: 25] [RATING: CRITICAL] [ID: AC-2] - Admin account found without MFA enabled.
[2026-05-11 14:15:00] [SCORE: 6] [RATING: LOW] [ID: PE-3] - Server room door left propped open for 5 minutes.
```

### [grc_audit_logger.py](grc_audit_logger.py)
The first version: logs a finding with a control ID and a simple Low / Medium / High severity.

---

## IT support tools

### [ticket_logger.py](ticket_logger.py)
A basic help desk ticket logger. Takes a customer name and issue and saves it with a timestamp.

---

## Practice

- [Codecademy-Automation-Labs](Codecademy-Automation-Labs): Python exercises from Codecademy (lists, sorting, slicing)

---

## How to run

```bash
python3 grc_audit_logger_w-risk-scoring.py
```

Each script asks for input and appends to a log file in the same folder (`security_audit_log.txt` or `ticket_log.txt`).

**Certs behind this:** Python PCEP, PCAP, PCPP1
