from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="econometrics_calculator",
    version="1.0",
    author="swxxxxxx",
    author_email="anonymous@gmail.com",
    description="Statsmodel wrapper",
    long_description=long_description,
    url="https://github.com/seungwoo-h/econometrics_calculator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
