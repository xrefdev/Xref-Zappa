import os
import sys
from setuptools import setup
from io import open
from xrefzappa import __version__

with open('README.md') as readme_file:
    long_description = readme_file.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    if sys.version_info[0] == 2:
        required = f.read().splitlines()
    else:
        # This logic is intended to prevent the futures package from being installed in python 3 environments
        # as it can cause unexpected syntax errors in other packages. Futures is in the standard library in python 3
        # and is should never be installed in these environments.
        # Related: https://github.com/Miserlou/Zappa/issues/1179
        required = []
        for package in f.read().splitlines():
            if 'futures' not in package:
                required.append(package)

with open(os.path.join(os.path.dirname(__file__), 'test_requirements.txt')) as f:
    test_required = f.read().splitlines()


def get_package():
    filename = os.path.join(
        os.path.dirname(__file__), 'dist',
        'xref_zappa-{}.tar.gz'.format(__version__)
    )
    return filename


if sys.argv[-1] == 'publish':
    print('Publishing the the package on gemfury:')
    os.system('fury push {} --as xref'.format(get_package()))
    sys.exit()

if sys.argv[-1] == 'tag':
    print('Tagging the version on github:')
    os.system('git tag -a {} -m "version {}"'.format(__version__, __version__))
    os.system('git push --tags')
    sys.exit()


setup(
    name='xrefzappa',
    version=__version__,
    packages=['xrefzappa'],
    install_requires=required,
    tests_require=test_required,
    test_suite='nose.collector',
    include_package_data=True,
    license='MIT License',
    description='Server-less Python Web Services for AWS Lambda and API Gateway',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Miserlou/Zappa',
    author='Rich Jones',
    author_email='rich@openwatch.net',
    entry_points={
        'console_scripts': [
            'xrefzappa=xrefzappa.cli:handle',
            'z=xrefzappa.cli:handle',
        ]
    },
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
