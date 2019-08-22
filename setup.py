from setuptools import (
    setup,
    find_packages
)


setup(
    name='pyreqtest',
    version='0.1',
    author='Iliyan Slavov',
    author_email='slavov.iliyan96@gmail.com',
    description='A command-line tool for HTTP tests over RESTful APIs',
    url='https://github.com/slaily/pyreqtest',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing'
    ],
)
