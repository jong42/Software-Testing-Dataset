from typing import List, Dict
from radon.complexity import SCORE
from radon.cli import Config
from radon.visitors import Function
from radon.cli.harvest import CCHarvester, RawHarvester


def get_static_features(filepaths:List[str])-> Dict:
    """
    Extract a set of code metrics from code files
    :param filepath: List of strings. paths to the files to analyse
    :return: Dictionary. Contains the locations of the files as keys, and a dictionary containing the metrics as values
    """
    config = Config(
        exclude=None,
        ignore=None,
        no_assert=True,
        show_closures=False,
        order=SCORE,
        min='A',
        max='F',
        average=True
    )
    h_raw = RawHarvester(filepaths, config)
    h_cc = CCHarvester(filepaths, config)
    results = {name: metrics for name, metrics in h_raw.results}

    # h_cc.results holds cyclomatic complexity per function and class.
    # Compute the average cyclomatic complexity per file
    for i in h_cc.results:
        cc_sum = 0
        cc_count = 0
        for j in i[1]:
            if isinstance(j, Function):  # only look at the functions, not at classes
                cc_sum += j.complexity
                cc_count += 1
        try:
            avg_cc = cc_sum/cc_count
        except ZeroDivisionError:
            avg_cc = 'NaN'
        results[i[0]]['avg_cc'] = avg_cc
    return results


if __name__ == "__main__":
    paths = ['/home/jonas/Desktop/pydeps_local/pydeps_local/colors.py',
             '/home/jonas/Desktop/pydeps_local/pydeps_local/cli.py']
    print(get_static_features(paths))

