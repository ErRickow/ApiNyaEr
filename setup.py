import os

from setuptools import find_packages, setup


def read_requirements():
    try:
        with open("requirements.txt") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print("Warning: requirements.txt not found. No dependencies will be installed.")
        return []


def read(fname, version=False):
    text = open(os.path.join(os.path.dirname(__file__), fname), encoding="utf8").read()
    return text


setup(
    name="ApiNyaEr",
    version="1.4",
    description="An Api Compile for another source",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Er",
    url="https://pypi.org/project/ApiNyaEr",
    packages=find_packages(),
    install_requires=read_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
    keywords="Python Api, With Easy Instalation",
)
