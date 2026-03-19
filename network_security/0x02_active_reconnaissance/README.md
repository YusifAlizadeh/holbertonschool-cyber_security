# 🔍 Active Reconnaissance

Welcome to the **Active Reconnaissance** directory! This folder documents my hands-on experience with active scanning, service enumeration, and web infrastructure analysis.

## 📌 Overview

Active reconnaissance involves direct interaction with the target system to gather detailed information. This phase is essential for identifying open ports, running services, and potential entry points like hidden directories or injectable parameters.

## 🗂️ Reconnaissance Logs & Findings

This folder contains the results of various scanning and enumeration tasks:

| File Name | Investigation Target | Key Findings |
| :--- | :--- | :--- |
| **`0-ports.txt`** | Port Scanning | Identification of open TCP/UDP ports and listening services. |
| **`1-webserver.txt`** | Banner Grabbing | Discovery of the web server software and version (e.g., Apache, Nginx). |
| **`2-injectable.txt`** | Vulnerability Research | Identification of parameters susceptible to injection (e.g., SQLi, XSS). |
| **`3-database.txt`** | Database Enumeration | Details about the backend database management system (DBMS). |
| **`4-tables.txt`** | Data Mapping | Enumeration of database tables retrieved through successful injection/access. |
| **`5-hidden_dir.txt`** | Directory Brute-forcing | Discovery of hidden admin panels and non-indexed directories. |

### 🚩 Capture The Flag (CTF) Milestone
* **`100-flag.txt` / `101-flag.txt` / `102-flag.txt`:** Documentation of flags captured during active exploitation, including the elusive **Admin Flag**.

## 🛠️ Security Concepts & Techniques

* **Port Scanning:** Probing a server to see which "doors" are open.
* **Service Enumeration:** Fingerprinting services to find specific versions with known vulnerabilities (CVEs).
* **Fuzzing & Directory Discovery:** Using wordlists to find sensitive paths like `/admin`, `/config`, or `.env`.
* **Database Scouting:** Understanding the structure of the backend to prepare for data extraction.
* **Manual vs. Automated Recon:** Balancing the use of tools (like `nmap`, `gobuster`) with manual verification to bypass simple filters.



## 🚀 Why Active Recon?
While passive recon gives you the "what" and "where," active recon gives you the **"how."** By the end of this phase, an analyst has a clear map of the target's attack surface, knowing exactly which service to target and which vulnerability to exploit.

---

⚠️ **Disclaimer** All projects in this repository are created for educational purposes as part of the Holberton School curriculum. Active reconnaissance should only be performed on systems for which you have explicit, written authorization.
