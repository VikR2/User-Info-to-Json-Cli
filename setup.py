from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme =f.read()


setup(
    name='hr',
    vesion='1.0',
    description='command line user export utlility',
    long_description=readme,
    author='Vik Ramineni',
    author_email='satvik.ramineni@abbott.com',
    packages=find_packages('src'),
    packagedir={'','src'},
    install_requires=[],
    entry_points={
        'console_scripts' : 'hr=hr.clin:main',
    }
)