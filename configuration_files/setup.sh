#!/bin/bash

# ==========================================
# AI Recon Lab Setup Script
# Author: Abubakar Idris
# Description: Installs all required tools for AI-based reconnaissance
# ==========================================

echo "=========================================="
echo " AI Recon Lab Setup Starting..."
echo " Author: Abubakar Idris"
echo "=========================================="

# Step 1: Fix Kali Repository (if broken)
echo "[+] Configuring Kali repositories..."

sudo bash -c 'cat > /etc/apt/sources.list <<EOF
deb http://http.kali.org/kali kali-rolling main contrib non-free
deb-src http://http.kali.org/kali kali-rolling main contrib non-free
EOF'

# Remove problematic debug repo if exists
sudo rm -f /etc/apt/sources.list.d/kali-debug.list

# Step 2: Update system
echo "[+] Updating system packages..."
sudo apt clean
sudo apt update -y
sudo apt full-upgrade -y

# Step 3: Install core tools
echo "[+] Installing reconnaissance tools..."

sudo apt install -y \
nmap \
nikto \
whatweb \
dnsenum \
sublist3r \
theharvester \
whois \
dnsutils \
git \
curl \
python3 \
python3-pip

# Step 4: Install Python libraries (for AI analysis)
echo "[+] Installing Python dependencies..."

pip3 install --upgrade pip

pip3 install \
numpy \
pandas \
scikit-learn \
matplotlib

# Step 5: Fix Sublist3r issues (optional dependency update)
echo "[+] Fixing Sublist3r dependencies..."

pip3 install requests

# Step 6: Verify installations
echo "[+] Verifying installed tools..."

echo "------------------------------------------"
echo "Installed Tools:"
which nmap
which nikto
which whatweb
which dnsenum
which sublist3r
which theHarvester
which python3
echo "------------------------------------------"

# Step 7: Display versions
echo "[+] Tool Versions:"
nmap --version | head -n 1
nikto -Version
whatweb --version
dnsenum --version 2>/dev/null
theHarvester --version
python3 --version

echo "=========================================="
echo " Setup Completed Successfully!"
echo " Environment Ready for AI Recon"
echo "=========================================="
