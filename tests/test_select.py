import pytest
from test_ranking.select import get_affected_files


def test_get_affected_files():

    filename = "test_module"
    dependency_graph = {
        "test_module":{ "name":"test_module","imported_by":["test_import_module"]},
        "test_import_module":{"name":"test_import_module"}
    }
    affected_files = get_affected_files(filename, dependency_graph)
    assert affected_files == ["test_module", "test_import_module"]
    # name not a string)
    filename = 999
    with pytest.raises(KeyError):
        get_affected_files(filename, dependency_graph)
    # name not in graph
    filename = "noname"
    with pytest.raises(KeyError):
        get_affected_files(filename, dependency_graph)
    # graph not a dict
    filename = "test_module"
    dependency_graph = 999
    with pytest.raises(TypeError):
        get_affected_files(filename, dependency_graph)
    # graph has nodes that are not imported by anything
    filename = "test_module"
    dependency_graph = {
        "test_module":{ "name":"test_module"},
        "test_import_module":{"name":"test_import_module"}
    }
    affected_files = get_affected_files(filename, dependency_graph)
    assert affected_files == ["test_module"]



if __name__ == '__main__':
    test_get_affected_files()