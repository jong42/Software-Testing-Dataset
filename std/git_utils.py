import os
import shutil
from typing import List,Tuple
import gitlab
import subprocess


def list_files(directory_path: str) -> List[str]:
    """
    get all filenames of a directory and its subdirectories.
    Taken from https://www.delftstack.com/howto/python/python-list-all-files-in-directory-and-subdirectories/
    :param directory_path: directory within which to list the filenames
    :return: List of strings. The filenames
    """
    files = []
    for entry in os.scandir(directory_path):
        if entry.is_file():
            files.append(entry.path)
        elif entry.is_dir():
            files.extend(list_files(entry.path))
    return files


def get_project_urls() -> Tuple[List[str], List[str]]:
    """
    Get a list of gitlab repos that use pytest
    :return: Tuple of two lists containing project names and project urls
    """
    project_urls = []
    project_names = []
    gl = gitlab.Gitlab()
    projects = gl.projects.list(topic='pytest')
    for project in projects:
        project_names.append(project.name)
        project_urls.append(project.web_url)
    return project_names, project_urls


def clone_project(url: str, outdir:str) -> None:
    subprocess.run(['git', 'clone', url, outdir])


def remove_project(dir:str) -> None:
    shutil.rmtree(dir)


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
    

#TODO: Install necessary packages (maybe its also necessary to create new conda envs each time)
#TODO: Extract failure yes/no (1. log the test message, 2. extract from the test message)
#TODO: Make a subclass of project that can clone, run tests and delete the local clone
