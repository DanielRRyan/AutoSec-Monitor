# scripts/launch_sandbox.py

import subprocess
import os

def launch_python_sandbox(image="python:3.10", packages=None):
    """
    Launch a Docker container with the given Python image and install specified packages.
    """
    packages = packages or ["fastapi", "sqlalchemy"]
    pkg_str = " ".join(packages)

    print(f"🚀 Launching sandbox with: {image}")
    print(f"📦 Installing packages: {pkg_str}")

    dockerfile = f"""
    FROM {image}
    RUN pip install {pkg_str}
    CMD ["python3"]
    """

    sandbox_dir = "sandbox_env"
    os.makedirs(sandbox_dir, exist_ok=True)

    dockerfile_path = os.path.join(sandbox_dir, "Dockerfile")
    with open(dockerfile_path, "w") as f:
        f.write(dockerfile)

    image_tag = "autosec-sandbox"

    try:
        subprocess.run(["docker", "build", "-t", image_tag, sandbox_dir], check=True)
        subprocess.run(["docker", "run", "-it", "--rm", image_tag], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during sandbox launch: {e}")

# Example usage
if __name__ == "__main__":
    launch_python_sandbox(
        image="python:3.10",
        packages=["fastapi==0.104.1", "sqlalchemy"]
    )
