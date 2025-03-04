# This is the setup.py of my project called "orbitals".
#  The source code is in the src/ folder.

from setuptools import setup, find_packages

setup(
    name="orbitals",
    version="0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},)
