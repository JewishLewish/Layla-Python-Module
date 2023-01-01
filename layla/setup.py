from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
    name = 'Layla Eval',
    version = '1.0.4',
    author= "JewishLewish",
    description="Math Evaluator that uses C Code over Python",
    packages=find_packages(),
    url = "https://github.com/JewishLewish/Layla-Python-Module",
    long_description=open('README.txt').read(),
    classifiers=classifiers
)