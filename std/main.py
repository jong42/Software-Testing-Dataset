import os
import pandas as pd
from git_utils import list_files, get_project_urls, clone_project, remove_project
from code_analysis import get_static_features

temp_repo_path = 'temp_repo'
outpath = 'dataset.csv'
df = []

# Get names and urls of possible repos
repo_names, repo_urls = get_project_urls()

for i,(repo_name, url) in enumerate(zip(repo_names, repo_urls)):
    print(i)
    # Clone repo
    try:
        clone_project(url, temp_repo_path)
        files = list_files(temp_repo_path)
        # Filter for python files
        files = [file for file in files if '.py' in file]
        # Exclude tests
        files = [file for file in files if 'test' not in file]
        # Get code metrics from repo, write them in a  dataframe
        code_metrics = get_static_features(files)
        for filename in code_metrics:
            try:
                df.append([url,
                    filename,
                    code_metrics[filename]['loc'],
                    code_metrics[filename]['lloc'],
                    code_metrics[filename]['sloc'],
                    code_metrics[filename]['comments'],
                    code_metrics[filename]['multi'],
                    code_metrics[filename]['blank'],
                    code_metrics[filename]['avg_cc']])
            except KeyError: pass
    except FileNotFoundError: pass
    # Delete repo
    if os.path.isdir(temp_repo_path):
        remove_project(temp_repo_path)

# Save dataframe as csv
df = pd.DataFrame(df, columns=['url',
                               'filename',
                               'loc',
                               'lloc',
                               'sloc',
                               'comments',
                               'multi',
                               'blank',
                               'avg_cc'])
df.to_csv(outpath)
