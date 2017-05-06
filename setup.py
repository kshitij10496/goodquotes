from setuptools import setup, find_packages


setup(
    name='GoodQuotes',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'Click',
        'requests',
        'bs4'
    ],
    entry_points= {
        'console_scripts': [
            'goodquotes = goodquotes.cli:cli'
        ]
    }
)
