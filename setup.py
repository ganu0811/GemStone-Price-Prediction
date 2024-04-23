from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str)-> List[str]:
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

setup(
    name = "DiamondPricePrediction",
    version = '0.0.1',
    author = "Ganesh Adarkar",
    author_email = "ganesh.adarkar0811@gmail.com",
    description ="A python package for connecting with database",
    install_requires = ['scikit-learn','pandas','numpy'],
    packages = find_packages(),
    
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
    install_requires = get_requirements("./requirements_dev.txt"),
)