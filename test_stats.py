from stats_descriptive import stats_mean, stats_median, stats_mode, stats_std
import pandas as pd

data = pd.read_csv("forbes_2022_billionaires.csv")

def test_values():
    assert (stats_mean(data)) == 64.21068938807126
    assert (stats_median(data)) == 64.0
    assert (stats_mode(data)[0]) == 57
    assert (stats_std(data)) == 13.401258058138897


test_values()
