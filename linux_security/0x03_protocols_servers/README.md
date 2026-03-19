# 🌐 Protocols & Server Security

Welcome to the **Protocols & Server Security** directory! This folder contains a comprehensive suite of Bash scripts designed for auditing, hardening, and testing the resilience of common network services and protocols.

## 📌 Overview

A server is only as secure as its weakest protocol configuration. This project focuses on identifying misconfigurations in standard services (like SSH, SNMP, and SMTP) and implementing proactive defense mechanisms using firewalls and encryption audits.

## 🗂️ Script Catalog & Features

| Script Name | Category | Description |
| :--- | :--- | :--- |
| **`0-iptables.sh`** | Firewall | Displays all active `iptables` rules in a clear, human-readable format. |
| **`1-audit.sh`** | SSH Security | Audits SSH configurations for non-standard or insecure settings. |
| **`2-harden.sh`** | File System | Identifies and secures world-writable directories to prevent unauthorized data injection. |
| **`3-identify.sh`** | Vulnerability | Uses the `Lynis` auditing tool to discover unpatched system vulnerabilities. |
| **`4-nfs.sh`** | Network Shares | Scans for publicly accessible NFS (Network File System) shares. |
| **`5-snmp.sh`** | SNMP Audit | Finds SNMP configurations that inadvertently allow public access to system info. |
| **`6-smtp.sh`** | Email Security | Checks SMTP servers for the absence of `STARTTLS` (unencrypted mail transfer). |
| **`7-dos.sh`** | Stress Testing | Simulates a basic DoS (Denial of Service) attack to test web server resilience. |
| **`8-cipher.sh`** | Encryption | Tests SSL/TLS servers for weak or deprecated cryptographic ciphers. |
| **`9-firewall.sh`** | Hardening | Implements a "Default Drop" policy, blocking all traffic except for SSH and HTTP. |

## 🛠️ Security Concepts Applied

* **Attack Surface Reduction:** Disabling unnecessary services and closing unused ports to minimize entry points.
* **Service Hardening:** Moving beyond default settings to secure protocols like SSH and SMTP.
* **Encryption Auditing:** Ensuring that data in transit is protected by strong TLS/SSL ciphers.
* **Network Reconnaissance (Defensive):** Using scanning techniques to find "leaky" services (NFS, SNMP) before an attacker does.
* **Resilience Testing:** Understanding how DoS attacks work to better configure rate-limiting and defensive buffers.

## 🚀 Key Tools Used
* **`iptables`**: For stateful packet filtering.
* **`Lynis`**: For professional-grade system hardening audits.
* **`nmap` / `ss`**: For service and port identification.
* **`openssl`**: For testing TLS handshakes and ciphers.

---

⚠️ **Disclaimer** All projects in this repository are created for educational purposes as part of the Holberton School curriculum. The DoS simulation script (`7-dos.sh`) must ONLY be used on systems you own or have explicit permission to test.
