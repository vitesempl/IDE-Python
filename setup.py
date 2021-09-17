from setuptools import setup, find_packages


setup(
    name="RK",

    author="Aleksandr Lobaskin, Alexey Eremin, SPbU",

    packages=find_packages(exclude=['RK']),

    install_requires=[
        'numpy'
    ]
)