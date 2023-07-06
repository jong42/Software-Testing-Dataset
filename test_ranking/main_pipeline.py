import os
import pandas as pd
from create_training_data import get_project_urls, clone_project, remove_project
from rank_testcases import get_static_features

temp_repo_path = '/home/jonas/Desktop/temp_repo'
outpath = 'code_metrics.csv'
df = []
# Get names and urls of possible repos
repo_names, repo_urls = get_project_urls()

for repo_name,url in zip(repo_names,repo_urls):
    # Clone repo
    clone_project(url, temp_repo_path)
    codebase_path = os.path.join(temp_repo_path,repo_name) 
    files = os.listdir(codebase_path)
    # Filter for python files
    files = [file for file in files if '.py' in file]
    # Get code metrics from repo, write them in a  dataframe
    abs_filepaths = [os.path.join(temp_repo_path,file) for file in files]
    code_metrics = get_static_features(abs_filepaths)
    for filename in code_metrics:
        df.append([url,
                   filename,
                   code_metrics[filename]['loc'],
                   code_metrics[filename]['lloc'],
                   code_metrics[filename]['sloc'],
                   code_metrics[filename]['comments'],
                   code_metrics[filename]['multi'],
                   code_metrics[filename]['blank'],
                   code_metrics[filename]['single_comments'],
                   code_metrics[filename]['avg_cc']])

# Delete repo
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
                               'single_comments',
                               'avg_cc'])
df.to_csv(outpath)