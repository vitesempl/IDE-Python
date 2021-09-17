from setuptools import setup, find_packages


setup(
    name="RK",

    version='1.0',

    author="Aleksandr Lobaskin, Alexey Eremin, SPbU",

    packages=find_packages(exclude=['RK']),

    install_requires=[
        'numpy'
    ]
)