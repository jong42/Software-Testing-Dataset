from pydeps.pydeps import call_pydeps


def create_dependency_graph(inpath:str, outpath:str):
    """
    Creates a dependency graph of a codebase at a given location
    :param inpath: string. The location of the codebase
    :param outpath: string. The location where the output file should be written to
    :return:
    """
    call_pydeps(inpath, show_deps=True, no_output=True, deps_out=outpath, )

if __name__ == '__main__':
    path = "/home/jonas/Desktop/pydeps_local/pydeps_local"
    outpath = "output.json"
    create_dependency_graph(path, outpath)