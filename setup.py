from setuptools import setup
from setuptools import find_packages

setup(
    name='my-gitlint',
    package_data={'my_gitlint': ['*.ini']},
    entry_points={'console_scripts': ['my-gitlint=my_gitlint.cli:main']},
    packages=find_packages(),
    install_requires=['gitlint'],
)