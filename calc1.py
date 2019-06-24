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




""" Convert from SHIFT-JIS to utf-8 """
def ShiftJis2Utf8(csv_name):
    now    = datetime.now()
    file_name = 'dataset/'+csv_name
    print(file_name)
    ''' Convert File from Shiftjis to UTF8 '''
    #S_file = open(file_name, 'w', encoding='cp932')                                 # Instance to open the shift-jis file
    #U_file = open('dataset/UTF8_{0:%Y%m%d}.csv'.format(now), 'w', encoding='utf8')  # Instance to open the UTF-8 file 
    #U_file.write(S_file.read()) # Write the contents of shift-jis file to the UTF-8 
    with open('dataset/UTF8_{0:%Y%m%d}.csv'.format(now), 'w', encoding='utf8') as fout:
        with open(file_name, encoding='cp932') as fin:
            fout.write(fin.read())



if __name__ == "__main__":
    csv_name  = 'SHIFT_JIS_190624.csv' 
    ShiftJis2Utf8(csv_name) 

