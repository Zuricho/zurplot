# setup.py
from setuptools import setup, find_packages

setup(
    name='zurplot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # dependencies here, e.g.,
        'numpy>=1.18',
        'matplotlib>=3.1',
    ],
)
