# scripts/patch_status_checker.py

import requests
from packaging import version  # for comparing version strings
from check_installed_versions import get_installed_versions

def check_pypi_latest(pkg_name):
    url = f"https://pypi.org/pypi/{pkg_name}/json"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()["info"]["version"]
    except Exception as e:
        print(f"⚠️ PyPI check failed for {pkg_name}: {e}")
    return None

def check_npm_latest(pkg_name):
    url = f"https://registry.npmjs.org/{pkg_name}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()["dist-tags"]["latest"]
    except Exception as e:
        print(f"⚠️ npm check failed for {pkg_name}: {e}")
    return None

def is_update_available(current, latest):
    try:
        return version.parse(latest) > version.parse(current)
    except Exception:
        return False

def check_all_patch_status(installed_versions):
    patch_report = {}

    for pkg, current_version in installed_versions.items():
        if pkg in ["vue", "graphql"]:  # npm packages
            latest = check_npm_latest(pkg)
            registry = "npm"
        else:  # assume PyPI for others
            latest = check_pypi_latest(pkg)
            registry = "PyPI"

        if latest:
            patch_report[pkg] = {
                "current": current_version,
                "latest": latest,
                "update_available": is_update_available(current_version, latest),
                "registry": registry
            }

    return patch_report

# Example usage
if __name__ == "__main__":
    installed = get_installed_versions()
    report = check_all_patch_status(installed)

    print("📦 Patch Status Report:\n")
    for pkg, info in report.items():
        status = "✅ Up to date" if not info["update_available"] else "⚠️ Update available"
        print(f"- {pkg} ({info['registry']}) → {info['current']} → {info['latest']} — {status}")
