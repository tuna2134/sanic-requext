from setuptools import setup, find_packages


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="sanic-requext",
    version="0.1.0a",
    description="Easy to use form",
    long_description=long_description,
    author="mc_fdc",
    packages=find_packages()
)