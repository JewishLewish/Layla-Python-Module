from setuptools import setup, find_packages

classifiers=[
    "Programming Language :: Python :: 3",
    "LICENSE :: OSI Approved :: zLib License",
    "Operating System :: OS Independent",
    "Inteneded Audience :: Education, Data Science"
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