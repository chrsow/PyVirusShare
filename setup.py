import setuptools
from distutils.util import convert_path
import sys

main_ns = {}
with open(convert_path('virusshare/version.py')) as f:
    exec(f.read(), main_ns)

if sys.version_info < (3, 6, 0):
    raise RuntimeError('PyVirusShare requires Python 3.6.0+')

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='PyVirusShare',
    version=main_ns['__version__'],
    description='A Python library/command line to interact with VirusShare API v2.',
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/chrsow/VirusShare',
    packages=['virusshare'],
    python_requires='>=3.6.0',
    install_requires=[            # I get to this in a second
        'requests'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',  
        'License :: OSI Approved :: MIT License'
    ])