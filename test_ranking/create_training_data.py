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
    pass

#execute the tests
def execute_tests(path:str):
    subprocess.run(['pytest', path])

if __name__ == '__main__':
    list_projects()
    url = 'https://gitlab.com/megabyte-labs/templates/python-cli'
    outdir = '/home/jonas/Desktop/temp_repo'
    #clone_project(url, outdir)




#Make a subclass of project that can clone, run tests and delete the local clone