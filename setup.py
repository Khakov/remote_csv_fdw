import subprocess
from setuptools import setup, find_packages, Extension

setup(
  name='remote_fdw',
  version='1.0.0',
  author='Khakov Rustam',
  link = 'https://github.com/Khakov/remote_csv_fdw',
  license='Postgresql',
  packages=['remote_fdw']
)