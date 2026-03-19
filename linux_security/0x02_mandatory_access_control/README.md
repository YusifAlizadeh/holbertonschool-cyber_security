# 🛡️ Mandatory Access Control (MAC)

Welcome to the **Mandatory Access Control** directory! This folder contains a collection of Bash scripts focused on managing and auditing high-level security frameworks in Linux, specifically **SELinux** (Security-Enhanced Linux) and **AppArmor**.

## 📌 Overview

Unlike standard Discretionary Access Control (DAC), where users control their own files, **MAC** is enforced by the system kernel. This project explores how to configure policies that restrict even the most privileged users (root), providing a robust layer of defense against zero-day exploits and service compromises.

## 🗂️ Script Catalog & Features

| Script Name | Description | Key Functionality |
| :--- | :--- | :--- |
| **`0-analyse_mode.sh`** | SELinux Status | Identifies if SELinux is in `Enforcing`, `Permissive`, or `Disabled` mode. |
| **`1-security_match.sh`** | AppArmor Auditor | Checks the status of AppArmor profiles (Enforce, Complain, or Unconfined). |
| **`2-list_http.sh`** | Network Contexts | Lists all network ports managed by SELinux, filtered for HTTP-related types. |
| **`3-add_port.sh`** | Policy Modification | Grants permissions to a specific TCP port (8080) by adding it to `http_port_t`. |
| **`4-list_user.sh`** | Identity Mapping | Displays the mapping between Linux users and SELinux confined identities. |
| **`5-add_selinux.sh`** | User Containment | Links a Linux login to a specific SELinux user role for restricted access. |
| **`6-list_booleans.sh`** | Feature Toggles | Lists all SELinux Booleans, which allow on-the-fly policy changes. |
| **`7-set_sendmail.sh`** | Boolean Management | Permanently enables the `httpd_can_sendmail` toggle to allow web servers to send emails. |

## 🛠️ Core Security Concepts

* **Labeling & Contexts:** Understanding how files, processes, and ports are assigned security contexts (e.g., `user:role:type:level`).
* **Enforcing vs. Permissive:** Learning how to test policies without breaking services using `Permissive` mode.
* **Type Enforcement (TE):** The core of SELinux that limits what a "type" (process) can do to another "type" (object).
* **Booleans:** Using simple switches to modify complex security policies without recompiling the kernel.
* **AppArmor Profiles:** Understanding path-based access control as an alternative to SELinux's label-based approach.

## 🚀 Why this matters?
Even if an attacker gains a shell via a vulnerability in `httpd`, **MAC** (SELinux/AppArmor) will prevent them from reading sensitive files like `/etc/shadow` or pivoting to other parts of the network, as the process context strictly forbids it.

---

⚠️ **Disclaimer** All projects in this repository are created for educational purposes as part of the Holberton School curriculum.
