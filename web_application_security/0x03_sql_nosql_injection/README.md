# 🗄️ SQL & NoSQL Injection

Welcome to the **SQL & NoSQL Injection** directory! This folder documents my technical journey in understanding how poorly sanitized database queries can be manipulated to leak sensitive information or bypass authentication.

## 📌 Overview

Database injections are among the most impactful vulnerabilities in the OWASP Top 10. This project covers the exploitation of traditional Relational Databases (SQL) and modern Document-Oriented Databases (NoSQL), demonstrating how different architectures require different attack vectors.

## 🗂️ Exploitation Catalog & Milestones

### 1. 🐘 SQL Injection (SQLi)
| File Name | Attack Type | Description |
| :--- | :--- | :--- |
| **`1-flag.txt`** | **In-Band SQLi** | Extracting database metadata (version, user, schema names) using `UNION` based techniques. |
| **`2-flag.txt`** | **Data Exfiltration** | Targeted extraction of sensitive data from specific application tables. |
| **`3-flag.txt`** | **Time-Based Blind** | Exfiltrating data by measuring server response delays using `SLEEP()` or `WAITFOR` commands. |
| **`4-flag.txt`** | **Second-Order Blind** | Exploiting vulnerabilities where the payload is stored by the app and executed later in a different context. |

### 2. 🍃 NoSQL Injection (NoSQLi)
| File Name | Attack Type | Description |
| :--- | :--- | :--- |
| **`5-vuln.txt`** | **Discovery** | Identifying entry points in JSON/BSON objects that accept NoSQL operators (e.g., `$gt`, `$ne`). |
| **`6-flag.txt`** | **Auth Bypass** | Bypassing login screens by injecting logical operators into the credentials check. |
| **`7-flag.txt`** | **Data Enumeration** | Using conditional injection to leak database contents from a NoSQL backend (like MongoDB). |

## 🛠️ Security Concepts Applied

* **Query Manipulation:** Altering the logic of backend queries to return `TRUE` or leak unauthorized data.
* **Blind Injection:** Understanding how to "ask the database questions" when no data is directly reflected on the page (Boolean-based or Time-based).
* **Second-Order Attacks:** Identifying vulnerabilities that are not immediate but persist in the database to be triggered later.
* **NoSQL Operator Injection:** Exploiting logic in non-relational databases by injecting objects instead of simple strings.
* **Defense-in-Depth:** Learning the importance of Prepared Statements (Parameterized Queries) and proper input sanitization.

## 📝 Learning Objectives

* Differentiate between SQL (structured) and NoSQL (document-based) injection methodologies.
* Master the art of manual data exfiltration through trial and error.
* Understand why "Blacklisting" characters is an insufficient defense compared to using secure API practices.

---

⚠️ **Disclaimer** All projects in this repository are created for educational purposes as part of the Holberton School curriculum. These techniques are strictly for authorized security testing and ethical hacking labs.
