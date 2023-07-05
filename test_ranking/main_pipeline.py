import os
import pandas as pd
from create_training_data import get_project_urls, clone_project, remove_project
from rank_testcases import get_static_features

temp_repo_path = '/home/jonas/Desktop/temp_repo'
outpath = 'code_metrics.csv'
df = []
# Get urls of possible repos
repo_urls = get_project_urls() # TODO: Write get_project_urls

for url in repo_urls:
    # Clone repo
    clone_project(url, temp_repo_path)
    codebase_path = os.path.join(temp_repo_path,repo_name) # TODO: get repo name
    files = os.listdir(codebase_path)
    # Get code metrics from repo, write them in a  dataframe
    abs_filepaths = [os.path.join(temp_repo_path,file) for file in files]
    code_metrics = get_static_features(abs_filepaths)
    for filename,values in code_metrics:
        # df.append([url,filename,values[], values['avg_cc']]) #TODO: insert all the metrics names

# Delete repo
remove_project(temp_repo_path)
# Save dataframe as csv
df = pd.DataFrame(df,columns=['url','filename','avg_cc']) # TODO: insert all metrics names
df.to_csv(outpath)