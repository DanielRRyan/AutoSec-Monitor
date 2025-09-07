# backend/cve_checker.py

import requests
import time
from datetime import datetime, timedelta

# --- NVD API Setup ---
NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
API_KEY = ""  # Optional: Get one from https://nvd.nist.gov/developers/request-an-api-key

HEADERS = {
    "User-Agent": "AutoSec-Monitor/1.0",
}
if API_KEY:
    HEADERS["apiKey"] = API_KEY

# --- List of packages to monitor ---
# You can later auto-load this from your actual project dependencies
MONITORED_PACKAGES = [
    "fastapi",
    "postgresql",
    "vuejs",
    "python",
    "docker",
    "ubuntu",  # For system-level CVEs if running Linux-based containers
]


def fetch_cves_for_keyword(keyword, max_results=5):
    """Search NVD for CVEs related to a given keyword."""
    params = {
        "keywordSearch": keyword,
        "resultsPerPage": max_results,
        "pubStartDate": (datetime.utcnow() - timedelta(days=90)).isoformat() + "Z"
    }

    print(f"🔍 Searching CVEs for '{keyword}'...")
    response = requests.get(NVD_API_URL, params=params, headers=HEADERS)

    if response.status_code == 200:
        cve_data = response.json()
        results = []
        for item in cve_data.get("vulnerabilities", []):
            cve = item["cve"]
            results.append({
                "id": cve["id"],
                "description": cve["descriptions"][0]["value"],
                "cvss": cve.get("metrics", {}),
                "published": cve["published"],
                "source": cve["sourceIdentifier"]
            })
        return results
    else:
        print(f"❌ Error fetching CVEs: {response.status_code}")
        return []


def run_cve_scan():
    """Run CVE checks for all monitored packages."""
    all_alerts = {}

    for pkg in MONITORED_PACKAGES:
        time.sleep(1)  # NVD API rate limit: 1 request/second without API key
        results = fetch_cves_for_keyword(pkg)
        if results:
            all_alerts[pkg] = results

    return all_alerts


# --- For manual testing ---
if __name__ == "__main__":
    cves = run_cve_scan()
    for pkg, entries in cves.items():
        print(f"\n📦 {pkg.upper()} CVEs:")
        for e in entries:
            print(f"- {e['id']}: {e['description'][:100]}...")
