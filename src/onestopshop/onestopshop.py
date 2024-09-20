"""Main module."""
import numpy as np
import pandas as pd

class OneStopShop:

    def __init__(self):
        d = 'd'

    def geocode(self, address):
        '''
        returns df
        '''
        return pd.DataFrame()


    def get_shapes(self, shape, size):
        '''
        '''
        return pd.DataFrame()
    

    def groupby_cagr(self, series, period):
        '''
        assumes period is in months and multiple of 12
        zhvi_calc['2yr_cagr_of_ttm_avg_of_zhvi'] = (
            zhvi_calc.groupby('zipcode')['ttm_avg_of_zhvi'].apply(lambda x: groupby_cagr(x, 24))
        )
        '''
        return ((series.pct_change(period)+1) ** (1/(period/12)) - 1)


    def ttm_avg(self, series):
        return series.rolling(12).mean()
