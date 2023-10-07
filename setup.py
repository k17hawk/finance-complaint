from setuptools import setup, find_packages
from typing import List
#read the content from Readme.md file and give the description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

#versision is specified
__version__ = "0.0.0"

REPO_NAME = "finance-complaint"
AUTHOR_USER_NAME = "k17hawk"
SRC_REPO = "finance-complaint"
AUTHOR_EMAIL = "kumardahal536@gmail.com"

DESRCIPTION = "This is a sample for industry ready solution"
REQUIREMENT_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT ="-e ."

def get_requirements_list(file_path=REQUIREMENT_FILE_NAME) -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(file_path) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list


setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_EMAIL,
    description=DESRCIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)