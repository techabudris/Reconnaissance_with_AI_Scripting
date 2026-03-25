import sys
from datetime import datetime

# ----------------------------
# INPUT
# ----------------------------
target = sys.argv[1]

print(f"\n[AI] Advanced Analysis for: {target}\n")

risk_score = 0
findings = []
confidence = "Medium"

# ----------------------------
# HELPER FUNCTION
# ----------------------------
def analyze_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read().lower()
    except FileNotFoundError:
        return ""

# ----------------------------
# LOAD DATA
# ----------------------------
nmap_data = analyze_file("nmap.txt")
nikto_data = analyze_file("nikto.txt")
web_data = analyze_file("web.txt")
dns_data = analyze_file("dns.txt")

# ----------------------------
#  NMAP ANALYSIS
# ----------------------------
if "22/tcp" in nmap_data:
    risk_score += 1
    findings.append("SSH port (22) open")

if "80/tcp" in nmap_data:
    risk_score += 1
    findings.append("HTTP service detected")

if "587/tcp" in nmap_data:
    risk_score += 2
    findings.append("SMTP service exposed (port 587)")

if "open" in nmap_data:
    risk_score += 2

# ----------------------------
#  WEB ANALYSIS
# ----------------------------
if "apache" in web_data:
    risk_score += 1
    findings.append("Apache web server detected")

if "2.4.7" in web_data:
    risk_score += 2
    findings.append("Outdated Apache version (possible known CVEs)")

if "ubuntu" in web_data:
    findings.append("Linux (Ubuntu) server identified")

# ----------------------------
#  NIKTO ANALYSIS
# ----------------------------
if "outdated" in nikto_data:
    risk_score += 2
    findings.append("Outdated server software")

if "missing" in nikto_data:
    risk_score += 2
    findings.append("Missing security headers (CSP, HSTS, etc.)")

if "mod_negotiation" in nikto_data:
    risk_score += 1
    findings.append("Apache MultiViews enabled (information disclosure risk)")

if "options:" in nikto_data:
    risk_score += 1
    findings.append("Multiple HTTP methods enabled")

# ----------------------------
#  DNS / IPv6 ANALYSIS
# ----------------------------
if ":" in dns_data:
    risk_score += 1
    findings.append("IPv6 detected (additional attack surface)")

# ----------------------------
#  CONTEXT AWARENESS
# ----------------------------
if "scanme.nmap.org" in target:
    findings.append("Target is a known controlled test environment (Nmap)")
    confidence = "High (environment identified)"

# ----------------------------
#  RISK CLASSIFICATION
# ----------------------------
if risk_score >= 12:
    risk_level = "🔴 High Risk"
elif risk_score >= 6:
    risk_level = "🟠 Medium Risk"
else:
    risk_level = "🟢 Low Risk"

# ----------------------------
#  OUTPUT DISPLAY
# ----------------------------
print("[AI] Findings:")
for f in findings:
    print(f"  - {f}")

print(f"\n[AI] Risk Score: {risk_score}")
print(f"[AI] Risk Level: {risk_level}")
print(f"[AI] Confidence Level: {confidence}")

# ----------------------------
#  SAVE REPORT
# ----------------------------
report = f"""
AI RECONNAISSANCE REPORT
========================
Target: {target}
Date: {datetime.now()}

Findings:
"""

for f in findings:
    report += f"- {f}\n"

report += f"""
Risk Score: {risk_score}
Risk Level: {risk_level}
Confidence: {confidence}
"""

with open("ai_report.txt", "w") as f:
    f.write(report)

print("\n[AI] Report saved as ai_report.txt")
print("[AI] Analysis Complete\n")
