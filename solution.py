import pandas as pd
import numpy as np

from scipy.stats import ks_2samp


chat_id = 670223087 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    statistic, pvalue = ks_2samp(x, y)
    alpha = 0.03
    reject = pvalue < alpha
    return reject
