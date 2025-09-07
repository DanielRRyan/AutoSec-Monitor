# scripts/fetch_cve_data.py
import requests

def fetch_cves(package_name):
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={package_name}&resultsPerPage=5"
    headers = {"apiKey": "your-api-key"}  # optional if you use NVD
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching CVEs for {package_name}")
        return []

    data = response.json()
    cves = []

    for item in data.get("vulnerabilities", []):
        cve = item["cve"]
        cves.append({
            "id": cve["id"],
            "description": cve.get("descriptions", [{}])[0].get("value", ""),
            "published": cve.get("published"),
            "source": "NVD"
        })

    return cves

# Example usage
if __name__ == "__main__":
    for pkg in ["fastapi", "vuejs", "postgresql"]:
        result = fetch_cves(pkg)
        print(f"\n{pkg.upper()} CVEs:")
        for cve in result:
            print(f"- {cve['id']} — {cve['description'][:100]}...")
