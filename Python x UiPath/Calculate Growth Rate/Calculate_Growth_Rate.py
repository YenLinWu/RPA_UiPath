# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:56:18 2020

@author: YenLin
"""
import pandas as pd

def Growth_Rate( xlsxPath, Groupers, TargetColumn, OutputPath, OutputSheetName='Sheet1' ): 
    
    Groupers = Groupers.split(',')
    
    raw_data = pd.read_excel( xlsxPath ) 
    raw_data['GROWTH RATE'] = raw_data.sort_values(['YEAR']).groupby(Groupers)[[TargetColumn]].pct_change()
    raw_data.fillna( '--', inplace = True )
    gr = raw_data.sort_values( Groupers+['YEAR'] )
    gr['GROWTH RATE'] = gr.apply( lambda x: '{:.2%}'.format(round(x['GROWTH RATE'],4)) if x['GROWTH RATE']!='--' else '--', axis=1 )
    gr.to_excel( OutputPath, sheet_name = OutputSheetName, index = False )   