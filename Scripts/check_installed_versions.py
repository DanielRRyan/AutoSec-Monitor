# scripts/check_installed_versions.py

import json
import os
import re

def parse_python_requirements(path="backend/requirements.txt"):
    versions = {}
    if not os.path.exists(path):
        print(f"⚠️ Python requirements file not found at {path}")
        return versions

    with open(path, "r") as f:
        for line in f:
            if "==" in line:
                pkg, ver = line.strip().split("==")
                versions[pkg.lower()] = ver
    return versions

def parse_node_package_json(path="frontend/package.json"):
    versions = {}
    if not os.path.exists(path):
        print(f"⚠️ package.json not found at {path}")
        return versions

    with open(path, "r") as f:
        pkg_data = json.load(f)
        for dep_type in ["dependencies", "devDependencies"]:
            deps = pkg_data.get(dep_type, {})
            for pkg, ver in deps.items():
                cleaned_ver = re.sub(r"[^0-9.]", "", ver)  # Strip ^, ~, etc.
                versions[pkg.lower()] = cleaned_ver
    return versions

def get_installed_versions():
    all_versions = {}
    all_versions.update(parse_python_requirements())
    all_versions.update(parse_node_package_json())
    return all_versions

# Example usage
if __name__ == "__main__":
    versions = get_installed_versions()
    print("🔍 Installed package versions:\n")
    for pkg, ver in versions.items():
        print(f"- {pkg} @ {ver}")
