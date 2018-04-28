from setuptools import setup, find_packages

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "Click"]

setup(
    name="emp",
    version='0.1',
    py_modules=['emp_cli'],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        emp=emp_cli:cli
    ''',
)