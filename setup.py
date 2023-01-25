# setup.py
from setuptools import setup, find_packages

setup(
    name='xirr_lite',
    version='0.1',
    packages=find_packages(exclude=["tests"]),
    extras_require={
        'optimize': ['numpy']
    }
)