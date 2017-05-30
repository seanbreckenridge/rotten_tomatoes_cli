from setuptools import setup, find_packages

setup(
    name="rotten_tomatoes_cli",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click==6.7",
        "rotten_tomatoes_client==0.0.3",
        "terminaltables==3.1.0",
        "termcolor==1.1.0"
    ],
    entry_points={
        "console_scripts": [
            "rotten= scripts.rotten:rotten"
        ],
    }
)