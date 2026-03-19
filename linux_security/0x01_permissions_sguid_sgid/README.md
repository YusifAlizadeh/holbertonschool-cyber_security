# 🔑 Permissions, SUID & SGID

Welcome to the **Permissions, SUID & SGID** directory! This folder contains a set of Bash scripts focused on user management, group policies, and identifying potential security vulnerabilities related to special Linux permissions.

## 📌 Overview

In Linux, incorrect permissions are one of the most common ways an attacker can gain root access. This project explores how to manage users and groups, and specifically how to audit **SUID (Set User ID)** and **SGID (Set Group ID)** bits, which allow a file to be executed with the privileges of the file owner or group.

## 🗂️ Script Catalog & Features

| Script Name | Description | Key Functionality |
| :--- | :--- | :--- |
| **`0-add_user.sh`** | User Provisioning | Automates the creation of a new user and sets their initial password. |
| **`1-add_group.sh`** | Group & Ownership | Creates a new group and updates directory ownership accordingly. |
| **`2-sudo_nopass.sh`** | Sudoers Configuration | Configures the system to allow specific script execution without a password prompt. |
| **`3-find_files.sh`** | Vulnerability Scanner | Specifically searches for known SUID vulnerabilities in a directory. |
| **`4-find_suid.sh`** | SUID Auditor | Lists all files with the SUID bit set (runs as owner). |
| **`5-find_sgid.sh`** | SGID Auditor | Lists all files with the SGID bit set (runs as group). |
| **`6-check_files.sh`** | Recent Activity Audit | Finds files modified in the last 24 hours with specific permission sets. |
| **`7-file_read.sh`** | Permission Lockdown | Changes all files in a directory to be read-only for security. |
| **`8-change_user.sh`** | Ownership Manager | Changes the owner and group of files to maintain strict access control. |
| **`9-empty_file.sh`** | Cleanup & Access | Finds empty files and resets permissions to a full-access state. |

## 🛠️ Core Security Concepts

* **Privilege Escalation:** Understanding how SUID/SGID bits can be abused to gain unauthorized high-level access.
* **The Principle of Least Privilege (PoLP):** Ensuring users and programs have only the minimum permissions necessary.
* **System Hardening:** Reducing the attack surface by finding and removing unnecessary SUID/SGID bits from binary files.
* **User & Group Administration:** Managing identity and access (IAM) via the command line.

## 🚀 How to Audit SUID/SGID

Files with SUID permissions are often represented in a long list (`ls -l`) with an `s` in the owner's execution field:
`-rwsr-xr-x` — The `s` indicates that any user running this file will have the owner's (often root) privileges.

Example of running an auditor script:
```bash
chmod +x 4-find_suid.sh
sudo ./4-find_suid.sh /usr/bin
```

⚠️ Disclaimer All projects in this repository are created for educational purposes as part of the Holberton School curriculum.
