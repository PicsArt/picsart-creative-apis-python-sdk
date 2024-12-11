import os
import re

from setuptools import find_packages, setup


def get_version():
    """Read the version from src/picsart_sdk/version.py."""
    version_file = os.path.join(
        os.path.dirname(__file__), "src", "picsart_sdk", "version.py"
    )
    with open(version_file, "r") as f:
        content = f.read()
        match = re.search(r"^__version__ = ['\"]([^'\"]+)['\"]", content, re.MULTILINE)
        if match:
            return match.group(1)
        raise RuntimeError("Version not found in version.py")


setup(
    name="picsart-creative-apis-py-sdk",
    version=get_version(),  # Dynamically fetched
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
