
# Software Testing Dataset

## Introduction

This project provides a dataset on code metrics of public gitlab repositories that use Python. It can serve as a start for a training dataset for Machine Learning approaches to prioritize test cases in software projects (see for example Bertolino et al 2020: [Learning-to-Rank vs Ranking-to-Learn: Strategies for Regression Testing in Continuous Integration](https://dl.acm.org/doi/10.1145/3377811.3380369)).

The following metrics are collected for each Python file in a project (excluding tests):
- total number of lines of code (loc)
- number of logical lines of code (lloc)
- number of source lines of code (sloc)
- number of comment lines (comments)
- number of lines which represent multi-line strings (multi)
- number of blank lines (blanks)
- average cyclomatic complexity at function level (avg_cc)



## Usage

To reproduce the dataset, execute the following steps:

1. Create a new Python environment
2. In that environment, run "pip install -r requirements.txt"
3. In that environment, std/execute main.py


## Future work

To be able to use this dataset as training data to prioritize test cases, data on test failure and test runtimes has to be collected for all the repositories. Additionally, data on the test history (how often have previous tests failed, last time a test class was run, etc.) could be considered. For this, an algorithm that automatically clones a repo, installs the necessary packages, and runs all tests has to be written.



