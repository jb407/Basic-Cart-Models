from setuptools import setup, find_packages

setup(
    name='shared-code',
    version='0.2',
    packages=find_packages(),
    install_requries=[
        'pydantic'
    ],
)