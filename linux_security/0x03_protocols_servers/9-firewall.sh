#!/bin/bash
iptables -F
iptables -A INPUT -J DROP
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
