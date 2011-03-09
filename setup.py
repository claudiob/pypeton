from distutils.core import setup

setup(
	name         = 'pypeton',
	packages     = ['pypeton',],
	scripts      = ['pypeton/pypeton',],
	version      = 'v0.4.0',
	author       = 'RED Interactive Agency',
	author_email = 'geeks@ff0000.com',

	package_data = {
		'pypeton': [
			'files/*',
		]
	},

	url          = 'http://www.github.com/ff0000/pypeton/',
	download_url = 'http://www.github.com/ff0000/pypeton/',

	license      = 'MIT license',
	description  = """ Tool to start Django and Bongo projects """,

	long_description = open('README.rst').read(),
	install_requires = ['pycolors',],

	classifiers  = (
		'Development Status :: 3 - Alpha',
		'Environment :: Web Environment',
		'Framework :: Django',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Topic :: Software Development',
	),
)
