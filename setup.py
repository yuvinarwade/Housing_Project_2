from setuptools import setup,find_packages
from typing import List

#Declearing variable for setup function
PROJECT_NAME="housing prediction"
VERSION="0.0.5"
AUTHOR="YK Narwade"
DESCRIPTION="this is first housing project"
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description :This function is going to return list of requirement mention in the requirements.txt file

    return this function i sgoing to return a list which contain name of libraaries mention in the requirements.txt
    """


    with open (REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list=[lib_name.replace("\n","") for lib_name in requirement_file.readlines()]
        print(requirement_list)
        if "-e ." in requirement_list:
            requirement_list.remove("-e .")

        return requirement_list  



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()
)