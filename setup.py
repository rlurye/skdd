from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='skdd',
    version='0.1',
    description='Test project',
    long_description=long_description,
    url='https://github.com/rlurye/skdd',
    author='Roman Lurye',
    author_email='rm.lurye@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='semantic knowledge discovery database',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
)