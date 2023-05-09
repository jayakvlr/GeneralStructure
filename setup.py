#Setting up all the packages and modules
from typing import List

from setuptools import setup,find_packages




def get_requirements(param):
    requirements=[]
    e='-e .'
    with open(param) as f:
        requirements = f.readlines()
        requirements=[req.replace ('\n','') for req in requirements]
        if e in requirements:
            requirements.remove(e)
        return requirements


setup(
    name='GeneralStructure',
    version='0.0.1',
    author='jayalekshmi',
    author_email='jayakvlr@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)