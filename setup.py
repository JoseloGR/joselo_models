from setuptools import setup, find_packages

setup(
    name='joselo_models',
    description='Data validation models',
    author='JoseloGR',
    author_email='joselo@flat.mx',
    packages=find_packages(),
    install_requires=[
        'pydantic==1.9.0',
        'pandas==1.4.1'
    ],
)
