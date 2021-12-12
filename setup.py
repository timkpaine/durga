import io
import os.path
from codecs import open

from setuptools import find_packages, setup

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))
name = "durga"


def get_version(file, name="__version__"):
    path = os.path.realpath(file)
    version_ns = {}
    with io.open(path, encoding="utf8") as f:
        exec(f.read(), {}, version_ns)
    return version_ns[name]


version = get_version(pjoin(here, name, "_version.py"))

with open(pjoin(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

requires = []

requires_dev = [
    "black>=20.",
    "bump2version>=1.0.0",
    "flake8>=3.7.8",
    "flake8-black>=0.2.1",
    "mock",
    "pytest>=4.3.0",
    "pytest-cov>=2.6.1",
    "pytest-rerunfailures>=10.1",
    "recommonmark",
    "Sphinx>=1.8.4",
    "sphinx-markdown-builder>=0.5.2",
    "sphinx-rtd-theme",
] + requires

setup(
    name=name,
    version="0.0.1",
    description="Distributed Object Database",
    long_description=long_description,
    url="https://github.com/timkpaine/durga",
    author="Tim Paine",
    author_email="t.paine154@gmail.com",
    license="Apache 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="object database",
    packages=find_packages(exclude=[]),
    install_requires=requires,
    extras_require={"dev": requires_dev},
    entry_points={
        "console_scripts": [
            "peer=durga.peer:main",
            "tracker=durga.tracker:main",
        ],
    },
)
