# 🛡️ CyberBank: IDOR & 3D Secure Bypass Assessment

## 📌 Project Overview
This assessment demonstrates a critical chain of **Insecure Direct Object Reference (IDOR)** vulnerabilities and logic flaws within a simulated banking environment. The goal was to bypass 3D Secure and access private customer data.

---

## 🚀 Exploitation Path

### 1. Customer Data Leakage (Flag 0)
* **Initial Discovery:** Identified `/api/customer/transactions` via the Network Tab, which leaked internal customer UUIDs.
* **IDOR Exploit:** Replaced the UUID in `/api/customer/info/[UUID]` to access private profiles of other users.
* **Result:** Successfully extracted **Flag 0** and PII (Personally Identifiable Information).

### 2. Banking Account Compromise (Flag 1)
* **Pivoting:** Used discovered `account_id` values to target the `/api/accounts/info/` endpoint.
* **Exploit:** Broken access control allowed dumping account balances and routing numbers.
* **Result:** Recovered **Flag 1** and identified linked credit card IDs.

### 3. 3D Secure Logic Bypass (Flag 3)
* **The Vulnerability:** The API leaked **CVV and OTP** codes in plaintext via `/api/cards/info/`.
* **Burp Suite Exploit:** 1. Intercepted the `POST /api/cards/init_payment` request.
    2. Injected the victim's card details.
    3. Confirmed the transaction via `/api/cards/confirm_payment/` using the stolen OTP.
* **Result:** Unauthorized transaction confirmed and **Flag 3** recovered.

---

## 🛠️ Tooling
* **Burp Suite:** Request interception, Repeater, and parameter tampering.
* **Browser DevTools:** Network XHR monitoring and JSON analysis.

---

## ⚠️ Disclaimer
**This project is for educational purposes only.** It was developed and executed within the **Holberton School** sandbox environment to study web security vulnerabilities. 
* All tools and techniques were used in a controlled environment. 
* No real-world financial systems were accessed or harmed during this assessment. 
* The findings documented here are intended to help developers understand and remediate security flaws.
