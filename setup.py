from setuptools import find_packages, setup


def read_requirements():
    try:
        with open("requirements.txt") as f:
            return f.read().splitlines()
 
    except FileNotFoundError:
        return []


setup(
    name="ApiNyaEr",
    version="1.1",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Er",
    packages=find_packages(),
    install_requires=read_requirements(),
)
