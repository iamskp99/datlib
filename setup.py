from setuptools import setup

with open("README.md","r") as fh:
    long_description = fh.read()

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3',
  'Programming Language :: Python :: 3.6',
  'Programming Language :: Python :: 3.7',
  'Programming Language :: Python :: 3.9'
]

setup(
    name = "datlib",
    version = "0.0.2",
    description = "A python package for data structures and algorithms.",
    py_modules =  ["graphs","numbertheory","rangeQueries"],
    package_dir = {"":"src"},
    classifiers = classifiers,
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/iamskp99/datlib.git",
    author = "Shashank Kumar Pandey",
    author_email = "iamskp99@gmail.com"
)