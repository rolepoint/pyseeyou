from setuptools import setup, find_packages

setup(
    name='pyseeyou',
    version='0.2.0',
    description='A Python Parser for the ICU MessageFormat.',
    author='Siame Rafiq',
    author_email='mail@sia.me.uk',
    packages=find_packages(exclude=['tests']),
    install_requires=['parsimonious', 'toolz'],
    tests_require=['pytest']
)
