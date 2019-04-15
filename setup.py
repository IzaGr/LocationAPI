from setuptools import setup
setup(
    name = 'locapi',
    version = '0.1.0',
    packages = ['locapi'],
    entry_points = {
        'console_scripts': [
            'locapi = locapi.__main__:main'
        ]
    })
