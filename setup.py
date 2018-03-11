from codecs import open
from os import path

from setuptools import setup


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="flake8-terningkast",
    version="1.0",
    description="A flake8 plugin for terningkast",
    long_description=long_description,
    url="https://github.com/hargoniX/flake8-terningkast",
    author="Henrik Boeving",
    author_email="hargoniX@gmail.com",
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Linter",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
    keywords=["terningkast", "flake8", "code rating"],
    packages=["flake8_terningkast"],
    install_requires=["flake8"],
    entry_points={
        'flake8.report': [
            "terningkast = flake8_terningkast:TerningkastPlugin",
        ],
    },
    package_data={
        "flake8_terningkast": ["images/*"]
    }
)
