import os

from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

install_requires = [
    "numpy",
    "Pillow"
]

setup(
	name='ple4ship',
	version='0.0.1',
	description='PLE4ship is a fork of PyGame Learning Environment (PLE) to create a naval environement to train and evaluate autonomous agents to avoid collisions.',
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
	url='https://github.com/francois-baptiste/PLE4ship',
	author='Norman Tasfi and Francois BAPTISTE',
	author_email='nope',
	keywords='',
	license="MIT",
	packages=find_packages(),
        include_package_data=False,
        zip_safe=False,
        install_requires=install_requires
)
