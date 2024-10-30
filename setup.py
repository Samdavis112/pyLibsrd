from setuptools import find_packages, setup

setup(
	name="libsrd",
	version="1.0.0",
	description="A tool that will scan the current directory for specified image types, then will convert them all into another specified format.",
	author="Sam Davis",
	author_email="sam076davis@gmail.com",
	packages=find_packages(),
	install_requires=[
		"pillow",
		"tabulate",
		"pypdf"
	],
	entry_points={
		'console_scripts': [
			'mergepdfs = libsrd.merge_pdf:script',
			'imgconvert = libsrd.image_convert:script',
		],
	},
)