# 🛡️ OWASP Top 10

Welcome to the **OWASP Top 10** directory! This folder contains scripts and documentation for identifying and exploiting the most critical web application security risks as defined by the Open Web Application Security Project (OWASP).

## 📌 Overview

The OWASP Top 10 is a standard awareness document for developers and web application security professionals. This project involves hands-on labs focusing on broken access control, cryptographic failures, and injection vulnerabilities.

## 🗂️ Investigation & Exploitation

| File Name | OWASP Category | Description |
| :--- | :--- | :--- |
| **`1-xor_decoder.sh`** | **A02: Cryptographic Failures** | A Bash script designed to decode XOR-encoded WebSphere passwords, demonstrating why weak encoding is not a substitute for encryption. |
| **`4-vuln.txt`** | **A03: Injection / A01: Broken Access Control** | Documentation of a vulnerability found in the "Bio" field of user profiles, typically indicating a Stored XSS or Injection point. |

### 🚩 Capture The Flag (CTF)
* **`2-flag.txt` (Cryptographic Failures):** Flag obtained by identifying and bypassing weak cryptographic implementations.
* **`3-flag.txt` (Broken Access Control):** Flag captured by successfully performing horizontal or vertical privilege escalation to identify restricted user profiles.

## 🛠️ Security Concepts Applied

* **Insecure Deserialization/Encoding:** Using the `1-xor_decoder.sh` to prove that obfuscation is not security.
* **Cryptographic Failures:** Identifying the use of hardcoded keys or weak algorithms that allow sensitive data to be recovered.
* **Broken Access Control:** Testing the application's ability to keep users within their own data boundaries (IDOR - Insecure Direct Object Reference).
* **Injection Points:** Identifying unsanitized input fields (like a user's Bio) that allow malicious payloads to be stored or executed.

## 📝 Learning Objectives

* Understand the impact of the Top 10 most critical web security risks.
* Learn how to identify "low-hanging fruit" like XOR-encoded strings and unvalidated profile fields.
* Develop a methodology for systematically testing a web application against the OWASP framework.

---

⚠️ **Disclaimer** All projects in this repository are created for educational purposes as part of the Holberton School curriculum. These techniques are strictly for authorized security testing.
