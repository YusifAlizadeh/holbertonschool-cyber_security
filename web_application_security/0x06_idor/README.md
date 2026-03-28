🛡️ CyberBank: IDOR & 3D Secure Bypass Assessment
📌 Project Overview
This repository contains the findings and methodology of a targeted security assessment of the CyberBank web application. The project focuses on identifying and exploiting Insecure Direct Object Reference (IDOR) vulnerabilities and logic flaws within the 3D Secure payment confirmation flow.

🎯 Objectives
Identify broken access control in API endpoints.

Expose sensitive PII (Personally Identifiable Information) through IDOR.

Demonstrate a full bypass of 3D Secure authentication using intercepted OTPs.

Document the findings in a professional security report format.

🚀 Vulnerability Chain Discovery
1. Information Reconnaissance (Flag 0)
Using the browser Network Tab, I identified that the application fetches transaction history via /api/customer/transactions. This endpoint leaked internal UUIDs of other customers.

Exploit: Manual IDOR on /api/customer/info/[UUID].

Result: Access to full profile of another user (Patricia Garcia) and recovery of Flag 0.

2. Deep Account Access (Flag 1)
By extracting account_id from the previous step, I tested the account-specific API.

Exploit: IDOR on /api/accounts/info/[ACCOUNT_UUID].

Result: Exposure of bank account balances, routing numbers, and associated card IDs. Recovery of Flag 1.

3. 3D Secure Bypass & Payment Manipulation (Flag 3)
The most critical finding involved intercepting the payment initiation process.

Method: Using Burp Suite, I intercepted the POST /api/cards/init_payment request and replaced my account details with the victim's card data (leaked from /api/cards/info/).

Bypass: The system leaked the OTP in plaintext via a GET request. I used this OTP to confirm the transaction via /api/cards/confirm_payment/.

Result: Unauthorized upgrade purchase and recovery of Flag 3.

🛠️ Tools Used
Burp Suite (Proxy & Repeater): For intercepting, modifying, and replaying HTTP requests.

Mozilla Firefox DevTools: For monitoring XHR requests and analyzing JSON responses.

REST API Testing: Manual manipulation of RESTful endpoints.

📁 Repository Structure
/screenshots: Contains evidence of successful exploits and flags.

REPORT.md: The detailed professional vulnerability report.

METHODOLOGY.md: Detailed steps on how the environment was tested.

📝 Key Recommendations
Enforce Object-Level Authorization: Validate user ownership for every resource request on the backend.

Secure OTP Transmission: Never expose OTPs or CVVs through GET API endpoints.

Data Masking: Sensitive financial identifiers should be masked in transit and at rest.

⚖️ Disclaimer
This project was performed in a controlled, simulated environment for educational purposes as part of a Holberton Cybersecurity curriculum. No real banking systems were harmed.
