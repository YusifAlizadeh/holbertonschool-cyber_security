# 🔐 Introduction to Cybersecurity

Welcome to my **Introduction to Cybersecurity** workspace! This folder contains scripts, notes, and exercises focused on the foundational concepts of cryptography, data integrity, and secure key management.

## 📌 About This Folder

This repository serves as a practical sandbox for learning how data is secured and verified. Here, I explore how to generate cryptographic keys, compute hashes, and understand the core mechanics behind encryption and authentication.

## 🗂️ Topics Covered

* **Key Generation (`gen key`):** Generating secure cryptographic keys (such as RSA key pairs or symmetric keys) used for secure communication, encryption, and digital signatures.
* **Hashing & Checksums (`gen sha`):** Calculating SHA (Secure Hash Algorithm) digests (like SHA-256) to verify file integrity and understand how one-way cryptographic functions work.
* **Data Integrity:** Exploring how hashes and keys are used in the real world to ensure data has not been tampered with or corrupted.

## ⚙️ Prerequisites

To run the scripts and commands in this folder, you will generally need a standard Linux/Unix environment (or WSL on Windows). Common tools utilized in these exercises include:

* `openssl` (for key generation and advanced cryptographic operations)
* Standard hashing utilities (e.g., `sha256sum`, `sha1sum`)

## 🚀 Usage Examples

*(Note: These are standard examples. Adjust the script names to match your exact files.)*

**Generating a SHA Hash:**
```bash
# Running a custom script to generate a hash
./gen_sha.sh my_document.txt
