import os
import shutil
import gitlab
import subprocess


def list_projects():
    gl = gitlab.Gitlab()
    # list all the projects
    projects = gl.projects.list(topic='pytest')
    for project in projects:
        print(project)


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

if __name__ == '__main__':
    #list_projects()
    url = 'https://gitlab.com/nicolas.bohorquez/flask-pytest-sample'
    path = '/home/jonas/Desktop/temp_repo'
    test_path = os.path.join(path, 'tests')
    clone_project(url, path)
    execute_tests(path)
    #remove_project(path)





#TODO: Install necessary packages (maybe its also necessary to create new conda envs each time)
#TODO: Extract failure yes/no (1. log the test message, 2. extract from the test message)
#TODO: Make a subclass of project that can clone, run tests and delete the local clone
#TODO: Run over night to get dataset
