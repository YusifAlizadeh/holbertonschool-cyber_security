# 🔍 Content Discovery

Welcome to the **Content Discovery** directory! This folder documents my methodology for uncovering hidden assets, forgotten directories, and sensitive information within web applications.

## 📌 Overview

Content discovery is the art of finding "the invisible." Whether it's a backup file, a hidden admin panel, or a developer's comment left in the source code, these hidden gems often provide the first step toward a full compromise. This project covers both **Manual Analysis** and **Automated Fuzzing**.

## 🗂️ Discovery Catalog & Milestones

### 1. 🧠 Manual Discovery (The Human Element)
| File Name | Technique | Discovery Detail |
| :--- | :--- | :--- |
| **`0-flag.txt`** | **Source Code Analysis** | Finding "Secrets in Plain Sight" within HTML/JS comments or hidden fields. |
| **`1-flag.txt`** | **HTTP Header Audit** | Identifying sensitive information leaked via custom or misconfigured server headers. |
| **`2-vendor.txt`** | **Fingerprinting** | "Stalking the Stack" — identifying CMS templates, frameworks, and vendor-specific paths. |
| **`3-senior.txt`** | **OSINT & Archiving** | Using "Time Travel" techniques (Wayback Machine, Google Dorking) to find legacy data. |

### 2. ⚡ The Buster Series (Automated Brute-forcing)
| File Name | Tool Used | Objective |
| :--- | :--- | :--- |
| **`4-flag.txt`** | **GoBuster (Dir)** | Initiating directory brute-forcing to find non-linked paths (e.g., `/backup`, `/dev`). |
| **`5-flag.txt`** | **GoBuster (DNS)** | Unveiling hidden subdomains that might host staging or internal environments. |
| **`6-flag.txt`** | **Fuzzing** | Using fuzzing techniques to identify vulnerable parameters and hidden API endpoints. |

## 🛠️ Security Concepts Applied

* **Information Leakage:** Identifying data that was never intended for public eyes but was left exposed due to negligence.
* **Directory Brute-forcing:** Using wordlists (like `SecLists`) to guess common and uncommon directory names.
* **Subdomain Enumeration:** Expanding the attack surface by finding sibling domains that might have weaker security.
* **OSINT for Web:** Leveraging external archives to find historical vulnerabilities or deleted pages.
* **Fingerprinting:** Determining the underlying technology stack to search for known vulnerabilities (CVEs).

## 🚀 Key Tools
* **GoBuster:** A high-performance tool used for discovering URIs and DNS subdomains.
* **Browser DevTools:** For inspecting DOM, Network headers, and Storage.
* **Wayback Machine / Google Dorks:** For passive history-based discovery.

---

⚠️ **Disclaimer** All projects in this repository are created for educational purposes as part of the Holberton School curriculum. Content discovery should only be performed on systems where you have explicit permission to test.
