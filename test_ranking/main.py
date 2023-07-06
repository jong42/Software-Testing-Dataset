import os
import pandas as pd
from create_training_data import list_files, get_project_urls, clone_project, remove_project
from rank_testcases import get_static_features

temp_repo_path = '/home/jonas/Desktop/temp_repo'
outpath = '../code_metrics.csv'
df = []
# Get names and urls of possible repos
repo_names, repo_urls = get_project_urls()
for repo_name,url in zip(repo_names,repo_urls):
    # Delete previous repo
    if os.path.isdir(temp_repo_path):
        remove_project(temp_repo_path)
    # Clone repo
    try:
        clone_project(url, temp_repo_path)
        #codebase_path = os.path.join(temp_repo_path,repo_name)
        files = list_files(temp_repo_path)
        # Filter for python files
        files = [file for file in files if '.py' in file]
        # Exclude tests
        files = [file for file in files if 'test' not in file]
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
    except FileNotFoundError: pass

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