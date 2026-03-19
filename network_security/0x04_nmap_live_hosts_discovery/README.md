# 📡 Nmap Live Host Discovery

Welcome to the **Nmap Live Host Discovery** directory! This folder contains a collection of Bash scripts focused on the "Ping Sweep" phase of network reconnaissance—identifying active devices within a subnetwork using various protocols and techniques.

## 📌 Overview

Host discovery is the process of enumerating active machines on a network. Since different systems and firewalls respond differently to various probes, this project explores multiple methods—from layer 2 (ARP) to layer 4 (TCP/UDP)—to ensure accurate network mapping.



## 🗂️ Script Catalog & Features

| Script Name | Method | Description |
| :--- | :--- | :--- |
| **`0-arp_scan.sh`** | **ARP Scan** | Discovers hosts on the local network. Highly accurate as it operates at Layer 2 and cannot be blocked by IP firewalls. |
| **`1-icmp_echo_scan.sh`** | **ICMP Echo** | The classic "Ping" request. Effective for discovering standard workstations and servers. |
| **`2-icmp_timestamp.sh`** | **ICMP Timestamp** | Uses non-standard ICMP queries to bypass firewalls that only block Echo requests. |
| **`3-icmp_mask_scan.sh`** | **ICMP Address Mask** | Another alternative ICMP probe used to elicit responses from systems with specific security configurations. |
| **`4-tcp_syn_ping.sh`** | **TCP SYN Ping** | Sends an empty SYN packet to a specific port (usually 80 or 443). A response indicates the host is alive. |
| **`5-tcp_ack_ping.sh`** | **TCP ACK Ping** | Sends an ACK packet to spoof an established connection, often effective at bypassing stateful firewalls. |
| **`6-udp_ping_scan.sh`** | **UDP Ping** | Sends UDP packets to rare ports to trigger an ICMP Port Unreachable message from an active host. |

### 🚩 Capture The Flag (CTF)
* **`100-flag.txt`:** Documentation of the flag captured during the Nmap host discovery challenge.

## 🛠️ Security Concepts Applied

* **Layer 2 Discovery:** Using **ARP** for lightning-fast and undetectable (by firewalls) scanning within the same local subnet.
* **Bypassing Firewalls:** Experimenting with **ACK Ping** and **ICMP Timestamps** to discover hosts that ignore standard Echo requests.
* **TCP/UDP Probing:** Leveraging the 3-way handshake mechanics to verify if a machine is online without completing a full connection.
* **Network Mapping:** Calculating the size and scope of a target network before performing deep port scans.

## 🚀 Why different scan types?
Modern networks are often "silent." A simple `ping` might return nothing, but an **ACK Ping** on port 80 might reveal a hidden web server. These scripts provide a toolkit to see through basic network filtering.

---

⚠️ **Disclaimer** All projects in this repository are created for educational purposes as part of the Holberton School curriculum. Only scan networks where you have explicit authorization.
