# 🌐 Web Fundamentals & Vulnerability Exploitation

Welcome to the **Web Fundamentals** directory! This folder documents my practical experience in identifying and exploiting common web vulnerabilities through manual analysis and automation.

## 📌 Overview

This project focuses on the "Exploitation" phase of a web penetration test. I explored how misconfigured web headers, unsanitized inputs, and insecure server-side processing can lead to full system compromise.

## 🗂️ Exploitation Catalog

| File Name | Vulnerability Type | Description |
| :--- | :--- | :--- |
| **`1-host_header_injection.sh`** | **Host Header Injection** | A Bash/Curl script that manipulates the HTTP Host header to redirect traffic or poison caches. |
| **`3-xss_payload.txt`** | **Cross-Site Scripting (XSS)** | A JavaScript payload designed to execute in a victim's browser (e.g., for session hijacking). |
| **`5-ticket.txt`** | **HTTP Request Analysis** | A raw GET HTTP request crafted to interact with a specific web endpoint. |
| **`7-rce_payload.txt`** | **Remote Code Execution (RCE)** | A payload designed to execute arbitrary commands on the host server. |

### 🚩 Captured Flags
* **`2-flag.txt` / `4-flag.txt`**: Flags captured through successful Host Header and XSS attacks.
* **`6-flag.txt`**: Access granted to the **Admin Panel** via web exploitation.
* **`8-flag.txt`**: Final flag achieved through **Remote Code Execution (RCE)**.

## 🛠️ Security Concepts Applied

* **Input Validation:** Understanding how the lack of "sanitization" allows attackers to inject malicious code (JS or Shell).
* **HTTP Protocol Manipulation:** Learning how web servers process headers and how to trick them into trusting malicious data.
* **XSS (Cross-Site Scripting):** Executing scripts in the context of a user's session to steal cookies or perform actions on their behalf.
* **RCE (Remote Code Execution):** The most critical vulnerability, allowing an attacker to run OS commands directly on the server.
* **Web Reconnaissance:** Identifying entry points like admin login pages or vulnerable URL parameters.

## 🚀 Tools Used
* **`curl`**: For crafting and sending manual HTTP requests.
* **Browser DevTools**: For inspecting DOM elements and testing XSS.
* **Burp Suite (Conceptual/Manual)**: For intercepting and modifying web traffic.

---

⚠️ **Disclaimer** All projects in this repository are created for educational purposes as part of the Holberton School curriculum. These payloads and scripts are strictly for authorized security testing and should never be used on public websites without permission.
