from setuptools import setup

setup(
    name="emf",
    version='0.1',
    py_modules=['emf_cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        emf=emf_cli:cli
    ''',
)