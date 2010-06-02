from setuptools import setup, find_packages
 
setup(name='cm-py',
    version='0.1',
    description='Python wrapper for accessing the Campaign Monitor API using SOAP',
    long_description=open('README').read(),
    author='Christopher Cote',
    url='http://github.com/campaignmonitor/cm-py',
    packages=find_packages()
)