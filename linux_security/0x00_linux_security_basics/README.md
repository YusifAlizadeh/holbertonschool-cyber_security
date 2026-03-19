# 🐧 Linux Security Basics

Welcome to the **Linux Security Basics** directory! This folder contains a collection of Bash scripts designed to automate system monitoring, network defense, and security auditing on Linux systems.

## 📌 Overview

The scripts in this repository focus on hardening a Linux environment, monitoring user activity, and managing network traffic. These tools represent the "first line of defense" for a system administrator or security analyst.

## 🗂️ Script Catalog & Features

| Script Name | Description | Key Functionality |
| :--- | :--- | :--- |
| **`0-login_sessions.sh`** | User Activity Monitor | Displays the last 5 login sessions to track user access patterns. |
| **`1-active-connections.sh`** | Network Socket Lister | Displays a real-time list of all active network socket connections. |
| **`2-incoming_connections.sh`** | Traffic Filter | Configures rules to allow only incoming connections via the TCP protocol. |
| **`3-firewall_rules.sh`** | Firewall Auditor | Lists all current rules in the security table of the system firewall. |
| **`4-network_services.sh`** | Service Inventory | Lists all running services, their current state, and corresponding ports. |
| **`5-audit_system.sh`** | System Auditor | Initiates a comprehensive system audit to scan for vulnerabilities. |
| **`6-capture_analyze.sh`** | Traffic Analyzer | Captures and analyzes live network traffic (Packet Sniffing). |
| **`7-scan.sh`** | Subnetwork Discovery | Scans a subnetwork to discover live hosts and map the local network. |

## 🛠️ Security Concepts Applied

* **Access Control:** Monitoring logins to detect unauthorized access or brute-force attempts.
* **Firewall Management:** Implementing the principle of "Least Privilege" by filtering unnecessary traffic.
* **Network Visibility:** Identifying listening services and open ports that could be potential entry points.
* **Traffic Analysis:** Understanding packet flow and protocols to identify suspicious network behavior.
* **System Auditing:** Regular health checks and scanning to ensure compliance with security standards.

## 🚀 Requirements & Execution

Most of these scripts interact with system-level configurations and network interfaces.
* **Privileges:** Root or `sudo` access is required for most scripts (especially firewall and traffic capture).
* **Tools:** Uses standard Linux utilities like `ss`, `iptables`, `tcpdump`, and `nmap`.

Example usage:
```bash
chmod +x 6-capture_analyze.sh
sudo ./6-capture_analyze.sh
```

⚠️ Disclaimer

All projects in this repository are created for educational purposes as part of the Holberton School curriculum.
