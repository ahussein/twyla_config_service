from setuptools import setup, find_packages

setup(
    name='Twyla Configuration Service',
    version='0.1.0',
    description='Configuration management service for Twyla',
    url='https://api.twyla.com',
    author='Abdelrahman Hussein',
    author_email='ahussein.abdelrahman@gmail.com',
    license='Apache',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'aiohttp',
        'motor',
        'sanic',
        'sanic-motor',
    ]
)
