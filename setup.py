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
        'aiohttp==3.0.3',
        'codecov==2.0.15',
        'coverage==4.5.1',
        'motor==1.2.1',
        'pytest==3.4.1',
        'pytest-cov==2.5.1',
        'sanic==0.7.0',
        'sanic-motor==0.2.8',
    ]
)
