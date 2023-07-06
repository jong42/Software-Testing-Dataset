import os
import shutil
from typing import List,Tuple
import gitlab
import subprocess


def list_projects():
    gl = gitlab.Gitlab()
    # list all the projects
    projects = gl.projects.list(topic='pytest')
    for project in projects:
        print(project)


def get_project_urls()->Tuple[List[str],List[str]]:
    """
    Get a list of gitlab repos that use pytest
    :return: Tuple of two lists containing project names and project urls
    """
    project_urls=[]
    project_names=[]
    gl = gitlab.Gitlab()
    projects = gl.projects.list(topic='pytest')
    for project in projects:
        project_names.append(project.name)
        project_urls.append(project.web_url)
    return project_names, project_urls


#clone those projects
def clone_project(url:str, outdir:str):
    subprocess.run(['git', 'clone', url, outdir])

def remove_project(dir:str):
    """
    Remove a directory from the file system
    :param dir:
    :return:
    """
    shutil.rmtree(dir)

#execute the tests
def execute_tests(path:str):
    subprocess.run(['pytest', path])

def install_packages(path:str):
    """
    Creates a new conda environment, activates it and installs all packages from a requirements file
    :param path: path to the requirements file
    """
    # create new conda env
    subprocess.run(['conda', 'create', '--name', 'temp_env', 'python=3', '--yes'])
    #switch to new conda env
    subprocess.run(['conda', 'activate', 'temp_env'])
    # install packages
    subprocess.run(['pip', 'install', '-r', path])

if __name__ == '__main__':
    #list_projects()
    url = 'https://gitlab.com/nicolas.bohorquez/flask-pytest-sample'
    path = '/home/jonas/Desktop/temp_repo'
    requirements_path = os.path.join(path, 'requirements.txt')
    test_path = os.path.join(path, 'tests')
    #clone_project(url, path)
    install_packages(requirements_path)
    #execute_tests(path)
    #remove_project(path)





#TODO: Install necessary packages (maybe its also necessary to create new conda envs each time)
#TODO: Extract failure yes/no (1. log the test message, 2. extract from the test message)
#TODO: Make a subclass of project that can clone, run tests and delete the local clone
#TODO: Run over night to get dataset
