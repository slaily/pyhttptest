from re import search
from setuptools import (
    setup,
    find_namespace_packages
)


with open('README.rst', 'r', encoding='utf8') as file:
    readme = file.read()

with open('pyhttptest/__init__.py', 'rt', encoding='utf8') as file:
    version = search(
        r"__version__ = ['\"]([^'\"]+)['\"]",
        file.read()
    ).group(1)

setup(
    name='pyhttptest',
    version=version,
    author='Iliyan Slavov',
    author_email='slavov.iliyan96@gmail.com',
    description='A command-line tool for HTTP tests over RESTful APIs',
    long_description=readme,
    keywords='HTTP test RESTFul API JSON',
    license='BSD 3-Clause License',
    url='https://github.com/slaily/pyhttptest',
    project_urls={
        'Issues': 'https://github.com/slaily/pyhttptest/issues',
    },
    packages=find_namespace_packages(include=['pyhttptest', 'pyhttptest.*']),
    install_requires=[
        'click==7.0',
        'ijson==2.5.1',
        'jsonschema==3.1.1',
        'requests==2.22.0',
        'tabulate==0.8.5'
    ],
    tests_require='pytest',
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'pyhttptest = pyhttptest.cli:main',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing'
    ],
)
