from setuptools import find_packages, setup


def read_requirements():
    try:
        with open("requirements.txt") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


setup(
    name="ApiNyaEr",
    version="1.0",
    packages=find_packages(),
    install_requires=read_requirements(),
)
