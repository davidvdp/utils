from setuptools import setup, find_packages
from pathlib import Path

this_dir = Path(__file__).parent

with open(this_dir / 'requirements.txt') as file:
    requirements = '\n'.join(file.readlines())

with open(this_dir / 'README.md') as file:
    long_description = file.read()

version = '0.0.5'
package_name = 'utils'
top_ns = 'dvdp'

setup(
    name=f'{top_ns}.{package_name}',
    version=version,
    packages=find_packages(),
    download_url=f'https://github.com/davidvdp/{package_name}/archive/v'
                 f'{version}.tar.gz',
    url=f'https://github.com/davidvdp/{package_name}',
    author='David van der Pol',
    author_email='david@davidvanderpol.com',
    license='MIT',
    description='Python utilities.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=requirements,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=[
        'Utils'
    ],
)