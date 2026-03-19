# 📤 Upload Vulnerabilities

Welcome to the **Upload Vulnerabilities** directory! This folder contains a series of lab results and techniques focused on bypassing file upload restrictions to achieve **Remote Code Execution (RCE)**.

## 📌 Overview

File upload functionality is a high-risk feature in web applications. This project explores how developers attempt to secure uploads and, more importantly, how those defenses can be systematically bypassed through various injection and manipulation techniques.

## 🗂️ Bypass Techniques & Milestones

| File Name | Defense Mechanism | Bypass Technique |
| :--- | :--- | :--- |
| **`0-target.txt`** | Reconnaissance | Identifying subdomains and upload endpoints for testing. |
| **`1-flag.txt`** | **Client-Side Filtering** | Bypassing JavaScript-based file type checks by intercepting and modifying the request (e.g., using Burp Suite). |
| **`2-flag.txt`** | **Filename Manipulation** | Using special characters, null bytes, or double extensions to trick the server-side storage logic. |
| **`3-flag.txt`** | **MIME-Type & Magic Numbers** | Spoofing the "Magic Bytes" (file signatures) to make a malicious script appear as a legitimate image (e.g., GIF89a). |
| **`4-flag.txt`** | **Server-Side Execution Prevention** | Overcoming sophisticated measures designed to prevent the execution of uploaded scripts in the web root. |

## 🛠️ Security Concepts Applied

* **Unrestricted File Upload:** The root cause where a server allows any file type to be uploaded and executed.
* **Content-Type Spoofing:** Manually changing the `Content-Type` header in an HTTP request to fool the server.
* **Magic Bytes Analysis:** Understanding that servers often check the first few bytes of a file (e.g., `FF D8 FF` for JPEG) rather than just the extension.
* **Web Shells:** Uploading small scripts (PHP, ASPX, JSP) to gain an interactive command-line interface on the target server.
* **Filter Evasion:** Using techniques like `.php5`, `.phtml`, or changing case (`.PhP`) to bypass blacklist-based filters.

## 🚀 Impact of Success
A successful file upload bypass typically results in **Critical** impact, allowing an attacker to:
1. Execute arbitrary system commands.
2. Read sensitive configuration files (e.g., database credentials).
3. Deface the website or pivot further into the internal network.

---

⚠️ **Disclaimer** All projects in this repository are created for educational purposes as part of the Holberton School curriculum. Testing file upload vulnerabilities on live systems without permission is illegal and unethical.
