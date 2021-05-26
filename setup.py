from setuptools import setup

setup( 
    name ='econometricsstats', 
    version = '1.0.0', 
    description = 'stats wrapper for econometrics', 
    author = 'sw', 
    author_email = None,
    install_requires=['linearmodels==4.24'],
    url = None, 
    py_modules = ['econometrics_stats']
 )

