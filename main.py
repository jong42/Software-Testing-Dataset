from pydeps.pydeps import call_pydeps


def create_dependency_graph(path:str):
    """
    Creates a dependency graph of a codebase at a given location
    :param path: string. The location of the codebase
    :return:
    """
    call_pydeps(path)

if __name__ == '__main__':
    path = "/home/jonas/Desktop/pydeps_local/pydeps_local"
    create_dependency_graph(path)