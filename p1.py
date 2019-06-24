#! /usr/bin/env python3 

"""基本ライブラリの読み込み""" 
import numpy as np 
import pandas as pd 
from scipy import stats 
"""データ取得"""
import urllib 
import urllib.request 
import json 
import pprint

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


"""データの取得""" 
class GetData(object):
    def __init__(self, appID, url, Keys):
        self.appID  = appID # application ID
        self.url    = url   # apiのurl 
        self.Keys   = Keys
 
    """ JSONデータの取得とJSON形式として読み込むまで """
    def GetData(self):
        #""" 日時の取得 """
        #now      = datetime.now()
        #filename = '{0:%Y}_{0:%m}_{0:%d}.csv'.format(now)
        """ JSONデータの取得"""
        #paramStr = urllib.parse.urlencode(self.Keys) #Keysからパラメータの文字列を取得
        robj     = urllib.request.urlopen(self.url)
        """ データの読み込み """
        resStr   = robj.read().decode()
        """ Jsonで保存""" 
        res      = json.loads(resStr) 
        return res 
    
"""本番"""
if __name__ == "__main__":
    """ 日時のインスタンスを作成 """
    now   = datetime.now()

    appID = "5b1b8199352cf84ce913ac75b63a32d6d911cd14" # 取得したapplicationIDの設定
    """ 小売物価統計調査 (月次) """
    # 参考URL: https://www.e-stat.go.jp/dbview?sid=0003105586
    #url   = "http://api.e-stat.go.jp/rest/2.1/app/getStatsData?" #当該調査用URL from e-stats 
    #url   = "http://api.e-stat.go.jp/rest/2.1/app/json/getStatsData?appId=5b1b8199352cf84ce913ac75b63a32d6d911cd14&lang=J&statsDataId=0003105586&metaGetFlg=Y&cntGetFlg=N&sectionHeaderFlg=1" #パンティストッキングス
    url   = "http://api.e-stat.go.jp/rest/2.1/app/json/getStatsData?cdArea=04100%2C13100&cdCat01=09013&appId=5b1b8199352cf84ce913ac75b63a32d6d911cd14&lang=J&statsDataId=0003105586&metaGetFlg=Y&cntGetFlg=N&sectionHeaderFlg=1" #テレビ(液晶)

    # 設定用Keys 
    Keys = {
        "appID"       : appID,
        "lang"        : "J",
        "statsDataID" : "0003105586",
        "metaGetFlg"       : "Y",
        "cntGetFlg"        : "N",
        "sectionHeaderFlg" : "1"
    }

    """ データの取得 """
    GetData   = GetData(appID, url, Keys)
    JsonData  = GetData.GetData()
    """ 読み出し """
    pprint.pprint(JsonData, depth=4)
    #print(JsonData, flush=True)
    """ 表の情報 """
    table_info_list = JsonData['GET_STATS_DATA']['STATISTICAL_DATA']['TABLE_INF']
    table_data_list = JsonData['GET_STATS_DATA']['STATISTICAL_DATA']
    #table_data_list = JsonData['GET_STATS_DATA']['STATISTICAL_DATA']['RESULT_INF']
    print(table_info_list)
    """ from json to pandas """ 
    df1 = pd.io.json.json_normalize(table_info_list, sep='_') 
    df2 = pd.io.json.json_normalize(table_data_list, sep='')
    #print(df1.columns)
    df1.to_csv('{0:%Y%m%d}_1.csv'.format(now))
    df2.to_csv('{0:%Y%m%d}_2.csv'.format(now))
    

