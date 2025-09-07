# scripts/utils.py

import requests
from packaging import version
import time
import logging
import re

# ---------------
# Logger Setup
# ---------------

logging.basicConfig(
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    level=logging.INFO
)

# ---------------
# Version Comparison
# ---------------

def is_outdated(current: str, latest: str) -> bool:
    try:
        return version.parse(current) < version.parse(latest)
    except Exception as e:
        logging.warning(f"Could not compare versions {current} vs {latest}: {e}")
        return False

# ---------------
# Safe HTTP Request
# ---------------

def safe_get(url, headers=None, timeout=5):
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        logging.warning(f"HTTP GET failed for {url}: {e}")
        return None

# ---------------
# Rate Limiter
# ---------------

def wait(seconds=1):
    logging.debug(f"⏳ Waiting {seconds}s to respect rate limits...")
    time.sleep(seconds)

# ---------------
# Normalize Package Names
# ---------------

def normalize_pkg_name(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_\-\.]", "", name.strip().lower())

# ---------------
# Pretty Print Output
# ---------------

def status_color(msg, is_alert=False):
    return f"\033[91m{msg}\033[0m" if is_alert else f"\033[92m{msg}\033[0m"
