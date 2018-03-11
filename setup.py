from codecs import open
from os import path

from setuptools import setup


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="flake8-terningkast",
    version="0.0.1",
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
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    keywords=["terningkast", "flake8", "code rating"],
    py_modules="flake8_terningkast.py",
    install_requires=["flake8"],
    entry_points={
        'flake8.report': [
            "terningkast = flake8_terningkast:TerningkastPlugin",
        ],
    },

)
