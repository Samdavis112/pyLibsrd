from setuptools import find_packages, setup

setup(
	name="libsrd",
	version="1.0.0",
	description="LibSrd is a library containing modules I use repeatedly.",
	long_description=open("README.md").read(),
	author="Sam Davis",
	author_email="sam076davis@gmail.com",
	packages=find_packages(),
	install_requires=[
		"pillow",
		"tabulate",
		"pypdf"
	],
	url="https://github.com/Samdavis112/libsrd",
	entry_points={
		'console_scripts': [
			'mergepdfs = libsrd.merge_pdf:script',
			'imgconvert = libsrd.image_convert:script',
		],
	},
)