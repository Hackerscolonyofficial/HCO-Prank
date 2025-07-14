#!/bin/bash
clear
echo -e "\e[32m╔══════════════════════════════════════════════════╗"
echo -e "\e[31m     HCO-Prank - Browser Lockdown Tool (v2.0)"
echo -e "\e[32m╚══════════════════════════════════════════════════╝\e[0m"
echo ""
echo -e "\e[33m[!] This tool is not free. Subscribe to continue."
echo -e "\e[36m[>] Redirecting to Hackers Colony YouTube in 10 seconds...\e[0m"
sleep 10
termux-open-url "https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya"
read -p $'\e[32m[✔] After subscribing, press Enter to continue...\e[0m'
python main.py
