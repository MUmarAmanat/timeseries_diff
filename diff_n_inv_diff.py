import numpy as np


def difference(dataset, interval=1):
    """
    dataset:
        type:list, 
        Desc: list contaning timeseries values
    interval: 
        type:integers
        Desc: Differencing order
    """
    def do_diff(dataset):
        diff = list()
        for i in range(1, len(dataset)):
            value = dataset[i] - dataset[i - 1]
            diff.append(value)
        return diff

    diff_list = dataset
    last_obs_value = []
    for _ in range(1, interval + 1):
        last_obs_value.append(diff_list[0])
        diff_list = do_diff(diff_list)
    return diff_list, last_obs_value


def revert_difference(diff_forecast, last_obs_list = []):
    """
    diff_forecast:
        type:list
        Desc: Differenced forecast
    last_obs_list:
        type:list
        Desc: list of last observed values while doing difference
              example [last_obs_for_1st_diff, last_obs_for_2nd_diff, ...]
    """
    undiff_list = []
    undiff_list = diff_forecast
    for i in reversed(last_obs_list):
        undiff_list = np.r_[i, undiff_list]
        for i in range(1, len(undiff_list)):
            undiff_list[i] = undiff_list[i-1] + undiff_list[i]
    return undiff_list