
from setuptools import setup, find_packages

setup(
    name='fw_utils',
    version='0.1',
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'plotly', 'IPython'],
    author='Warrick Sabatta',
    description='Framework utilities for data science and reporting',
)
