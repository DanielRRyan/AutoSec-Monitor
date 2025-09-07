# Add these imports
from db import SessionLocal
from models import CVEAlert
from datetime import datetime

# Inside the Mutation class → scan_cves function:
@strawberry.field
def scan_cves(self) -> List[CVEPackageAlerts]:
    """Trigger CVE scan, store results, and return alerts grouped by package."""
    raw_data = run_cve_scan()
    results = []
    db = SessionLocal()

    for pkg, entries in raw_data.items():
        cve_entries = []
        for e in entries:
            cve_entry = CVEAlert(
                package=pkg,
                cve_id=e["id"],
                description=e["description"],
                published=datetime.fromisoformat(e["published"].replace("Z", "+00:00")),
                source=e["source"]
            )
            db.add(cve_entry)
            cve_entries.append(
                CVEEntry(
                    id=e["id"],
                    description=e["description"],
                    published=e["published"],
                    source=e["source"]
                )
            )
        results.append(CVEPackageAlerts(package=pkg, entries=cve_entries))

    db.commit()
    db.close()

    return results
