# 🔐 Cryptography Basics

Welcome to the **Cryptography Basics** directory! This folder documents my transition from theoretical encryption to hands-on practical application, focusing on hashing algorithms, password security, and recovery techniques.

## 📌 Overview

The core of this project is understanding **Data Integrity** and **Authentication**. I explored the evolution of hashing functions—from older, vulnerable standards to modern, computationally expensive algorithms designed to resist brute-force attacks.

## 🗂️ Topics Covered

### 1. 🧬 Hashing Algorithms
A deep dive into the properties of one-way functions and their specific use cases:
* **MD5 & SHA-1:** Analysis of "legacy" hashes. Understanding collision vulnerabilities and why they are no longer suitable for security but still used for basic file integrity.
* **SHA-256:** Studying the industry standard for digital signatures and secure data verification.
* **bcrypt:** Exploring "salted" and "stretched" hashes. Learning why bcrypt is superior for password storage due to its adaptive cost factor.

### 2. ⚡ Password Recovery & Cracking Tools
Hands-on experience with industry-leading tools to test credential strength:
* **John the Ripper (JtR):** Using this versatile tool for dictionary attacks and "single crack" modes.
* **Hashcat:** Leveraging the world's fastest password recovery utility. I practiced identifying hash types and using rule-based attacks to simulate real-world password guessing.
* **Wordlists & Rules:** Utilizing `rockyou.txt` and custom rules to understand how patterns in human behavior affect password security.

### 3. 🛡️ Security Concepts
* **Salting:** Why adding unique random data to a password before hashing is critical to preventing Rainbow Table attacks.
* **Pepper:** Understanding the role of a secret key stored outside the database.
* **Rainbow Tables vs. Brute Force:** Comparing pre-computed hash tables against real-time calculation.

## 🛠️ Tools Utilized

* **Hashcat:** GPU-optimized hash cracking.
* **John the Ripper:** Fast, CPU-based password auditing.
* **OpenSSL:** For manual hash generation and testing.
* **Python/Bash:** Scripting simple automation for hash comparison.

## 📝 Learning Objectives

* Differentiate between **Encryption** (reversible) and **Hashing** (one-way).
* Identify hash types by their length and character sets (Hex vs. Base64).
* Understand the "Work Factor": Why making a hash slow is a feature, not a bug.
* Evaluate the strength of organizational password policies through simulated audits.

---

⚠️ **Disclaimer** All projects in this repository are created for educational purposes as part of the Holberton School curriculum.
