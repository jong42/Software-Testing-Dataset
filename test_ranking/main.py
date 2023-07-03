import re
import json
from select import create_dependency_graph, get_affected_files
from prioritize_random import prioritize_random

codebase_path = "/home/jonas/Desktop/pydeps_local"
commit_path = "commit.txt"
graph_path = "dep_graph.json"


create_dependency_graph(codebase_path, graph_path)

# Extract filenames from commit
filenames = []
with open(commit_path, "r") as f:
    lines = f.readlines()
    lines = lines[6:-1]
    for line in lines:
        filename = re.findall('/.+\.py',line)[0][1:]
        filenames.append(filename)


# Load graph into Dict
with open(graph_path, "r") as f:
    dependency_graph = json.load(f)

# query graph for dependent files.
selected_tests = []
for filename in filenames:
    affected_files = get_affected_files(filename, dependency_graph)
    selected_tests.append(affected_files)  # Assumption: Test files have same names as the codebase files
    selected_tests = list(set(selected_tests))  # to remove duplicate entries

ranked_tests = prioritize_random(selected_tests)