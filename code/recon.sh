#!/bin/bash

TARGET=$1

echo "[+] Starting Advanced AI Recon on $TARGET"

echo " AI Recon Script by Abubakar Idris"

# Function to check tool
check_tool() {
    command -v $1 >/dev/null 2>&1
}

echo "[+] WHOIS..."
whois $TARGET > whois.txt 2>/dev/null

echo "[+] DNS..."
dig $TARGET ANY +short > dns.txt

echo "[+] Running Nmap..."
if check_tool nmap; then
    nmap -sV -T4 $TARGET -oN nmap.txt
fi

echo "[+] Detecting Web Tech..."
if check_tool whatweb; then
    whatweb $TARGET > web.txt
fi

echo "[+] Running Nikto (optimized)..."
if check_tool nikto; then
    nikto -h http://$TARGET -Tuning 1,2,3 -maxtime 60 > nikto.txt
fi

echo "[+] Running AI Analysis..."
python3 ai_analysis.py $TARGET

echo "[+] Recon Completed"
