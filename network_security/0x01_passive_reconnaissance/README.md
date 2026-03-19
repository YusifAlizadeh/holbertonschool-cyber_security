# 📡 Passive Reconnaissance

Welcome to the **Passive Reconnaissance** directory! This folder contains tools and reports focused on gathering information about a target without sending any packets directly to the target's infrastructure.

## 📌 Overview

Passive reconnaissance is the first phase of an ethical hacking engagement. By leveraging public records, DNS data, and third-party services, an investigator can map out an organization's digital footprint while remaining completely invisible to their security systems.

## 🗂️ Script Catalog & Features

### DNS & Domain Intelligence
| Script Name | Tool Used | Description |
| :--- | :--- | :--- |
| **`0-whois.sh`** | `whois` | Extracts domain registration details and exports them in CSV format. |
| **`1-a_record.sh`** | `nslookup` | Retrieves the **A record** (IP address) for a specified domain. |
| **`2-mx_record.sh`** | `nslookup` | Identifies the **MX records** (Mail Servers) for the target domain. |
| **`3-txt_record.sh`** | `nslookup` | Fetches **TXT records**, often used for SPF, DKIM, and verification codes. |
| **`4-dig_all.sh`** | `dig` | Performs a comprehensive DNS query to retrieve all available records. |
| **`5-subfinder.sh`** | `subfinder` | Automates subdomain discovery to expand the target's attack surface. |

### Capture The Flag (CTF) Results
* **`100-flag.txt` / `101-flag.txt` / `102-flag.txt`:** Captured flags from reconnaissance challenges, involving name servers and mail server identification.

### Reports
* **`holbertonschool_report.md`:** A detailed markdown report documenting the reconnaissance findings and methodology.

## 🛠️ Security Concepts Applied

* **OSINT (Open Source Intelligence):** Using publicly available data to build a profile of the target.
* **DNS Enumeration:** Mapping out hostnames and infrastructure through DNS record analysis.
* **Subdomain Discovery:** Finding "hidden" or forgotten subdomains that might have weaker security than the main site.
* **Footprinting:** The process of creating a blueprint of a target's network and systems.

## 🚀 Why Passive Recon?
In a real-world scenario, active scanning (like `nmap`) can be detected by Intrusion Detection Systems (IDS). Passive techniques allow an analyst to find:
1. IP ranges owned by the company.
2. Email providers and potential security misconfigurations in DNS (like weak SPF records).
3. Hidden development or staging environments via subdomains.

---

⚠️ **Disclaimer** All projects in this repository are created for educational purposes as part of the Holberton School curriculum. Always ensure you have permission before performing reconnaissance on any domain.
