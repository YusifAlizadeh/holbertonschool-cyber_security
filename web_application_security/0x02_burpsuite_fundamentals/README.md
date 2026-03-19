# 🛰️ Burp Suite Fundamentals

Welcome to the **Burp Suite Fundamentals** directory! This folder documents my proficiency with the industry-standard tool for web application security testing. Each flag represents a successful exercise in intercepting, analyzing, and manipulating HTTP traffic.

## 📌 Overview

Mastering Burp Suite is essential for identifying vulnerabilities that automated scanners often miss. This project covers everything from basic proxy interception to advanced token analysis and automated payload injection.

## 🗂️ Lab Milestones & Tool Mastery

| Flag File | Burp Tool / Module | Learning Objective |
| :--- | :--- | :--- |
| **`0-flag.txt`** | **Proxy & Intercept** | Initial setup and capturing/forwarding baseline HTTP requests. |
| **`1-flag.txt`** | **Target & TLS** | Handling Client-Side TLS Authentication within the Burp ecosystem. |
| **`2-flag.txt`** | **Proxy (Response Mod)** | Manually modifying server responses to reveal hidden UI elements or data. |
| **`3-flag.txt`** | **Repeater** | Manually tweaking and re-sending individual requests to test server logic. |
| **`4-flag.txt`** | **Intruder** | Automating attacks to brute-force or enumerate hidden user profiles. |
| **`5-flag.txt`** | **Sequencer** | Analyzing the randomness and predictability of session tokens. |
| **`6-flag.txt`** | **Decoder** | Manipulating and forging Base64 encoded Bearer tokens for authentication bypass. |

## 🛠️ Security Concepts Applied

* **Interception Proxies:** Acting as a "Man-in-the-Middle" between the client and the server to inspect raw traffic.
* **Request/Response Manipulation:** Altering data on the fly to test how the server handles unexpected input or how the browser renders modified responses.
* **Fuzzing & Enumeration:** Using the **Intruder** tool with wordlists to discover hidden endpoints and resources.
* **Token Analysis:** Using the **Sequencer** to ensure that session identifiers are cryptographically strong and not predictable.
* **Encoding/Decoding:** Quickly translating between formats (Base64, URL, Hex) using the **Decoder** to analyze and forge authentication tokens.

## 🚀 Key Takeaways
Through these labs, I learned how to move beyond the browser's limitations, interacting directly with the server's API and backend logic to uncover vulnerabilities like Broken Access Control and Insecure Authentication.

---

⚠️ **Disclaimer** All projects in this repository are created for educational purposes as part of the Holberton School curriculum. Burp Suite should only be used on applications and networks where you have explicit authorization.
