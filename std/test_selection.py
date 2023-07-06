import subprocess
from typing import Dict, List


def create_dependency_graph(inpath:str, outpath:str) -> None:
    """
    Creates a dependency graph of a codebase at a given location
    :param inpath: string. The location of the codebase
    :param outpath: string. The location where the output file should be written to
    :return:
    """
    subprocess.run(['pydeps', '--show_deps', '--no-output', '--deps-out ' + outpath])


def get_affected_files(filename:str, dependency_graph: Dict) -> List[str]:
    """
    Get names of all files that could possibly be affected by a change in a given file, according to a given
    dependency graph.
    :param filename: string. name of the file where the change occurred.
    :param dependency_graph: Dictionary. Graph containing the dependencies between files in a codebase.
    :return: List of string. A list of names of the files that have dependencies to the changed file. Includes the changed file
    """
    dependent_files = []

    def recursive_search(node: str) -> None:
        dependent_files.append(node)
        if 'imported_by' in dependency_graph[node].keys():
            for name in dependency_graph[node]['imported_by']:
                recursive_search(name)
    recursive_search(filename)
    return dependent_files


if __name__ == '__main__':
    path = "/home/jonas/Desktop/pydeps_local/pydeps_local"
    outpath = "output.json"
    create_dependency_graph(path, outpath)

