#! /usr/bin/env python3 

"""基本ライブラリの読み込み""" 
import numpy as np 
import pandas as pd 
from scipy import stats 

""" Coversion from SHIFT-JIS to UTF8 """
import codecs


""" データの保存 """
from datetime import datetime 
import csv 

"""グラフ描画"""
#from ipython.display import display  
from matplotlib import pylab as plt 
import seaborn as sns 
#%matplotlib inline 

"""グラフのサイズの指定"""
from matplotlib.pylab import rcParams 
rcParams['figure.figsize'] = 15, 6 

"""統計モデル""" 
import statsmodels.api as sm 

""" 同定 """
class StatClass(object):
    def __init__(self, num):
        self.num = num 





if __name__ == "__main__":
    csv_name  =  'UTF8_190624.csv' # file name to analysis
    


