"""Setup for the pdfformfields package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Nguyen Ba Long",
    author_email="Nguyen.Ba.Long13@gmail.com",
    name='pdfformfields',
    license="GPLv3+",
    description='pdfformfields is a Python wrapper around pdftk that fills in pdf forms from a Python dictionary.',
    version='v0.0.1',
    long_description=README,
    url='https://github.com/Balonger/pdfformfields',
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=['xfdfgen'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)