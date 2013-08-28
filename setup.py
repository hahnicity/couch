
#!/usr/bin/env python
from setuptools import setup, find_packages

__version__ = "0.1"


setup(
    name="couch",
    author="Gregory Rehm",
    author_email="grehm87@gmail.com",
    version=__version__,
    description="A web framework for slothpal to lounge around on"
    install_requires=[
        "slothpal",
        "tornado"
    ],
)
