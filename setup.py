__author__ = 'ameadows'

import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import datanexus


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

setup(
    name='dataNexus',
    version=datanexus.__version__,
    url='https://github.com/OpenDataAlex/dataNexus',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    description='Data source version control and lineage tool.',
    author='Alex Meadows',
    author_email='alexmeadows@bluefiredatasolutions.com',
    packages=find_packages(),
    install_requires=[
        'appdirs==1.4.0',
        'configparser==3.5.0b1',
        'docutils==0.12',
        'ecdsa==0.11',
        'GitPython==1.0.1',
        'Jinja2==2.7.3',
        'MarkupSafe==0.23',
        'Pygments==1.6',
        'PyYAML==3.11',
        'Sphinx==1.2.3',
        'SQLAlchemy==0.9.7',
        'py==1.4.24',
        'tox==1.7.2'

    ],
    tests_require=[
        'PyMySQL==0.6.2',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers'
    ],
    cmdclass={'tox': Tox},
    keywords='database, version control, data lineage',
    test_suite='datanexus.test',
    entry_points={
        'console_scripts': [
            'dataNexus = datanexus.dataNexus:main',
            'datanexus = datanexus.dataNexus:main',
        ]
    },
    package_data={
        'dataNexus': ['.datanexus-settings.yml'],
    }
)
