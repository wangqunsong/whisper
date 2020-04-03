"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/wangqunsong/whisper
"""
import setuptools
import os


with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name="whisper",
	version="0.0.1",
	author="zootopia",
	author_email=" ",
	description="this is a test",
	long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wangqunsong/whisper",
    packages=setuptools.find_packages(),
    install_requires=['Pillow>=5.1.0', 'numpy==1.14.4'],
    entry_points={
        'console_scripts': [
            'whisper=whisper:main'
        ],
    },
    classifiers=(
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    # These classifiers are *not* checked by 'pip install'. See instead
    # 'python_requires' below.
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    "Programming Language :: Python",
),
	)