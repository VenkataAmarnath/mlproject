# responsible in creating ml app as package and deploy in pypi
from typing import List
from setuptools import find_packages,setup # (automaticly finds all packages in our folder)



HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirements.
    '''
    requirements=[]
    with open(file_path,'r') as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='venkat',
    author_email="pendelaamarnath@gmail.com",
    packages=find_packages(),
    #install_requires=["pandas,numpy,seaborn"]
    install_requires=get_requirements('requirements.txt')

)


