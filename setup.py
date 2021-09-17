from setuptools import setup, find_packages

setup(
    name="RK",
    version='1.0',
    author="A.A. Lobaskin, A.S. Eremin, SPbU",
    author_email='ravelraise@gmail.com',
    packages=find_packages(exclude=['RK']),
    install_requires=['numpy']
)
