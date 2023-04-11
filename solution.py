import pandas as pd
import numpy as np

from scipy.stats import ks_2samp


chat_id = 670223087 # Ваш chat ID, не меняйте название переменной

def test_randomizer(x: np.array, y: np.array):
    alpha=0.03
    n = len(x)
    critical_value = 1.36 / np.sqrt(n)
    statistic, p_value = ks_2samp(x, y)
    return statistic > critical_value
