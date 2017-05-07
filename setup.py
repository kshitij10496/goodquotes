from setuptools import setup, find_packages


setup(
    name = 'GoodQuotes',
    author = 'kshitij10496',
    author_email = 'KshitijSaraogi@gmail.com',
    url = 'https://github.com/kshitij10496/goodquotes',
 
    version = '1.0',
    download_url = 'https://github.com/kshitij10496/goodquotes/archive/v1.0.tar.gz',
    
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
