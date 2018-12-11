from setuptools import find_packages, setup

setup(
    name='pyseeyou',
    version='0.4.0',
    description='A Python Parser for the ICU MessageFormat.',
    author='Siame Rafiq',
    author_email='mail@sia.me.uk',
    packages=find_packages(exclude=['tests']),
    install_requires=['parsimonious', 'toolz', 'future'],
    tests_require=['pytest'],
    url='https://github.com/rolepoint/pyseeyou',
    download_url='https://github.com/rolepoint/pyseeyou/archive/v0.4.0.tar.gz',
    keywords='python i18n messageformat python3 python2')
