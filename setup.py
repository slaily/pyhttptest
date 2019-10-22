from setuptools import (
    setup,
    find_namespace_packages
)


setup(
    name='pyreqtest',
    version='0.1a',
    author='Iliyan Slavov',
    author_email='slavov.iliyan96@gmail.com',
    description='A command-line tool for HTTP tests over RESTful APIs',
    keywords='HTTP test RESTFul API JSON',
    license='BSD 3-Clause License',
    url='https://github.com/slaily/pyreqtest',
    project_urls={
        'Issues': 'https://github.com/slaily/pyreqtest/issues',
    },
    packages=find_namespace_packages(include=['pyreqtest', 'pyreqtest.*']),
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
            'pyreqtest = pyreqtest.cli:main',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing'
    ],
)
