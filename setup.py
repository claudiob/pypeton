from distutils.core import setup

setup(
    name = 'pypeton',
    packages=['pypeton',],
	version = '0.0.1',
    author='FF0000 Geeks',
    author_email='ff0000geeks@ff0000.com',

    package_data={
        'pypeton': [
            'files/*',
        ]
    },

    url='http://www.github.com/ff0000/pypeton/',
    download_url = 'http://www.github.com/ff0000/pypeton/',

    license = 'MIT license',
    description = """ Tool to start Django and Bongo projects """,

    long_description = open('README.rst').read(),
    requires = [],

    classifiers = (
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ),
)
